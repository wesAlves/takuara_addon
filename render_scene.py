import bpy

import bpy

def render_single(frame):
    bpy.context.scene.frame_set(frame)
    bpy.ops.render.view_show()
    bpy.ops.render.render(use_viewport=False)
    
render_single(51)
#create a ui to set frame