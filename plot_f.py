import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def plot_velocity_distribution(fname):
    Ngamma = 3
    Nv = 100
    v_list = np.linspace(0,800,Nv)

    _gammas, _vs, _fs, _fs_full = np.loadtxt(fname, unpack=True)

    gamma_grid = np.reshape(_gammas, (Ngamma, Nv))
    v_grid = np.reshape(_vs, (Ngamma, Nv))
    f_grid = np.reshape(_fs, (Ngamma, Nv))
    f_full_grid = np.reshape(_fs_full, (Ngamma, Nv))

    colmap = matplotlib.cm.get_cmap('turbo_r')

    for i in range(Ngamma):
        plt.plot(v_grid[i,:],f_grid[i,:]+f_full_grid[i,:], color=colmap(i/(Ngamma-1)))


    plt.show()



plot_velocity_distribution("results/veldists/f_hm_MOD_mx1.0000MeV_lsig-33.00.txt")
plot_velocity_distribution("results/veldists/f_ulm_MOD_mx1.0000MeV_lsig-33.00.txt")
