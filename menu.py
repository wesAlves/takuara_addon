import bpy


class Menu_marcenaria_Operator(bpy.types.Header):
    bl_idname = "OBJECT_MT_menu_marcenaria"
    bl_label = "Menu Marcenaria"
    bl_space_type = "VIEW_3D"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.tomillimeters", text="To Milleters")
        # layout.operator("object.add_new_board", text="Add new board")
        # layout.operator("object.side_columns", text = "Add new side")
        # layout.operator("object.front_rear_columns", text = "Add new Front/Rear")
        # layout.operator("object.delet_all_", text="Delete all")
        layout.operator("object.create_limits", text = "Create a base")
        layout.operator("object.top_bottom", text = "Top/Bottom")
        layout.operator("object.side_columns", text = "Left/Right")
        layout.operator("object.front_rear_columns", text = "Front/Rear")
        layout.operator("object.delet_all_", text="Delete all")
        
        

class new_Tool(bpy.types.Panel):
    bl_label = "Marcenaria"
    bl_idname = "OBJECT_PT_marcenaria"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.operator("object.tomillimeters", text = "Change to Millimeters")
        
        row = layout.row()
        row.operator("object.cut_plan", text = 'Create cut plan')

        row = layout.row()
        row.prop(obj, "name")
        
        row = layout.row()
        row.prop(obj, 'dimensions')

        row = layout.row()
        row.operator("object.thickness_06", text = "Thickness 06")
        row.operator("object.thickness_15", text = "Thickness 15")
        row.operator("object.thickness_18", text = "Thickness 18")

        row = layout.row()
        row.operator("object.rotate_x", text = "Rotate X")
        row.operator("object.rotate_y", text = "Rotate Y")
        row.operator("object.rotate_z", text = "Rotate Reset")

        # row = layout.row()
        # row.operator("object.create_limits", text = "Create a base")


        row = layout.row()
        row.prop(obj, 'rotation_euler', text = "Rotation")

        row = layout.row()
        row.prop(obj, 'location')



       
