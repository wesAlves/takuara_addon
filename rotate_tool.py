import bpy
import mathutils
from math import pi


class Rotate_tool_Operator(bpy.types.Operator):
    bl_idname = "object.rotate_tool"
    bl_label = "Rotate_tool"

    rotate_x = bpy.props.FloatProperty(name = 'Rotate in X by:')
    rotate_y = bpy.props.FloatProperty(name = 'Rotate in Y by:')
    rotate_z = bpy.props.FloatProperty(name = 'Rotate in Z by:')



    def execute(self, context):
        # bpy.context.object.rotation_euler = (0, ((-90/360)*(2*3.14)), 0)
        rotate_board(self.rotate_x, self.rotate_y, self.rotate_z)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)



class Rotate_Col_Operator(bpy.types.Operator):
    bl_idname = "object.rotate_col"
    bl_label = "rotate-col"

    def execute(self, context):
        rotate_by_button(90, 0)
        return {'FINISHED'}

class Rotate_Frot_Rear_Operator(bpy.types.Operator):
    bl_idname = "object.rotate_frot_rear"
    bl_label = "Rotate_frot_rear"

    def execute(self, context):
        rotate_by_button(90, 90)
        return {'FINISHED'}


def rotate_board(x, y, z):
    bpy.context.object.rotation_euler = (
        ((x/360)*(2*pi)),
        ((y/360)*(2*pi)*(-1)),
        ((z/360)*(2*pi))
    )

def rotate_by_button(column, fronRear):
    bpy.context.object.rotation_euler = (
        0,
        ((-column/360)*(2*pi)),
        ((fronRear/360)*(2*pi))
    )

# def rotate_to_front_rear():
#     bpy.object.rotation_euler = (
#         0,
#         ((-90)*(2*pi)),
#         ((90)*(2*pi)),
#     )