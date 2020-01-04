import bpy


class Add_new_board_Operator(bpy.types.Operator):
    bl_idname = "object.add_new_board"
    bl_label = "Add_new_board"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")
    scale = bpy.props.FloatVectorProperty( name = "Board size", default = (1.0, 1.0, 0.0075))
    
    def execute(self, context):
        Add_board(self.name, self.scale)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


def Add_board(name, scale):
    bpy.ops.mesh.primitive_cube_add()
    bpy.context.object.name = name
    bpy.ops.transform.resize(value = scale)
    bpy.ops.transform.translate(value = scale)
    bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)
