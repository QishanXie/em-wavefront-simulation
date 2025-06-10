# EM Wavefront Simulation

This project simulates the wavefront in an electron microscope considering defocus, coma, and astigmatism. The simulation computes the wavefront phase and visualizes the results using various parameters.

## Overview

The simulation aims to provide insights into how defocus, coma, and astigmatism affect the wavefront in electron microscopy. By adjusting these parameters, users can observe the resulting changes in the wavefront phase.

## Project Structure

- `src/`: Contains the source code for the simulation.
  - `__init__.py`: Marks the directory as a Python package.
  - `main.py`: Entry point for the simulation.
  - `wavefront.py`: Core functionality for simulating the wavefront.
  - `parameters.py`: Defines constants and parameters used in the simulation.
  - `plot_utils.py`: Utility functions for plotting the results.

- `requirements.txt`: Lists the dependencies required for the project.

## How to Run the Simulation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
4. Run the simulation by executing the main script:
   ```
   python src/main.py
   ```

## Parameters

- **Wavelength**: The wavelength of the electrons used in the simulation (in meters).
- **Defocus**: The amount of defocus applied (in meters).
- **Coma Amplitude**: The amplitude of the coma aberration (in meters).
- **Astigmatism Parameters**: Parameters defining the astigmatism effect.

Adjust these parameters in `parameters.py` to explore different simulation scenarios.