import bpy


class Move_positive_x_Operator(bpy.types.Operator):
    bl_idname = "object.move_positive_x"
    bl_label = "Move_positive_x"

    def execute(self, context):
        move_loc(0, "positive")
        return {'FINISHED'}

class Move_negative_x_Operator(bpy.types.Operator):
    bl_idname = "object.move_negative_x"
    bl_label = "Move_negative_x"

    def execute(self, context):
        move_loc(0, "negative")
        return {'FINISHED'}

class Move_positive_y_Operator(bpy.types.Operator):
    bl_idname = "object.move_positive_y"
    bl_label = "Move_positive_y"

    def execute(self, conteyt):
        move_loc(1, "positive")
        return {'FINISHED'}

class Move_negative_y_Operator(bpy.types.Operator):
    bl_idname = "object.move_negative_y"
    bl_label = "Move_negative_y"

    def execute(self, conteyt):
        move_loc(1, "negative")
        return {'FINISHED'}

class Move_positive_z_Operator(bpy.types.Operator):
    bl_idname = "object.move_positive_z"
    bl_label = "Move_positive_z"

    def execute(self, contezt):
        move_loc(2, "positive")
        return {'FINISHED'}

class Move_negative_z_Operator(bpy.types.Operator):
    bl_idname = "object.move_negative_z"
    bl_label = "Move_negative_z"

    def execute(self, contezt):
        move_loc(2, "negative")
        return {'FINISHED'}

class Move_To_origin_Operator(bpy.types.Operator):
    bl_idname = "object.move_to_origin"
    bl_label = "Move_to_origin"

    def execute(self, contezt):
        move_loc(0, "origin")
        move_loc(1, "origin")
        move_loc(2, "origin")
        return {'FINISHED'}


def move_thickness(axis, amount):
    bpy.context.object.location[axis] = amount


def move_loc(axis, direction):
    x = bpy.context.object.location[0]
    y = bpy.context.object.location[1]
    z = bpy.context.object.location[2]

    dz = bpy.context.object.dimensions[2]

    if (direction == "positive"):
        if (axis == 0):
            mov = (x + dz)
        elif (axis == 1):
            mov = y + dz
        elif (axis == 2):
            mov = z + dz
        else:
            pass
    elif (direction == "negative"):
        if (axis == 0):
            mov = (x - dz)
        elif (axis == 1):
            mov = y - dz
        elif (axis == 2):
            mov = z - dz
        else:
            pass
    elif (direction == "origin"):
        mov = 0
    else:
        pass

    move_thickness(axis, mov)
