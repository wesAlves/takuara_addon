import bpy


class Adj_width_Operator(bpy.types.Operator):
    bl_idname = "object.adj_width"
    bl_label = "Adj_width"

    def execute(self, context):
        resize_by("x", "shirink")        
        return {'FINISHED'}

def resize_by(axis, act):
    width = bpy.context.object.dimensions[0]
    height = bpy.context.object.dimensions[1]
    locX = bpy.context.object.location[0]
    locY = bpy.context.object.location[1]
    thickness = bpy.context.object.dimensions[2]
    if(axis == "x"):
        if(act == 'shirink'):
            bpy.context.object.dimensions[0](width-(thickness*2))
            bpy.context.object.locations[0](locY-thickness)
        elif (act == 'expand'):
            bpy.context.object.dimensions[0](width+(thickness*2))
            bpy.context.object.locations[0](locY+thickness)

    # bpy.context.object.dimensions[1](height-(thickness*2))

