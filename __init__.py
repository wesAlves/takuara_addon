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
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . new_board import *
# from . menu import *
from . rotate_tool import *
from . move_tool import Move_tool_Operator
from . changeUnitis import ToMillimeters_Operator
from . clearScene import Delet_all_Operator
from . cutPlan import Cut_plan_Operator
from . add_columns import *
from . thick import *
from . create_empty import *
from . create_and_place import *
from . adj_size_by_position import *
from . render_scene import *
from . ui import *

classes = (
    Add_new_board_Operator,
    Rotate_tool_Operator,
    Move_tool_Operator,
    ToMillimeters_Operator,
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
    Move_positive_x_Operator,
    Move_negative_x_Operator,
    Move_positive_y_Operator,
    Move_negative_y_Operator,
    Move_positive_z_Operator,
    Move_negative_z_Operator,
    Move_To_origin_Operator,
    Create_limits_Operator,
    Shrink_width_Operator,
    Shrink_height_Operator,
    Expand_width_Operator,
    Expand_height_Operator,
    Render_studio_Operator,
    Attach_Operator,
    Side_L_column_Operator,
    Side_R_column_Operator,
    Side_M_column_Operator,
    Front_column_Operator,
    Back_column_Operator,
    FB_M_column_Operator,
    Top_board_Operator,
    Bottom_board_Operator,
    Line_board_Operator,
    Main_Controls_PT_panel,
    Creation_Controls_PT_panel,
    Adjusts_Controls_PT_panel,
    Render_Controls_PT_panel,
    Cut_Plane_PT_panel,
    
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

        

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()