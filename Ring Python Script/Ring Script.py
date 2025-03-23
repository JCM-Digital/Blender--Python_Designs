import bpy
import math


def make_fcurves_linear(obj):
    if obj.animation_data and obj.animation_data.action:
        for fcurve in obj.animation_data.action.fcurves:
            for kp in fcurve.keyframe_points:
                kp.interpolation = 'LINEAR'


def create_ring(index, radius):
    bpy.ops.mesh.primitive_circle_add(vertices=64, radius=radius, location=(0, 0, 0))
    ring_obj = bpy.context.active_object
    ring_obj.name = f"ring_{index}"

    # Convert to curve and add depth
    bpy.ops.object.convert(target="CURVE")
    ring_obj.data.bevel_depth = 0.05
    ring_obj.data.bevel_resolution = 4

    return ring_obj


def animate_ring(ring_obj, start_frame, end_frame, z_rotation_start, y_rotation):
    # Start rotation
    ring_obj.rotation_euler = (
        0,
        math.radians(y_rotation),
        math.radians(z_rotation_start),
    )
    ring_obj.keyframe_insert(data_path="rotation_euler", frame=start_frame)

    # End rotation (360° Z + 360° Y for loop)
    ring_obj.rotation_euler = (
        0,
        math.radians(y_rotation + 360),
        math.radians(z_rotation_start + 360 * 2),
    )
    ring_obj.keyframe_insert(data_path="rotation_euler", frame=end_frame)

    make_fcurves_linear(ring_obj)


def add_camera():
    bpy.ops.object.camera_add(location=(12, -12, 8), rotation=(math.radians(60), 0, math.radians(45)))
    cam = bpy.context.active_object
    bpy.context.scene.camera = cam


def add_light():
    bpy.ops.object.light_add(type='AREA', location=(0, 0, 6))
    light = bpy.context.active_object
    light.data.energy = 1000


def setup_scene():
    # Clean up existing objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 360
    scene.frame_current = 1


def main():
    setup_scene()
    add_camera()
    add_light()
# add or subtract rings here
    num_rings = 50
    radius_step = 0.1
    z_rotation_step = 10
    z_rotation = 0
    y_rotation = 30

    for i in range(num_rings):
        radius = radius_step * i
        ring = create_ring(i, radius)

        animate_ring(
            ring_obj=ring,
            start_frame=1,
            end_frame=361,
            z_rotation_start=z_rotation,
            y_rotation=y_rotation
        )

        z_rotation += z_rotation_step  # progressively offset Z-axis spin

    print("✅ Animated spiral ring loop created.")


if __name__ == "__main__":
    main()
