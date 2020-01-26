import bpy
import mathutils
from math import pi

class Side_M_column_Operator(bpy.types.Operator):
    bl_idname = "object.column_side"
    bl_label = "Right column"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")

    def execute(self, context):
        get_locators()
        Add_board("Right_board", get_locators()[3].location[1], get_locators()[2].location[2])
        rotate_fit(90, 90)
        move_fit(get_locators()[1].location[0]/2, 0, 0)
        return {'FINISHED'}

class Side_R_column_Operator(bpy.types.Operator):
    bl_idname = "object.column_right"
    bl_label = "Right column"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")

    def execute(self, context):
        get_locators()
        Add_board("Right_board", get_locators()[3].location[1], get_locators()[2].location[2])
        rotate_fit(90, 90)
        move_fit(get_locators()[1].location[0]-(15/1000), 0, 0)
        return {'FINISHED'}


class Side_L_column_Operator(bpy.types.Operator):
    bl_idname = "object.column_left"
    bl_label = "Left column"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")

    def execute(self, context):
        get_locators()
        Add_board("Left_board", get_locators()[3].location[1], get_locators()[2].location[2])
        rotate_fit(90, 90)
        return {'FINISHED'}


class FB_M_column_Operator(bpy.types.Operator):
    bl_idname = "object.fb_column"
    bl_label = "Front_column"

    def execute(self, context):
        get_locators()
        Add_board("Front_board", get_locators()[1].location[0], get_locators()[2].location[2])
        rotate_fit(90, 0)
        move_fit(0, get_locators()[3].location[1]/2, 0)
        return {'FINISHED'}

class Front_column_Operator(bpy.types.Operator):
    bl_idname = "object.front_column"
    bl_label = "Front_column"

    def execute(self, context):
        get_locators()
        Add_board("Front_board", get_locators()[1].location[0], get_locators()[2].location[2])
        rotate_fit(90, 0)
        move_fit(0, 15/1000, 0)
        return {'FINISHED'}

class Back_column_Operator(bpy.types.Operator):
    bl_idname = "object.back_column"
    bl_label = "Front_column"

    def execute(self, context):
        get_locators()
        Add_board("Back_board", get_locators()[1].location[0], get_locators()[2].location[2])
        rotate_fit(90, 0)
        move_fit(0, get_locators()[3].location[1], 0)
        return {'FINISHED'}


class Line_board_Operator(bpy.types.Operator):
    bl_idname = "object.line_board"
    bl_label = "Line_board"

    def execute(self, context):
        get_locators()
        Add_board("Line_board", get_locators()[1].location[0], get_locators()[3].location[1])
        move_fit(0, 0, get_locators()[2].location[2]/2)
        return {'FINISHED'}

class Bottom_board_Operator(bpy.types.Operator):
    bl_idname = "object.bottom_board"
    bl_label = "Bottom_board"

    def execute(self, context):
        get_locators()
        Add_board("Bottom_board", get_locators()[1].location[0], get_locators()[3].location[1])
        return {'FINISHED'}

class Top_board_Operator(bpy.types.Operator):
    bl_idname = "object.top_board"
    bl_label = "Top_board"

    def execute(self, context):
        get_locators()
        Add_board("Top_board", get_locators()[1].location[0], get_locators()[3].location[1])
        move_fit(0, 0, get_locators()[2].location[2]-(15/1000))
        return {'FINISHED'}


def Add_board(name, width, height):
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.object.name = name
    bpy.context.object.dimensions = (
        ((width)),
        ((height)),
        ((15)/1000)
    )
    bpy.context.object.location = (
        (bpy.context.object.scale[0]),
        (bpy.context.object.scale[1]),
        (bpy.context.object.scale[2])
        )
    bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)

def get_locators():
    origin = bpy.data.objects['Origin_(0.0, 0.0, 0.0)'] #TODO FIX THE ORIGIN NAME AND GET
    width = bpy.data.objects['width']
    depth = bpy.data.objects['depth']
    height = bpy.data.objects['height']
    return(origin, width, height, depth)

def move_fit(right, back, top):
        bpy.context.object.location=(
            right,
            back,
            top
        )


def rotate_fit(front, side):
    bpy.context.object.rotation_euler = (
        ((front/360)*(2*pi)),
        0,
        ((side/360)*(2*pi))
    )