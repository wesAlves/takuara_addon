import bpy
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
    bpy.ops.wm.open_mainfile(filepath=(".\\base_render.blend"))
    print("working")

#### Open a file 
'''import bpy
import os

user = os.getlogin()
dir = "C:\\Users\\%s\\Documents\\Nova pasta" %(user)

def openFile():
    bpy.ops.wm.open_mainfile(filepath=("%s\\test.blend" %(dir)))

print(dir)
openFile()'''