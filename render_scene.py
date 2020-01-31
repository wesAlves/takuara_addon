import bpy
import os
import addon_utils

class Render_studio_Operator(bpy.types.Operator):
    bl_idname = "object.render_studio"
    bl_label = "render_studio"

    def execute(self, context):
        r_studio()
        return {'FINISHED'}

class Attach_Operator(bpy.types.Operator):
    bl_idname = "object.attach"
    bl_label = "Attach"

    def execute(self, context):
        attach_scenes()
        return {'FINISHED'}


def r_studio():
    # user = os.getlogin()
    addon_utils.modules_refresh()
    for mod in (addon_utils.addons_fake_modules):
        location = addon_utils.addons_fake_modules[mod].bl_info['location']
        if location == 'takuara_addon':
            ver = "%s%s%s" %(addon_utils.addons_fake_modules[mod].bl_info['version'][0], addon_utils.addons_fake_modules[mod].bl_info['version'][1], addon_utils.addons_fake_modules[mod].bl_info['version'][2])
            cVersion = ("%s-%s" %(location, ver))
            # dir = "C:\\Users\\%s\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81\\scripts\\addons\\%s" %(user,cVersion)
            dir = select_path[1]
            myfile = "%s\\base_render.blend" %(dir)
            files = []
            with bpy.data.libraries.load(myfile) as (data_from, data_to):
                data_to.scenes = ["render_scene"]
                data_to.worlds = ['studio', 'artist_workshop', 'entrance_hall', 'varanda']


def attach_scenes():
    thisScene = bpy.data.collections
    render_coll = bpy.data.scenes['render_scene'].collection.children['render_collection']
    for col in range(len(thisScene)):
        if thisScene[col].name != "render_collection":
            bpy.ops.object.select_all(action='DESELECT')
            removeToRender()
            addToRender(thisScene, render_coll, col)

def addToRender(thisScene, render_coll, col):
    bpy.ops.object.select_same_collection(collection="render_collection")
    bpy.ops.object.delete()
    bpy.ops.object.collection_instance_add(name=thisScene[col].name, collection = 'render_collection', align="WORLD", location=(0, 0, 0))
    render_coll.objects.link(bpy.context.object)
    bpy.ops.collection.objects_remove_active()
    print(thisScene[col])
    print('criado')
    
def removeToRender():
    bpy.ops.object.select_same_collection(collection="render_collection")
    bpy.ops.object.delete()
    print('yes is workin')

select_path = addon_utils.paths()

