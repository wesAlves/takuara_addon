import bpy


class Side_columns_Operator(bpy.types.Operator):
    bl_idname = "object.side_columns"
    bl_label = "side_columns"

    height = bpy.props.FloatProperty(name = "Width")
    width = bpy.props.FloatProperty(name = "Height")

    def execute(self, context):
        Add_board("col_", height, width, 15, 90, 0)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)



class FrontRear_columns_Operator(bpy.types.Operator):
    bl_idname = "object.front_rear_columns"
    bl_label = "Front-Rear_columns"

    height = bpy.props.FloatProperty(name = "Width")
    width = bpy.props.FloatProperty(name = "Height")

    def execute(self, context):
        Add_board("col_", width, height, 15, 0, -90)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


def Add_board(name, x, y, z, rx, ry):
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
    bpy.context.object.rotation = (
        rx,
        ry,
        0
    )
    bpy.ops.object.transform_apply(location = True, rotation = False, scale = True)