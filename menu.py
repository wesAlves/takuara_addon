import bpy

class Menu_marcenaria_Operator(bpy.types.Header):
    bl_idname = "OBJECT_MT_menu_marcenaria"
    bl_label = "Menu Marcenaria"
    bl_space_type = "VIEW_3D"


    def draw(self, context):
        layout = self.layout

        layout.operator("object.tomillimeters" ,text = "To Milleters" )
        layout.operator("object.add_new_board", text = "Add new board")
        layout.operator("object.delet_all_", text = "Delete all")
        # layout.operator("object.rotate_tool", text = "Rotate board")
        # layout.operator("object.move_tool", text = "Move board")



# class Marcenaria_panel_Operator(bpy.types.Panel):
    # bl_idname = "object.marcenaria_panel"
    # bl_label = "Marcenaria Panel"
    # bl_space_type = "PROPERTIES"
    # bl_region_type = "WINDOW"
    # bl_context = "object"


    # def draw(self, context):
    #     Obj = context.object
        
    #     layout = self.layout
        
    #     row = layout.row()
    #     row.operator("object.tomillimeters", text = "Change to Millimeters")
    #     row.operator("object.add_new_board", text = "Add new board")

class newTool(bpy.types.Panel):
    bl_label = "Marcenaria"
    bl_idname = "OBJECT_PT_marcenaria"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # layout.label(text = "Marcenaria")

        row = layout.row()
        row.operator("object.tomillimeters", text = "Change to Millimeters")
        
        row = layout.row()
        row.operator("object.cut_plan", text = 'Create cut plan')

        row = layout.row()
        row.prop(obj, "name")
        
        row = layout.row()
        row.prop(obj, 'dimensions')

        row = layout.row()
        row.prop(obj, 'rotation_euler')

        row = layout.row()
        row.prop(obj, 'location')



       