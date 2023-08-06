"""Definition of lattice object and its methods"""

import numpy as np

__all__ = ["Lattice"]

PP_INFO = 100
TAU_MAX = 0.6




class Lattice(object):
    """ Lattice definition D2Q9"""

    def __init__(self, dm, max_vel=None, verbose=False):

        self.tau = TAU_MAX
        self.dm = dm
        self.np_x = dm.shape[1]
        self.np_y = dm.shape[0]
        self.lu_x = dm.delta_x
        self.verbose= verbose
        self.obstacle = np.transpose(dm.obstacle)
        print(dm.fields["vel_u"].shape, dm.fields["vel_v"].shape,)
        self.init_velocity = np.stack(
            (np.transpose(dm.fields["vel_u"]),
             np.transpose(dm.fields["vel_v"])),
            axis=0)
        self.init_density = np.ones((self.np_x, self.np_y)) * dm.rho

        self.velocity = self.init_velocity
        self.density = self.init_density

        if max_vel is None:
            self.max_vel = np.max(dm.fields["vel_u"])
        else:
            self.max_vel = max_vel

        self.dim_q = 9
        self.speed = 1. # 1. # in lu/ts
        
        self._init_lattice_struct()

        self.compute_equilibrium_function()
        # Use it to initialize the distribution function
        self.f_n = self.feq.copy()
        self.f_tmp = self.feq.copy()
        # Initialize density
        self.compute_density()

    def _init_lattice_struct(self):
        # The numbering of the directions in the lattice unit is like this: (see p32)
        # 6 2 5
        # 3 0 1
        # 7 4 8
        # The direction vectors in the lattice unit are relative to the center. (see p32)
        # In 2D this leads to:
        # (-1, 1)     ( 0, 1)     ( 1, 1)
        # (-1, 0)     ( 0, 0)     ( 1, 0)
        # (-1,-1)     ( 0,-1)     ( 1,-1)
        # So with the numbering the direction array is:
        # ( (0,0) (1,0) (0,1) (-1,0) (0,-1) (1,1) (-1,1) (-1,-1) (1,-1) )
        self.directions = np.zeros((self.dim_q, 2), dtype=np.int)
        self.directions[0] = [0, 0]
        self.directions[1] = [1, 0]
        self.directions[2] = [0, 1]
        self.directions[3] = [-1, 0]
        self.directions[4] = [0, -1]
        self.directions[5] = [1, 1]
        self.directions[6] = [-1, 1]
        self.directions[7] = [-1, -1]
        self.directions[8] = [1, -1]

        # weights for each direction for the equilibrium function
        # see p35 after eq17
        # ( 1/36)     ( 1/9 )     ( 1/36)
        # ( 1/9 )     ( 4/9 )     ( 1/9 )
        # ( 1/36)     ( 1/9 )     ( 1/36)
        self.weights = np.zeros(self.dim_q)
        self.weights[0] = 4. / 9.
        self.weights[1] = 1. / 9.
        self.weights[2] = 1. / 9.
        self.weights[3] = 1. / 9.
        self.weights[4] = 1. / 9.
        self.weights[5] = 1. / 36.
        self.weights[6] = 1. / 36.
        self.weights[7] = 1. / 36.
        self.weights[8] = 1. / 36.

        # Bounceback boundary (see p44)
        #         6 2 5         8 4 7
        # Lattice 3 0 1 becomes 1 0 3
        #         7 4 8         5 2 6
        #self.bnd_noslip = np.zeros((self.dim_q), dtype=np.int)
        self.bnd_noslip = [ 0, 3, 4, 1, 2, 7, 8, 5, 6]

        # Bounceback along y and slip along x
        #         6 2 5         7 4 8
        # Lattice 3 0 1 becomes 3 0 1
        #         7 4 8         6 2 5
        #self.bnd_slip_x = np.zeros((self.dim_q), dtype=np.int)
        self.bnd_slip_x = [ 0, 1, 4, 3, 2, 8, 7, 6, 5]

        # Bounceback along x and slip along y
        #         6 2 5         5 2 6
        # Lattice 3 0 1 becomes 1 0 3
        #         7 4 8         8 4 7
        #self.bnd_slip_y = np.zeros((self.dim_q), dtype=np.int)
        self.bnd_slip_y = [ 0, 3, 2, 1, 4, 6, 5, 8, 7]

    def iteration(self, time, time_step):
        """Major iteration."""

        def delta_t_from_tau(tau):
            delta_t = (tau - 0.5) / 3. * self.lu_x * self.lu_x / self.dm.nu_  # [s]
            return delta_t

        def tau_from_delta_t(delta_t):
            tau = 0.5 + delta_t * 3. / (self.lu_x * self.lu_x) * self.dm.nu_
            if tau > TAU_MAX:
                raise RuntimeError("Tau value is too high :", tau)
            return tau

        delta_t = delta_t_from_tau(TAU_MAX)
        t_end = time + time_step
        iteration = 0
        if time + delta_t > t_end:
            if self.verbose:
                print(".  Single iteration")
            delta_t = time_step
            self.tau = tau_from_delta_t(delta_t)
            self.sub_iteration(time)
            time += delta_t
        else:
            while time + delta_t < t_end:
                self.tau = TAU_MAX
                self.sub_iteration(time)
                time += delta_t
                iteration += 1
                if self.verbose and iteration % PP_INFO == 0:
                    print(".   - t [s] =" + str(time))
                    print(".   max_vel:" + str(np.max(self.velocity)))
                
            if time + delta_t > t_end:
                delta_t = t_end-time
                if self.verbose:
                    print(".   Final partial iteration")
                self.tau = tau_from_delta_t(delta_t)
                self.sub_iteration(time)
                time += delta_t

    def sub_iteration(self, time):
        """ Perform the time loop """
        
        self.delta_t = (
            (self.tau - 0.5) / 3.
            * self.lu_x * self.lu_x / self.dm.nu_
        )  # [s]
        # Law of similarity
        # Conversion factor for the velocity
        self.c_vel = self.lu_x / self.delta_t
        self.velocity_lu = self.max_vel / self.c_vel

        self.compute_density()
        self.compute_velocity()
        self.compute_equilibrium_function()
        self.collision()
        self.streaming()
        self.xmin_bnd()
        self.xmax_bnd()
        self.ymin_bnd()
        self.ymax_bnd()
        self.test_iteration(time)

    def test_iteration(self, time):
        max_vel = np.max(self.velocity)
        if max_vel > 360:
            print(" - t [s] =" + time)
            raise RuntimeError("Supersonic speed, probably diverging...")
    
    def compute_velocity(self):
        """ Compute the macroscopic velocity which is an average of
            the microscopic velocities weighted by the directional
            densities (see p34 eq15)
        """        
        self.velocity = (np.dot(self.directions.transpose(),
                                   self.f_tmp.transpose((1, 0, 2)))
                         / self.density)
        
        self.dm.fields["vel_u"] = np.transpose(self.velocity[0, :, :])
        self.dm.fields["vel_v"] = np.transpose(self.velocity[1, :, :])
        #return self.velocity

    def compute_density(self):
        """ Calculate macroscopic densities and velocities from the lattice units.
            The macroscopic density is the sum of direction-specific fluid densities.
            (see p33 eq14)
        """
        self.density = np.sum(self.f_tmp, axis=0)
        #return self.density


    def compute_equilibrium_function(self):
        """ D2Q9 Equilibrium distribution function.
            see p35 eq 17 with the basic speed of the lattice
            set at c=1"""

        # Add a volume force
        # gravity

        rho = self.density
        u = self.velocity
        force = np.zeros(2)
        force[0] = 0
        force[1] = 0.0
        #force[1] = 0.0003
        #u[0, :, :] = u[0, :, :] + domain.tau*force[0]/rho
        #print(">>>", u.shape, domain.np_x, domain.np_y)
        u[1, :, :] = u[1, :, :] + self.tau*force[1]
        # Cohesion
        psi0 = 4.0
        rho0 = 200.0
        G = 120.0
        cohesion_force_buffer = np.zeros((2, self.np_x, self.np_y))
        cohesion_force = np.zeros((2, self.np_x, self.np_y))
        psi = np.zeros((self.np_x, self.np_y))
        psi = psi0 * np.exp(-rho0/rho)
        psi_streamed = np.zeros((self.dim_q, self.np_x, self.np_y))
        for i_dir in range(self.dim_q):
            psi_streamed[i_dir, :, :] = (
                np.roll(
                    np.roll(psi[:, :],
                            self.directions[i_dir, 0],
                            axis=0),
                self.directions[i_dir, 1],
                axis=1)
            )
        for i_dir in range(self.dim_q):
            #print("Shape of weights:", np.shape(lattice.weights[i_dir]))
            #print("Shape of directions:", np.shape(lattice.directions[i_dir, :]))
            #print("Shape of streamed psi:", np.shape(psi_streamed[i_dir, :, :]))
            cohesion_force_buffer[0, :, :] += (
                self.weights[i_dir]
                * self.directions[i_dir, 0]
                * psi_streamed[i_dir, :, :])
            cohesion_force_buffer[1, :, :] += (
                self.weights[i_dir]
                * self.directions[i_dir, 1]
                * psi_streamed[i_dir, :, :])
        cohesion_force[:, :, :] = (
            -G * psi[:, :] * cohesion_force_buffer[:, :, :])
        u[0, :, :] = u[0, :, :] + self.tau*cohesion_force[0, :, :]/rho
        u[1, :, :] = u[1, :, :] + self.tau*cohesion_force[1, :, :]/rho

        # Computation of ea.velocity
        ea_u = np.dot(self.directions, u.transpose(1, 0, 2))

        # Computation of velocity squared field (npx, npy)
        usqr = u[0]**2 + u[1]**2

        # equilibrium distribution function
        self.feq = np.zeros((self.dim_q, self.np_x, self.np_y))
        for i_dir in range(self.dim_q):
            self.feq[i_dir, :, :] = (
                rho * self.weights[i_dir]
                * (1. + 3. * ea_u[i_dir] + 4.5 * ea_u[i_dir]**2 - 1.5 * usqr)
            )

    def streaming(self):
        """ Streaming via the distribution function.
            Direction specific densities are moved to
            the nearest neighbor lattice nodes.
            see p36
            Periodicity is applied at all the boundaries.
        """
        self.f_tmp = np.zeros((self.dim_q, self.np_x, self.np_y))

        for i_dir in range(self.dim_q):
            # np.roll(a, shift, axis)
            # Roll array elements along a given axis. Elements that roll beyond the last position
            # are re-introduced at the first (ensuring periodicty).
            # shift: The number of places by which elements are shifted. If a tuple, then axis must
            # be a tuple of the same size, and each of the given axes is shifted by the correspond
            # ing number. If an int while axis is a tuple of ints, then the same value is used for
            # all given axes.
            self.f_tmp[i_dir, :, :] = (
                np.roll(
                    np.roll(self.f_n[i_dir, :, :],
                            self.directions[i_dir, 0],
                            axis=0),
                 self.directions[i_dir, 1],
                 axis=1)
            )

    def collision(self):
        """ Perform D2Q9 collision """
        # Collision of the particles everywhere
        self.f_n = self.f_tmp - (self.f_tmp - self.feq) / self.tau

        # Collision with the Solid part
        # Bounceback boundary (see p44)
        for i_dir in range(self.dim_q):
            self.f_n[i_dir, self.obstacle] = (
                self.f_tmp[self.bnd_noslip[i_dir], self.obstacle])

    def xmin_bnd(self, inlet_method="bounceback"):
        """ Initialize the domain
        Initialize rho, u, fi, fi_eq
        """
        type_bc = self.dm.bc_xmin_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            # bounce back
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, 0, :] = (
                    self.f_n[self.bnd_noslip[i_dir], 0, :])
        elif type_bc == "wall_slip":
            # symmetry bounce
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, 0, :] = (
                    self.f_n[self.bnd_slip_y[i_dir], 0, :])
        elif type_bc == "inlet":
            bnd_ux = self.dm.bc_xmin_values["vel_u"]
            self.density[0, :] = (
                (self.f_n[2, 0, :]
                 + self.f_n[0, 0, :]
                 + self.f_n[4, 0, :]
                 + 2. * (self.f_n[6, 0, :]
                         + self.f_n[3, 0, :]
                         + self.f_n[7, 0, :]))
                / (1. - bnd_ux))

            if inlet_method == "non_equil":
                # Non equilibrium extrapolation method
                # p 79 book mohamad
                # p194 book sukop
                self.f_tmp[1, 0, :] = (
                    self.f_n[3, 0, :] + 2. / 3. * self.density[0, :] * bnd_ux)
                self.f_tmp[5, 0, :] = (
                    self.f_n[7, 0, :] + self.feq[5, 0, :] - self.feq[7, 0, :])
                self.f_tmp[8, 0, :] = (
                    self.f_n[6, 0, :] + self.feq[8, 0, :] - self.feq[6, 0, :])
            elif inlet_method == "equil":
                # Equilibrium bc inlet
                # Recompute density and a new equ
                # p191 book sukop
                self.compute_equilibrium_function(
                    self.density,
                    self.init_velocity)
                self.f_tmp[5, 0, :] = self.feq[5, 0, :]
                self.f_tmp[1, 0, :] = self.feq[1, 0, :]
                self.f_tmp[8, 0, :] = self.feq[8, 0, :]
            else:
                # Non equilibrium bounce back (default)
                # Zhu He
                # p77 book Mohamad
                # p198 book Sukop
                self.f_tmp[1, 0, :] = (
                    self.f_n[3, 0, :]
                    + 2. / 3. * self.density[0, :] * bnd_ux)
                self.f_tmp[5, 0, :] = (
                    self.f_n[7, 0, :]
                    + (1. / 6.) * self.density[0, :] * bnd_ux)
                self.f_tmp[8, 0, :] = (
                    self.f_n[6, 0, :]
                    + (1. / 6.) * self.density[0, :] * bnd_ux)
        else:
            raise NotImplementedError("BC type :", type_bc)

    def xmax_bnd(self, outlet_method="extrapolate"):
        type_bc = self.dm.bc_xmax_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, -1, :] = (
                    self.f_n[self.bnd_noslip[i_dir], -1, :])
        elif type_bc == "wall_slip":
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, -1, :] = (
                    self.f_n[self.bnd_slip_y[i_dir], -1, :])
        elif type_bc == "outlet":
            rho_outlet = self.dm.rho
            if outlet_method == "density_imposed":
                # Open imposed density boundary
                # p79 mohamad
                self.velocity[0, -1, :] = (
                    (self.f_n[2, -1, :]
                     + self.f_n[0, -1, :]
                     + self.f_n[4, -1, :]
                     + 2. * (self.f_n[5, -1, :] +
                             self.f_n[1, -1, :] +
                             self.f_n[8, -1, :]))
                    / rho_outlet - 1.)

                rhoux_out = rho_outlet * self.velocity[0, -1, :]
                self.f_tmp[6, -1, :] = self.f_n[8, -1, :] - 1. / 6. * rhoux_out
                self.f_tmp[3, -1, :] = self.f_n[1, -1, :] - 2. / 3. * rhoux_out
                self.f_tmp[7, -1, :] = self.f_n[5, -1, :] - 1. / 6. * rhoux_out
            else:
                # Simple extrapolation at the outlet
                # p79 mohamad
                self.f_tmp[6, -1, :] = (
                    2. * self.f_tmp[6, -2, :] - self.f_tmp[6, -3, :])
                self.f_tmp[3, -1, :] = (
                    2. * self.f_tmp[3, -2, :] - self.f_tmp[3, -3, :])
                self.f_tmp[7, -1, :] = (
                    2. * self.f_tmp[7, -2, :] - self.f_tmp[7, -3, :])
        else:
            raise NotImplementedError("BC type :", type_bc)

    def ymin_bnd(self):
        type_bc = self.dm.bc_ymin_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, :, 0] = (
                    self.f_n[self.bnd_noslip[i_dir], :, 0])
        elif type_bc == "wall_slip":
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, :, 0] = (
                    self.f_n[self.bnd_slip_x[i_dir], :, 0])
        else:
            raise NotImplementedError("BC type :", type_bc)
    
    def ymax_bnd(self):
        type_bc = self.dm.bc_ymax_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, :, -1] = (
                    self.f_n[self.bnd_noslip[i_dir], :, -1])
        elif type_bc == "wall_slip":
            for i_dir in range(self.dim_q):
                self.f_tmp[i_dir, :, -1] = (
                    self.f_n[self.bnd_slip_x[i_dir], :, -1])
        else:
            raise NotImplementedError("BC type :", type_bc)

        return self.f_tmp

