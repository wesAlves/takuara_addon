import bpy


class Positive_Thickness_Operator(bpy.types.Operator):
    bl_idname = "object.positive_thickness"
    bl_label = "Positive Thickness"

    def execute(self, context):
        loc = bpy.context.object
        positiveX = loc.location[0] = (loc.location[0] + 15)
        return {'FINISHED'}

import bpy

class movex(bpy.types.Operator):
    bl_idname = "object.move"
    bl_label = "move"
    
    def execute(self, context):
        loc = bpy.context.object
        locs = loc.location[0] = (loc.location[0]+15)
        return {'FINISHED'}
        
        
'''
class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        layout.label(text=" Simple Row:")
        layout.operator('object.move', text = "btn")

        

def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(movex)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(movex)


if __name__ == "__main__":
    register()
'''