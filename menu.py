import bpy


class Menu_marcenaria_Operator(bpy.types.Header):
    bl_idname = "OBJECT_MT_menu_marcenaria"
    bl_label = "Menu Marcenaria"
    bl_space_type = "VIEW_3D"

    def draw(self, context):
        layout = self.layout

        # layout.operator("object.tomillimeters", text="To Milleters")
        # layout.operator("object.create_limits", text = "Create a base")
        # layout.operator("object.side_column", text="Add new side")
        # layout.operator("object.front_column", text = "Add new Front")
        # layout.operator("object.line_board", text = "Line")
        # layout.operator("object.delet_all_", text="Delete all")
        
        layout.operator("object.adj_width", text="Shirink X")

        

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
        layout.label (text = "Board name") 
        row.prop(obj, "name")
        
        row = layout.row()
        layout.label (text = "Dimensions") 
        row.prop(obj, 'dimensions')

        # row = layout.row()
        # row.operator("object.thickness_06", text = "Thickness 06")
        # row.operator("object.thickness_15", text = "Thickness 15")
        # row.operator("object.thickness_18", text = "Thickness 18")



        row = layout.row()
        layout.label (text = "Set thickness") 
        row.operator("object.thickness_06", text = "Thickness 06")
        row.operator("object.thickness_15", text = "Thickness 15")
        row.operator("object.thickness_18", text = "Thickness 18")

        row = layout.row()
        layout.label (text = "Rotation") 
        row.operator("object.rotate_x", text = "Rotate X")
        row.operator("object.rotate_y", text = "Rotate Y")
        row.operator("object.rotate_z", text = "Rotate Reset")

        row = layout.row()
        row.prop(obj, 'rotation_euler', text = "Rotation")

        row = layout.row()
        row.prop(obj, 'location')

        layout.label (text = "Move Thickness") 
        row = layout.row()
        row.operator('object.move_negative_x', text = '- Front')
        row.operator('object.move_positive_x', text = '+ Front')

        row = layout.row()
        row.operator('object.move_negative_y', text = '\- Side')
        row.operator('object.move_positive_y', text = '\+ Side')

        row = layout.row()
        row.operator('object.move_negative_z', text = '\- Hight')
        row.operator('object.move_positive_z', text = '\+ Hight')

        row = layout.row()
        row.operator('object.move_to_origin', text = 'To Origin')

        row = layout.row()
        layout.label (text = "Make a cut plan") 
        row.operator("object.cut_plan", text = 'Create cut plan')

        row = layout.row()
        layout.label (text = "Change units") 
        row.operator("object.tomillimeters", text = "Change to Millimeters")