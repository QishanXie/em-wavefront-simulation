def plot_wavefront(wavefront_data, qmax, title='Wavefront Phase', xlabel='qx (1/nm)', ylabel='qy (1/nm)'):
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 5))
    plt.imshow(wavefront_data, extent=[-qmax*1e-9, qmax*1e-9, -qmax*1e-9, qmax*1e-9], cmap='twilight', origin='lower')
    plt.colorbar(label='Wavefront phase χ (radians)')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()