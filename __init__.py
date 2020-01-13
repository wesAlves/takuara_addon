# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Takuara_marcenaria",
    "author" : "Wes",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . new_board import *
from . menu import *
from . rotate_tool import *
from . move_tool import Move_tool_Operator
from . changeUnitis import ToMillimeters_Operator
from . clearScene import Delet_all_Operator
from . cutPlan import Cut_plan_Operator
from . add_columns import *
# def panel_func(self, context):
#     self.layout.operator(Add_new_board_Operator.bl_idname)

# def panel_func(self, context):
    # self.layout.operator(Add_new_board_Operator.bl_idname)

# def menu_draw(self, context):
#     self.layout.operator("wm.save_homefile")

classes = (
    Add_new_board_Operator,
    Menu_marcenaria_Operator,
    Rotate_tool_Operator,
    Move_tool_Operator,
    ToMillimeters_Operator,
    new_Tool,
    Delet_all_Operator,
    Cut_plan_Operator,
    Rotate_X_Operator,
    Rotate_Y_Operator,
    Rotate_Z_Operator,
    Thickness_06_Operator,
    Thickness_15_Operator,
    Thickness_18_Operator,
    Side_columns_Operator,
    FrontRear_columns_Operator,
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

        

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()