# def lbm_filter(velocity, density):
#     # Filtering
#     density = gaussian_filter(density, 0.1)
#     velocity[0, :, :] = gaussian_filter(velocity[0, :, :], 0.5)
#     velocity[1, :, :] = gaussian_filter(velocity[1, :, :], 0.5)



   # def print_infos(self):
   #      """ Print infos """
   #      print("Dim Q = ", self.dim_q)
   #      print("directions = ", self.directions)
   #      print("Weights = ", self.weights)
   #      print("BND no slip:", self.bnd_noslip)
   #      print("Direction & weights & noslip")
   #      for index in range(self.dim_q):
   #          print(
   #              self.directions[index], 
   #              " | ", self.weights[index], 
   #              " | ", self.bnd_noslip[index])


# For convenience of treating the boundary conditions, keep in a table the indicies
# of the dimensions relative to the left, middle and right column (axis y)
# and also the down, middle and up line (axis x)
# self.bnd_i1 = np.zeros(3, dtype=int)  # First column (left bnd)
# self.bnd_i1[0] = 3
# self.bnd_i1[1] = 6
# self.bnd_i1[2] = 7
# self.bnd_i2 = np.zeros(3, dtype=int)  # Second column (middle vertical)
# self.bnd_i2[0] = 0
# self.bnd_i2[1] = 2
# self.bnd_i2[2] = 4
# self.bnd_i3 = np.zeros(3, dtype=int)  # Third column (right bnd)
# self.bnd_i3[0] = 1
# self.bnd_i3[1] = 5
# self.bnd_i3[2] = 8
# self.bnd_j1 = np.zeros(3, dtype=int)  # First line (down bnd)
# self.bnd_j1[0] = 4
# self.bnd_j1[1] = 7
# self.bnd_j1[2] = 8
# self.bnd_j2 = np.zeros(3, dtype=int)  # Second line (middle horizontal)
# self.bnd_j2[0] = 0
# self.bnd_j2[1] = 1
# self.bnd_j2[2] = 3
# self.bnd_j3 = np.zeros(3, dtype=int)  # Third line (up bnd)
# self.bnd_j3[0] = 2
# self.bnd_j3[1] = 5
# self.bnd_j3[2] = 6