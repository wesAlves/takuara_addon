import bpy


class Delet_all_Operator(bpy.types.Operator):
    bl_idname = "object.delet_all_"
    bl_label = "Delet_all_"

    def execute(self, context):
        bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}
