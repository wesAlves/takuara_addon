import bpy


class Create_limits_Operator(bpy.types.Operator):
    bl_idname = "object.create_limits"
    bl_label = "Create_limits"

    origin = bpy.props.FloatProperty(name="Set the origin")
    wd = bpy.props.FloatProperty(name="Set the Width")
    dp = bpy.props.FloatProperty(name="Set the Depth")
    hg = bpy.props.FloatProperty(name="Set the Height")

    def execute(self, context):
        empty_positions = [(self.origin/1000), (self.wd/1000), (self.dp/1000), (self.hg/1000)]

        width = (empty_positions[1]-empty_positions[0])
        depth = (empty_positions[2]-empty_positions[0])
        height = (empty_positions[3]-empty_positions[0])

        print(empty_positions)

        create_empty(empty_positions[0], 0,0)
        bpy.context.object.name=("Origin_(%s, %s, %s)" %(empty_positions[0], empty_positions[0], empty_positions[0]))
        bpy.context.object.hide_viewport = True
        create_empty(empty_positions[1], 0,0)
        bpy.context.object.name=("width")
        bpy.context.object.hide_viewport = True
        create_empty(0, empty_positions[2],0)
        bpy.context.object.name=("depth")
        bpy.context.object.hide_viewport = True
        create_empty(0, 0, empty_positions[3])
        bpy.context.object.name=("height")
        bpy.context.object.hide_viewport = True


        create_base(width, depth, height)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


def create_empty(x, y, z):  # Add the empty
    bpy.ops.object.empty_add(location=(x, y, z))


def create_base(width, depth, height):  # create a wire that represents the whole shape
    bpy.ops.mesh.primitive_cube_add(location=((width/2), (depth/2), (height/2)))
    bpy.context.object.dimensions = (width, depth, height)
    bpy.context.object.display_type = 'WIRE'
    bpy.context.object.hide_select = True
    bpy.context.object.hide_render = True



def create_board(width, depth, height):  # create a board to test the tool
    bpy.ops.mesh.primitive_cube_add(location=((height/2), (depth/2), ((15/2)/1000)))
    bpy.context.object.dimensions = (height, depth, (15/1000))
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.context.object.rotation_euler[1] = -1.5708
    bpy.context.object.location[0] = 0.010


# collection to main scene collection => C.scene.collection.children.link(col[0])
