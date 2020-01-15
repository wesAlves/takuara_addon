import bpy
import mathutils
from math import pi

class Side_column_Operator(bpy.types.Operator):
    bl_idname = "object.side_column"
    bl_label = "Side_column"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")

    def execute(self, context):
        get_locators()
        Add_board("side_board", get_locators()[2].location[2], get_locators()[3].location[1])
        rotate_fit(0, 90)
        return {'FINISHED'}


class Front_column_Operator(bpy.types.Operator):
    bl_idname = "object.front_column"
    bl_label = "Front_column"

    def execute(self, context):
        get_locators()
        Add_board("side_board", get_locators()[1].location[0], get_locators()[2].location[2])
        rotate_fit(90, 0)
        return {'FINISHED'}


class Line_board_Operator(bpy.types.Operator):
    bl_idname = "object.line_board"
    bl_label = "Line_board"

    def execute(self, context):
        get_locators()
        Add_board("side_board", get_locators()[1].location[0], get_locators()[3].location[1])
        return {'FINISHED'}


def Add_board(name, x, y):
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.object.name = name
    bpy.context.object.dimensions = (
        ((x)),
        ((y)),
        ((15)/1000)
    )
    bpy.context.object.location = (
        (bpy.context.object.scale[0]),
        (bpy.context.object.scale[1]),
        (bpy.context.object.scale[2])
        )
    bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)

def get_locators():
    origin = bpy.data.objects['Origin_(0.0, 0.0, 0.0)']
    width = bpy.data.objects['width']
    depth = bpy.data.objects['depth']
    height = bpy.data.objects['height']
    return(origin, width, height, depth)

def rotate_fit(front, side):
    bpy.context.object.rotation_euler = (
        ((front/360)*(2*pi)),
        ((-side/360)*(2*pi)),
        0
    )