class behavior_flage:
    def __init__(self):
        self.plan_to_mining_fl = True
        self.goto_mining_fl = False
        self.do_mining_fl = False
        self.plan_to_berm_fl = False
        self.goto_berm_fl = False
        self.deposit_fl = False
        self.dcs_ost_extrustio_fl = False
        self.adjust_goal_point_fl = False
        self.identify_obsticl_fl = False
        self.identify_obsticle_fl = False
        self.retrace_path_fl = False

    def del_fl(self):
        self.plan_to_mining_fl = False
        self.goto_mining_fl = False
        self.do_mining_fl = False
        self.plan_to_berm_fl = False
        self.goto_berm_fl = False
        self.deposit_fl = False
        self.dcs_ost_extrustio_fl = False
        self.adjust_goal_point_fl = False
        self.identify_obsticl_fl = False
        self.identify_obsticle_fl = False
        self.retrace_path_fl = False
# path plan to mining
def plan_to_mining(is_planning_failed):
    while (is_planning_failed):
        # Decrease obstacle extrusion

    else:
        # go to mining area

def goto_mining(is_robot_stuck, is_map_changed):
    if (is_robot_stuck):
        # Identify obsiticle
    elif (is_map_changed):
        # stop moving & back to pathplan_to_mining
    else:
        # at mining area & do mining

def do_mining():
    # be sad & need more detail

def plan_to_berm(is_planning_failed):
    while is_planning_failed:
        # Decrease obstacle extrusion
    else:
        #  go to berm

def goto_berm(is_robot_stuck, is_map_changed):
    if (is_robot_stuck):
        # Identify obsiticle
    elif (is_map_changed):
        # stop moving & back to pathplan_to_mining
    else:
        # deposit

def deposit():
    while (is_deposit_failed):

    # bin empty & goto plan to mining

def dcs_ost_extrustion():
    if (is_decreased):
        # adj goal point

def adjust_goal_point():

def identify_obsticle():
    if (is_crater):
        # wiggle
    else:
        # retrace_path

def retrace_path():
