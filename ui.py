import bpy



class Main_Controls_PT_panel(bpy.types.Panel):
    bl_label = "Main controls"
    bl_region_type = 'UI'
    bl_space_type = "VIEW_3D"
    bl_category = "Marcenaria"
    
    def draw(self, context):
        layout = self.layout
        # obj = context.object

        layout.operator("object.delet_all_", text="Delete all")
        layout.operator("object.create_limits", text = "Create a base")

class Creation_Controls_PT_panel(bpy.types.Panel):
    bl_label = "Creation controls"
    bl_region_type = 'UI'
    bl_space_type = "VIEW_3D"
    bl_category = "Marcenaria"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.label (text = "Board Left/Right") 
        layout.operator("object.column_left", text="Add new Left")
        layout.operator("object.column_right", text="Add Right")
        layout.operator("object.column_side", text="Middle")
        
        layout.label (text = "Board Front/Back") 
        layout.operator("object.front_column", text = "Add new Front")
        layout.operator("object.back_column", text = "Add new Back")
        layout.operator("object.fb_column", text = "Middle")
        
        layout.label (text = "Board Top/Bottom") 
        layout.operator("object.top_board", text = "Top")
        layout.operator("object.bottom_board", text = "Bottom")
        layout.operator("object.line_board", text = "Middle")



class Adjusts_Controls_PT_panel(bpy.types.Panel):
    bl_label = "Adjusts"
    bl_region_type = 'UI'
    bl_space_type = "VIEW_3D"
    bl_category = "Marcenaria"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object


        layout.prop(obj, "name")
        layout.prop(obj, 'dimensions')

        layout.label (text = "Shrink") 
        
        layout.operator("object.shrink_width", text = "Shrink Width")
        layout.operator("object.shrink_height", text = "Shrink Height")
        layout.label (text = "Expand") 
        
        layout.operator("object.expand_width", text = "Expand  Width")
        layout.operator("object.expand_height", text = "Expand Height")

        layout.label (text = "Set thickness") 
        
        layout.operator("object.thickness_06", text = "Thickness 06")
        layout.operator("object.thickness_15", text = "Thickness 15")
        layout.operator("object.thickness_18", text = "Thickness 18")

        layout.label (text = "Rotation") 
        
        layout.operator("object.rotate_x", text = "Rotate X")
        layout.operator("object.rotate_y", text = "Rotate Y")
        layout.operator("object.rotate_z", text = "Rotate Reset")

        
        layout.prop(obj, 'rotation_euler', text = "Rotation")

        
        layout.prop(obj, 'location')

        layout.label (text = "Move Thickness") 
        
        layout.operator('object.move_negative_x', text = '- Front')
        layout.operator('object.move_positive_x', text = '+ Front')

        
        layout.operator('object.move_negative_y', text = '\- Side')
        layout.operator('object.move_positive_y', text = '\+ Side')

        
        layout.operator('object.move_negative_z', text = '\- Height')
        layout.operator('object.move_positive_z', text = '\+ Height')

        
        layout.operator('object.move_to_origin', text = 'To Origin')

        layout.label (text = "Make a cut plan") 
        

class Cut_Plane_PT_panel(bpy.types.Panel):
    bl_label = "Cut Plan"
    bl_region_type = 'UI'
    bl_space_type = "VIEW_3D"
    bl_category = "Marcenaria"
    
    def draw(self, context):
        layout = self.layout

        layout.operator("object.cut_plan", text = 'Create cut plan')
    

class Render_Controls_PT_panel(bpy.types.Panel):
    bl_label = "Render"
    bl_region_type = 'UI'
    bl_space_type = "VIEW_3D"
    bl_category = "Marcenaria"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.label(text = "Render")
        layout.operator("object.render_studio", text="Open Studio Scene")
        layout.operator("object.attach", text="Attach to render")
