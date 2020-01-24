import bpy
import os
# import base_render.blend

# def render_single(frame):
#     bpy.context.scene.frame_set(frame)
#     bpy.ops.render.view_show()
#     bpy.ops.render.render(use_viewport=False)
    
# render_single(51)
#create a ui to set frame

class Render_studio_Operator(bpy.types.Operator):
    bl_idname = "object.render_studio"
    bl_label = "render_studio"

    def execute(self, context):
        r_studio()
        return {'FINISHED'}


def r_studio():
    user = os.getlogin()
    dir = "C:\\Users\\%s\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81\\scripts\\addons\\takuara_addon-wes-feature-create-render-setup" %(user)
    bpy.ops.wm.open_mainfile(filepath=("%s\\base_render.blend" %(dir)))
    print("working")

This works perfectly
import bpy
import os

user = os.getlogin()
dir = "C:\\Users\\%s\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81\\scripts\\addons\\takuara_addon-wes-feature-create-render-setup" %(user)
myfile = "%s\\base_render.blend" %(dir)
#print(myfile)
with bpy.data.libraries.load(myfile) as (data_from, data_to):
    files = []
    for obj in data_from.objects:
        files.append({'name' : obj})
    bpy.ops.wm.append(directory=myfile+'\\Object\\', files=files)