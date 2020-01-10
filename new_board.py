import bpy

class Add_new_board_Operator(bpy.types.Operator):
    bl_idname = "object.add_new_board"
    bl_label = "Add_new_board"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")
    # scale = bpy.props.FloatVectorProperty( name = "Board size", default = (1.0, 1.0, 0.0075))
    scale_x = bpy.props.FloatProperty(name = "Board size in X")
    scale_y = bpy.props.FloatProperty(name = "Board size in Y")
    scale_z = bpy.props.FloatProperty(name = "Board size in Z", default = 15)


    def execute(self, context):
        Add_board(self.name, self.scale_x, self.scale_y, self.scale_z)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Thickness_15_Operator(bpy.types.Operator):
    bl_idname = "object.thickness_15"
    bl_label = "Thickness_15"

    def execute(self, context):
        thickness(15)
        return {'FINISHED'}

class Thickness_06_Operator(bpy.types.Operator):
    bl_idname = "object.thickness_06"
    bl_label = "Thickness_06"

    def execute(self, context):
        thickness(6)
        return {'FINISHED'}

class Thickness_18_Operator(bpy.types.Operator):
    bl_idname = "object.thickness_18"
    bl_label = "Thickness_18"

    def execute(self, context):
        thickness(18)
        return {'FINISHED'}



def Add_board(name, x, y, z):
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.object.name = name
    bpy.context.object.scale = (
        ((x/2)/1000),
        ((y/2)/1000),
        ((z/2)/1000)
    )
    bpy.context.object.location = (
        ((x/2)/1000),
        ((y/2)/1000),
        ((z/2)/1000)
        )
    bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)
   
def thickness(thick):
    bpy.context.object.dimensions[2] = (
    (thick/1000)
)
   
    # bpy.ops.transform.resize(value = (scale))
    # bpy.ops.transform.translate(value = scale)
