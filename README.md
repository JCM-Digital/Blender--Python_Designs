# Hexagon Script for Blender

<p align="center">
  <a href="https://youtu.be/kbFGsYS4JtE">
    <img src="https://img.youtube.com/vi/kbFGsYS4JtE/hqdefault.jpg" alt="Watch the video">
  </a>
</p>

## Overview
This script, designed for use with Blender, animates a "Raven Flies Out of Hexagonal Cage" scenario, authored by Jorge Montes. It programmatically generates a series of hexagonal rings that increase in size, rotate, and then are converted into curved meshes to form a dynamic animation sequence.
## Python Script

## Python Script

The Python script used in this project is available in the `scripts` folder. Access it here: [Python Scripts Folder][(https://github.com/johndoe/animation-project/tree/main/scripts)
](https://github.com/JCM-Digital/Blender--Python_Designs/tree/main/Hexagon%20Python%20Script)

![Hexagonal Cage III](https://github.com/user-attachments/assets/3e9fab78-44af-46cf-964a-3a5226412794)

## Features
- **Dynamic Hexagon Creation**: Automatically generates hexagons with increasing radii.
- **Rotation Animation**: Each hexagon is rotated both on its local X-axis and around the Z-axis to create a spiraling effect.
- **Mesh to Curve Conversion**: Converts the hexagon mesh to a curve to facilitate further manipulation.
- **Beveling**: Applies a bevel to the curves to enhance the visual depth and smoothness.

![Hexagonal Cage IV](https://github.com/user-attachments/assets/dbd52efa-0704-403c-8e84-48a056cd6738)

## Usage
To run this script:
1. Open Blender.
2. Load the script in the Blender text editor.
3. Run the script by pressing `Run Script`.

![Hexagonal Cage V](https://github.com/user-attachments/assets/3b8a084c-2e76-4291-bf9e-f5b8c7868d9e)

## Code Breakdown
- **Variables Initialization**: Sets up the initial parameters like `radius_step`, `current_radius`, and `number_triangles`.
- **Main Loop**:
  - Each iteration creates a hexagon with an increasing radius.
  - Applies rotations in degrees converted to radians for precise angular control.
  - Converts the mesh to a curve and applies bevel properties for aesthetic enhancement.
- **Scene Update**: Ensures the view layer is updated to reflect changes made by the script.

![Hexagonal Cage VI](https://github.com/user-attachments/assets/79a0b717-62e7-42f2-b9c4-3ccbf5cd3701)

## Dependencies
This script requires Blender to be installed with the `bpy` module available for scripting.

![RAVEN_FLIGHT0708 copy](https://github.com/user-attachments/assets/48cf27db-dfa0-46ad-a28e-921513140b22)

## Author
Jorge Montes
