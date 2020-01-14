import bpy

empty_positions = [0, 1.5, 1, 0.85]

width = (empty_positions[1]-empty_positions[0])
depth = (empty_positions[2]-empty_positions[0])
height = (empty_positions[3]-empty_positions[0])

def create_empty(x, y,z):
    bpy.ops.object.empty_add(location = (x, y, z))

def set_positions():
    for i in range(len(empty_positions)):
        if(empty_positions[i] == empty_positions[0]):
            create_empty(empty_positions[0], 0,0)
            
        elif(empty_positions[i] == empty_positions[1]):
            create_empty(empty_positions[1], 0,0)
            
        elif(empty_positions[i] == empty_positions[2]):
            create_empty(0, empty_positions[2],0)

        elif(empty_positions[i] == empty_positions[3]):
            create_empty(0, 0, empty_positions[3])

        i+=1
        
def create_cube():
    bpy.ops.mesh.primitive_cube_add(location = ((width/2), (depth/2), (height/2)))
    bpy.context.object.dimensions=(width, depth, height)

set_positions()
create_cube()
