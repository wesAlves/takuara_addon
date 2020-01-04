import bpy


class Move_tool_Operator(bpy.types.Operator):
    bl_idname = "object.move_tool"
    bl_label = "Move_tool"

    move_x = bpy.props.FloatProperty(name = "Move in X by:")
    move_y = bpy.props.FloatProperty(name = "Move in Y by:")
    move_z = bpy.props.FloatProperty(name = "Move in Z by:")

    def execute(self, context):
        move_board(self.move_x, self.move_y, self.move_z)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def move_board(x, y, z):
    # bpy.ops.transform.translate(value = (x, y, z))
    bpy.context.object.location = (
        (x/1000),
        (y/1000),
        (z/1000)
        )