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


def rotate_board(x, y, z):
    bpy.context.object.rotation_euler = (
        ((x/360)*(2*pi)),
        ((y/360)*(2*pi)*(-1)),
        ((z/360)*(2*pi))
    )