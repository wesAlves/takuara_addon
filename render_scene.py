import bpy
import os

class Render_studio_Operator(bpy.types.Operator):
    bl_idname = "object.render_studio"
    bl_label = "render_studio"

    def execute(self, context):
        r_studio()
        return {'FINISHED'}


def r_studio():
    user = os.getlogin()
    dir = "C:\\Users\\%s\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81\\scripts\\addons\\takuara_addon" %(user)
    myfile = "%s\\base_render.blend" %(dir)
    # bpy.ops.wm.open_mainfile(filepath=("%s\\base_render.blend" %(dir)))
    with bpy.data.libraries.load(myfile) as (data_from, data_to):
        data_to.scenes = ["render_scene"]
    print("working")

# This works perfectly to open
# import bpy
# import os

# user = os.getlogin()
# dir = "C:\\Users\\%s\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81\\scripts\\addons\\takuara_addon-wes-feature-create-render-setup" %(user)
# myfile = "%s\\base_render.blend" %(dir)
# #print(myfile)
# with bpy.data.libraries.load(myfile) as (data_from, data_to):
#     files = []
#     for obj in data_from.objects:
#         files.append({'name' : obj})
#     bpy.ops.wm.append(directory=myfile+'\\Object\\', files=files)


# This works to append
# import bpy
# import os

# user = os.getlogin()
# dir = "C:\\Users\\%s\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81\\scripts\\addons\\takuara_addon-wes-feature-create-render-setup" %(user)
# myfile = "%s\\base_render.blend" %(dir)
# #print(myfile)
# with bpy.data.libraries.load(myfile) as (data_from, data_to):
#     data_to.scenes = ["teste"]

    # https://docs.blender.org/api/current/bpy.types.BlendDataLibraries.html?highlight=data_from

###Add the other scene to render scene
    import bpy

thisScene = bpy.data.collections
#print(len(thisScene))
print("NewLine")

for col in range(len(thisScene)):
    if thisScene[col].name != "render_collection":
        bpy.ops.object.collection_instance_add(name=thisScene[col].name, collection="render_collection")
        print(col)
        print(thisScene[col].name)