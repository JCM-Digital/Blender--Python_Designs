# Hexagon Script used for "Raven Flies Out of Hexagonal Cage Animation"by Jorge Montes

import bpy
import math  # Import the math module

# create variables ised in loop
radius_step = 0.1
current_radius = 0.1
number_triangles = 55  # iterations of chosen shape

# rotation steps
z_step = 10

# repeat 50 times
for i in range(number_triangles):
    # Add object to scene
    current_radius = i * + radius_step
    bpy.ops.mesh.primitive_circle_add(vertices=6, radius=current_radius)  # vertice number determines shape

    # Get a reference to the currently active object
    triangle_mesh = bpy.context.active_object

    # Rotate mesh about the x-axis
    degrees = 90

    radians = math.radians(degrees)
    triangle_mesh.rotation_euler[0] = radians

    # Rotate mesh about the x-axis
    degrees = z_step * i
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.z = radians

    # convert mesh into a curve
    bpy.ops.object.convert(target='CURVE')

    # added bevel to curve
    triangle_mesh.data.bevel_depth = 0.03

    triangle_mesh.data.bevel_resolution = 12
    # shade smooth
    bpy.ops.object.shade_smooth()

# Update the scene (this line is sometimes necessary in scripting outside of normal Blender UI operations)
bpy.context.view_layer.update()

