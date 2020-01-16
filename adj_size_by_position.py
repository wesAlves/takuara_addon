import bpy


class Shrink_width_Operator(bpy.types.Operator):
    bl_idname = "object.shrink_width"
    bl_label = "Shrink_width"

    def execute(self, context):
        resize_by("x", "shrink")        
        return {'FINISHED'}

class Expand_width_Operator(bpy.types.Operator):
    bl_idname = "object.expand_width"
    bl_label = "Expand_width"

    def execute(self, context):
        resize_by("x", "expand")        
        return {'FINISHED'}

class Shrink_height_Operator(bpy.types.Operator):
    bl_idname = "object.shrink_height"
    bl_label = "Shrink_height"

    def execute(self, context):
        resize_by("x", "shrink")        
        return {'FINISHED'}

class Expand_height_Operator(bpy.types.Operator):
    bl_idname = "object.expand_height"
    bl_label = "Expand_height"

    def execute(self, context):
        resize_by("x", "expand")        
        return {'FINISHED'}

def resize_by(axis, act):
    width = bpy.context.object.dimensions[0]
    height = bpy.context.object.dimensions[1]
    # locX = bpy.context.object.location[0]
    # locY = bpy.context.object.location[1]
    # locZ = bpy.context.object.location[2]
    thickness = bpy.context.object.dimensions[2]
    if(axis == "x"):
        if(act == 'shrink'):
            bpy.context.object.dimensions[0]=(width-(thickness*2))
            # bpy.context.object.location[0]=(locX+thickness)
            # bpy.context.object.location[1]=(locY+thickness)
        elif (act == 'expand'):
            bpy.context.object.dimensions[0]=(width+(thickness*2))
            # if(locX <= 0):
            #     bpy.context.object.location[0]=(0)
            # else:
            #     bpy.context.object.location[0]=(locX-thickness)
            # if(locY <= 0):
            #     bpy.context.object.location[1]=(0)
            # else:
            #     bpy.context.object.location[1]=(locY-thickness)
            
    elif(axis == "y"):
        if(act == 'shrink'):
            bpy.context.object.dimensions[1]=(height-(thickness*2))
            # bpy.context.object.location[2]=(locZ+thickness)

        elif (act == 'expand'):
            bpy.context.object.dimensions[1]=(height+(thickness*2))
            # bpy.context.object.location[2]=(locZ-thickness)
            # if(locZ <= 0):
            #     bpy.context.object.location[2]=(0)
            # else:
            #     bpy.context.object.location[2]=(locY-thickness)

