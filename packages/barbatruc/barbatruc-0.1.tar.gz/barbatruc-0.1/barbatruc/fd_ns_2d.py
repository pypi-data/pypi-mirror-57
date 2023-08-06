"""Module to solve 2D Naviers stokes equations.

The interactive module 12 steps to Navier-Stokes is one of several
components of the Computational Fluid Dynamics class taught by Professor
Lorena Barba in Boston university between 2009 and 2013.

The following code is started from step12 see
https://nbviewer.jupyter.org/github/barbagroup/CFDPython/tree/master/lessons/
for futher reading

Dom here after isthe FluidDomain object of barbatruc
"""

import numpy as np
from barbatruc.fd_operators import (grad_2, scnd_der_2)


PP_INFO = 100
CFL_MAX = 0.699
FOU_MAX = 0.099
SMALL = 1e-6

__all__ = ["NS_fd_2D_explicit"]


class NS_fd_2D_explicit():

    def __init__(self, dom, max_vel=None, verbose=False, obs_ib_factor=0.):

        self.dom = dom
        if max_vel is None:
            self.max_vel = max(np.max(np.hypot(
                self.dom.fields["vel_u"],
                self.dom.fields["vel_v"])), 1.e-8)
        else:
            self.max_vel = max_vel
        self.verbose = verbose
        self.periox, self.perioy = dom.perio_xy()
        print(self.periox, self.perioy)
        self.obst_x = np.zeros(self.dom.shape)
        self.obst_y = np.zeros(self.dom.shape)
        self.obs_ib_factor = obs_ib_factor

    def mini_delta_t(self):
        """ Define the mai iteration of the temporal loop.
        """
        delta_t_cfl = CFL_MAX*self.dom.delta_x/self.max_vel
        delta_t_fou = FOU_MAX/self.dom.nu_*self.dom.delta_x**2
        delta_t = min(delta_t_cfl, delta_t_fou)
        return delta_t

    def iteration(self, time, time_step):
        """Major iteration."""
        delta_t = self.mini_delta_t()

        t_end = time + time_step
        iteration = 0
        if time + delta_t > t_end:
            if self.verbose:
                print(".  Single iteration")
            delta_t = time_step
            self.sub_iteration(time, delta_t)
            time += delta_t
        else:
            while time + delta_t < t_end:
                self.sub_iteration(time, delta_t)
                time += delta_t
                iteration += 1
                if self.verbose and iteration % PP_INFO == 0:
                    print(".   - t [s] =" + str(time))
                    print(".   max_vel:"
                          + str(np.max(self.dom.fields["vel_u"])))
            if time + delta_t > t_end:
                delta_t = t_end-time
                if self.verbose:
                    print(".   Final partial iteration")
                self.sub_iteration(time, delta_t)
                time += delta_t

    def sub_iteration(self, time, delta_t):
        """Sub iteration of Naviers stokes."""
        fields_new = dict()
        grad_x, grad_y, ggrad_x, ggrad_y = self.compute_derivatives()

        # compute pressure term
        fields_new["press"] = self.pressure_poisson(delta_t)

        if self.obs_ib_factor > 0:
            self.obst_x += (
                - self.obs_ib_factor*self.dom.obstacle*self.dom.fields["vel_u"])
            self.obst_y += (
                - self.obs_ib_factor*self.dom.obstacle*self.dom.fields["vel_v"])

        field = "vel_u"
        fields_new[field] = self.dom.fields[field] + delta_t * (
            - (self.dom.fields["vel_u"] * grad_x[field]
               + self.dom.fields["vel_v"] * grad_y[field])
            - grad_x["press"] / (2. * self.dom.rho)
            + self.obst_x
            + self.dom.nu_ * (ggrad_x[field] + ggrad_y[field])
        )
        field = "vel_v"
        fields_new[field] = self.dom.fields[field] + delta_t * (
            - (self.dom.fields["vel_u"] * grad_x[field]
               + self.dom.fields["vel_v"] * grad_y[field])
            - grad_y["press"] / (2. * self.dom.rho)
            + self.obst_y
            + self.dom.nu_ * (ggrad_x[field] + ggrad_y[field])
        )
        field = "scal"
        fields_new[field] = self.dom.fields[field] + delta_t * (
            - (self.dom.fields["vel_u"] * grad_x[field]
               + self.dom.fields["vel_v"] * grad_y[field])
            + self.dom.source["scal"]
            + self.dom.nu_ * (ggrad_x[field] + ggrad_y[field])
        )

        self.dom.fields = fields_new
        self.xmin_bnd()
        self.xmax_bnd()
        self.ymin_bnd()
        self.ymax_bnd()

        if self.obs_ib_factor == 0:
            for field in ["vel_u", "vel_v"]:
                self.dom.fields[field] = (
                    self.dom.nullify_on_obstacle(self.dom.fields[field]))
        
    def compute_derivatives(self):
        """Compute the derivatives of fields."""
        grad_x = dict()
        grad_y = dict()
        ggrad_x = dict()
        ggrad_y = dict()

        for field in ["vel_u", "vel_v", "scal", "press"]:
            grad_x[field], grad_y[field] = grad_2(
                self.dom.fields[field],
                self.dom.delta_x,
                periox=self.periox,
                perioy=self.perioy
                )
            ggrad_x[field], ggrad_y[field] = scnd_der_2(
                self.dom.fields[field],
                self.dom.delta_x,
                periox=self.periox,
                perioy=self.perioy)

        return grad_x, grad_y, ggrad_x, ggrad_y

    def xmin_bnd(self):
        type_bc = self.dom.bc_xmin_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            self.dom.fields["vel_u"][:, 0] = 0.
            self.dom.fields["vel_v"][:, 0] = 0.
        elif type_bc == "wall_slip":
            self.dom.fields["vel_u"][:, 0] = 0.
        elif type_bc == "inlet":
            bnd_ux = self.dom.bc_xmin_values["vel_u"]
            self.dom.fields["vel_u"][:, 0] = bnd_ux
            self.dom.fields["vel_v"][:, 0] = 0.
        else:
            raise NotImplementedError("BC type :", type_bc)

    def xmax_bnd(self):
        type_bc = self.dom.bc_xmax_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            self.dom.fields["vel_u"][:, -1] = 0.
            self.dom.fields["vel_v"][:, -1] = 0.
        elif type_bc == "wall_slip":
            self.dom.fields["vel_u"][:, -1] = 0.
        elif type_bc == "outlet":
            pass  # Nothing to do
        else:
            raise NotImplementedError("BC type :", type_bc)

    def ymin_bnd(self):
        type_bc = self.dom.bc_ymin_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            self.dom.fields["vel_u"][0, :] = 0.
            self.dom.fields["vel_v"][0, :] = 0.
        elif type_bc == "wall_slip":
            self.dom.fields["vel_v"][0, :] = 0.
        else:
            raise NotImplementedError("BC type :", type_bc)

    def ymax_bnd(self):
        type_bc = self.dom.bc_ymax_type
        if type_bc == "periodic":
            pass  # Nothing to do
        elif type_bc == "wall_noslip":
            self.dom.fields["vel_u"][-1, :] = 0.
            self.dom.fields["vel_v"][-1, :] = 0.
        elif type_bc == "wall_slip":
            self.dom.fields["vel_v"][-1, :] = 0.
        elif type_bc == "moving_wall":
            bnd_uy = self.dom.bc_ymax_values["vel_u"]
            self.dom.fields["vel_u"][-1, :] = bnd_uy
            self.dom.fields["vel_v"][-1, :] = 0
        else:
            raise NotImplementedError("BC type :", type_bc)

    def pressure_poisson(self, delta_t):
        """Define Pressure Poisson iterative function.

        here ggrad_p_x and ggrad_p_y are terms coming
        from the pressure laplacian
        u_term is the pressure term coming from div_u
        """
        b_press = self.press_from_div_u(delta_t)
        eps_old = 1.
        press = self.dom.fields["press"].copy()
        norm_ref = max(np.linalg.norm(press), SMALL)
        for _ in range(40):
            p_old = press.copy()
            ggrad_p_x, ggrad_p_y = scnd_der_2(
                p_old,
                self.dom.delta_x,
                periox=self.periox,
                perioy=self.perioy,
                no_center=True)
            press = (
                (ggrad_p_x + ggrad_p_y - b_press) * self.dom.delta_x**2 / 4.0
            )
            eps = np.linalg.norm(press-p_old)/norm_ref
            if eps < 1e-3:
                break
            if eps_old > eps:
                break
            eps_old = eps
        press -= press.mean()
        return press

    def press_from_div_u(self, delta_t):
        """Compute the presure term from velocity divengence."""
        b_press = np.zeros(self.dom.shape)
        gux, guy = grad_2(
            self.dom.fields["vel_u"],
            self.dom.delta_x,
            periox=self.periox,
            perioy=self.perioy)
        gvx, gvy = grad_2(
            self.dom.fields["vel_v"],
            self.dom.delta_x,
            periox=self.periox,
            perioy=self.perioy)
        b_press = self.dom.rho * (
            (gux + gvy)/delta_t - (gux**2 + 2.0*guy*gvx + gvy**2)
        )
        return b_press
