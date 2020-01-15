import bpy

class Side_column_Operator(bpy.types.Operator):
    bl_idname = "object.side_column_"
    bl_label = "Side_column_"

    name = bpy.props.StringProperty(name = "Board name:", default = "Board_")

    def execute(self, context):
        Add_board("side_%s" %s(self.name))
        return {'FINISHED'}


class Front_column_Operator(bpy.types.Operator):
    bl_idname = "object.front_column_"
    bl_label = "Front_column_"

    def execute(self, context):
        return {'FINISHED'}


class Line_board_Operator(bpy.types.Operator):
    bl_idname = "object.line_board_"
    bl_label = "Line_board_"

    def execute(self, context):
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

def get_locators():
    origin = bpy.data.objects['Origin_(0.0, 0.0, 0.0)']
    height = bpy.data.objects['height']
    depth = bpy.data.objects['depth']
    width = bpy.data.objects['width']
    return(origin, height, depth, width)