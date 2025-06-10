# Entry point for the electron microscope wavefront simulation

import numpy as np
import matplotlib.pyplot as plt
from wavefront import simulate_wavefront
from parameters import wavelength, defocus, coma_mag, astig_mag, astig_angle_deg

def main():
    # Set up parameters for the simulation
    defocus_values = [1000e-9, 500e-9]  # Example defocus values in meters
    coma_values = [0, coma_mag]          # Example coma values in meters

    for defocus in defocus_values:
        for coma in coma_values:
            # Simulate the wavefront
            wavefront_phase = simulate_wavefront(wavelength, defocus, coma, astig_mag, astig_angle_deg)

            # Plot the wavefront
            plt.figure(figsize=(6, 5))
            plt.imshow(wavefront_phase, extent=[-1e9, 1e9, -1e9, 1e9], cmap='twilight', origin='lower')
            plt.colorbar(label='Wavefront Phase (radians)')
            plt.xlabel('qx (1/nm)')
            plt.ylabel('qy (1/nm)')
            plt.title(f'Wavefront Phase with Defocus: {defocus*1e9:.1f} nm, Coma: {coma*1e9:.1f} nm')
            plt.tight_layout()
            plt.show()

if __name__ == "__main__":
    main()