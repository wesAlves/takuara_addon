import bpy

class Menu_marcenaria_Operator(bpy.types.Header):
    bl_idname = "OBJECT_MT_menu_marcenaria"
    bl_label = "Menu Marcenaria"
    bl_space_type = "VIEW_3D"


    def draw(self, context):
        layout = self.layout
   
        layout.operator("object.add_new_board", text = "Add new board")


        
