import bpy

empty_positions = [0, 1.5, 1, 0.85]

width = (empty_positions[1]-empty_positions[0])
depth = (empty_positions[2]-empty_positions[0])
height = (empty_positions[3]-empty_positions[0])

def create_empty(x, y,z): #Add the empty
    bpy.ops.object.empty_add(location = (x, y, z))

def set_positions(): #Create a set of empties objects tha map all main positions, like origin, width, depth, height
    for i in range(len(empty_positions)):
        if(empty_positions[i] == empty_positions[0]):
            create_empty(empty_positions[0], 0,0)
            bpy.context.object.name=("Origin_(%s,%s,%s)" %(empty_positions[0], empty_positions[0], empty_positions[0]))
            bpy.context.object.hide_viewport = True

            
        elif(empty_positions[i] == empty_positions[1]):
            create_empty(empty_positions[1], 0,0)
            bpy.context.object.name=("width")
            bpy.context.object.hide_viewport = True

            
        elif(empty_positions[i] == empty_positions[2]):
            create_empty(0, empty_positions[2],0)
            bpy.context.object.name=("depth")
            bpy.context.object.hide_viewport = True


        elif(empty_positions[i] == empty_positions[3]):
            create_empty(0, 0, empty_positions[3])
            bpy.context.object.name=("height")
            bpy.context.object.hide_viewport = True

        i+=1
        
def create_cube(): #create a wire that represents the whole shape
    bpy.ops.mesh.primitive_cube_add(location = ((width/2), (depth/2), (height/2)))
    bpy.context.object.dimensions=(width, depth, height)
    bpy.context.object.display_type = 'WIRE'


set_positions()
create_cube()
    
def create_board(): #create a board to test the tool
    bpy.ops.mesh.primitive_cube_add(location = ((height/2), (depth/2), ((15/2)/1000)))
    bpy.context.object.dimensions=(height, depth, (15/1000))
    
    
create_board()