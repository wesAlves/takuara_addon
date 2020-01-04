import bpy

class Rotate_tool_Operator(bpy.types.Operator):
    bl_idname = "object.rotate_tool"
    bl_label = "Rotate_tool"

    def execute(self, context):
        # bpy.ops.transform.rotate(value = (0, (-90/360)*(2*3.14)), 0))
        bpy.context.object.rotation_euler = (0, ((-90/360)*(2*3.14)), 0)
        return {'FINISHED'}
