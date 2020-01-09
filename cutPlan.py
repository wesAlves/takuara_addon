#TODO - Adequar para que seja uma class e criar menu
import bpy

def writing_cut_plan():
    objects = bpy.data.objects
    
    for obj in objects:
        obj_name = obj.name
        obj_dim = str(obj.dimensions)
        bpy.data.texts['cut_plan'].write(obj.name + "\t")
        bpy.data.texts['cut_plan'].write(obj_dim + "\n") #só funciona com string

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