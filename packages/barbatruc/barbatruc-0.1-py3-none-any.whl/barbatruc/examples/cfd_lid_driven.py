"""Example on how to solve a pollution problem with the navier stokes solver"""

import numpy as np

from barbatruc.fluid_domain import DomainRectFluid
from barbatruc.fd_ns_2d import NS_fd_2D_explicit
from barbatruc.lattice import Lattice

__all__ = ["cfd_lid_driven"]


def cfd_lid_driven(nsave, t_end):
    """Startup computation
    solve a lid_driven_cavity  problem
    """
    dom = DomainRectFluid(dimx=0.82, dimy=0.61, delta_x=0.02)
    vel = 0.0001
    dom.switch_bc_xmin_wall_noslip()
    dom.switch_bc_xmax_wall_noslip()
    #dom.switch_bc_xmax_outlet()
    dom.switch_bc_ymax_moving_wall(vel_u=vel)
    dom.switch_bc_ymin_wall_noslip()
    
    time = 0.0
    time_step = t_end/nsave

    #solver = Lattice(dom, max_vel=2*vel)
    solver = NS_fd_2D_explicit(dom, obs_ib_factor=0.9)
    for i in range(nsave):
        time += time_step
        solver.iteration(time, time_step)
        print('  Max u:', np.max(dom.fields["vel_u"]))
        print('  Time :', time)
        print('  Iteration %d' % (i))

    dom.show_fields()
    dom.show_flow()

    print('Normal end of execution.')


if __name__ == "__main__":
    cfd_lid_driven(10, 0.50)
