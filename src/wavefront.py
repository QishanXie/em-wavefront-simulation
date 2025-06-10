def simulate_wavefront(wavelength, defocus, coma_mag, astig_mag, astig_angle_deg, coma_angle_deg, N=512, qmax=1e9):
    import numpy as np

    astig_angle = np.deg2rad(astig_angle_deg)
    coma_angle = np.deg2rad(coma_angle_deg)

    # Reciprocal space grid
    qx = np.linspace(-qmax, qmax, N)
    qy = np.linspace(-qmax, qmax, N)
    QX, QY = np.meshgrid(qx, qy)

    # Wavefront phase calculation
    chi = (np.pi * wavelength *
           (defocus * (QX**2 + QY**2) +
            astig_mag * ((QX**2 - QY**2) * np.cos(2 * (np.arctan2(QY, QX) - astig_angle))) +
            coma_mag * (QX * np.cos(coma_angle) + QY * np.sin(coma_angle) * (QX**2 + QY**2))))

    return chi