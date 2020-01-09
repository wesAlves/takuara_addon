import bpy

def writing_cut_plan():
    objects = bpy.data.objects
    bpy.data.texts['cut_plan'].write("Length,Width,Qty,Material,Label,Enabled\n")     
    for obj in objects:
        obj_name = obj.name
        obj_dim = (str(round(obj.dimensions[0], 3)*1000) + "," + str(round(obj.dimensions[1], 3)*1000)+ "," + "1") #str(round(obj.dimensions[2], 3)*1000))
        material = ("Material_%s" %(round(obj.dimensions[2], 3)*1000))
        
        bpy.data.texts['cut_plan'].write(obj_dim + ",") #só funciona com string
        bpy.data.texts['cut_plan'].write(material + ",") #write the material name
        bpy.data.texts['cut_plan'].write(obj.name + ",true\n") #Add the lastest information to the line
        

def create_cut_plan():
    bpy.ops.text.new()
    tx = bpy.data.texts['Text']
    tx.name = ('cut_plan')

if 'cut_plan' in bpy.data.texts:
    bpy.data.texts['cut_plan'].clear()
    writing_cut_plan()
    
else:
    create_cut_plan()
    writing_cut_plan()