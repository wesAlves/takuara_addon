import bpy
 

class ToMillimeters_Operator(bpy.types.Operator):
    bl_idname = "object.tomillimeters"
    bl_label = "To Millimeters"

    def execute(self, context):
        bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
        return {'FINISHED'}