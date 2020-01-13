import bpy
import mathutils
from math import pi


class Side_columns_Operator(bpy.types.Operator):
    bl_idname = "object.side_columns"
    bl_label = "side_columns"

    width = bpy.props.FloatProperty(name = "Width")
    height = bpy.props.FloatProperty(name = "Height")

    def execute(self, context):
        Add_board("side_", self.height, self.width, 15)
        rotate_by_button(0, 90)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)



class FrontRear_columns_Operator(bpy.types.Operator):
    bl_idname = "object.front_rear_columns"
    bl_label = "Front-Rear_columns"

    width = bpy.props.FloatProperty(name = "Width")
    height = bpy.props.FloatProperty(name = "Height")

    def execute(self, context):
        Add_board("front_", self.width, self.height, 15)
        rotate_by_button(90, 0)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Top_Bottom_Operator(bpy.types.Operator):
    bl_idname = "object.top_bottom"
    bl_label = "Top_Bottom"

    width = bpy.props.FloatProperty(name = "Front")
    depth = bpy.props.FloatProperty(name = "Side")

    def execute(self, context):
        Add_board("front_", self.width, self.depth, 15)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)



def Add_board(name, x, y, z):
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.object.name = name
    bpy.context.object.scale = (
        ((x/2)/1000),
        ((y/2)/1000),
        ((z/2)/1000)
    )
    bpy.context.object.location = (
        ((x/2)/1000),
        ((y/2)/1000),
        ((z/2)/1000)
        )
    bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)

def rotate_by_button(rx, ry):
    bpy.context.object.rotation_euler = (
        ((rx/360)*(2*pi)),
        ((ry/360)*(2*pi)*(-1)),
        0
    )
    # bpy.context.object.location = (
    #     (bpy.context.object.location[0]+((rx/1000)/6)),
    #     (bpy.context.object.location[1]+((ry/1000)/6)),
    #     (bpy.context.object.location[2])
    #     )
    # bpy.ops.object.transform_apply(location = True)