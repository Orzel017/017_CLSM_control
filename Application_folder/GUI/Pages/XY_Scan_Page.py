"""
File name: "XY_Scan_Page.py"

Contents: UI elements to control Xy image taking

Dates:
Originally created: 01-17-2023
Last modified: 02-04-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Fill UI elements from previous GUI
"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

import matplotlib # generic Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

import sys
# print(sys.path)
sys.path.insert(0, "C:\Users\Orzel017main\Desktop\CLSM_control_software_main\017_CLSM_control\Application_folder\GUI\Helper_Utilities")
# import Helper_Utilities

# import path
# directory = path.Path(__file__).abspath()
# sys.path.append(directory.parent.parent)
# import GUI
# from GUI.Helper_Utilities import Plotting_Setup
# import Helper_Utilities
# from Application_folder.GUI.Helper_Utilities import Plotting_Setup
# import GUI
# from GUI.Helper_Utilities import Plotting_Setup

########################################################################################## end package imports ########################################################################################

def build_xy_scan_page(self): # define build_welcome_page to setup the xy scan page UI elements

    ##################################################################################### start create layout #########################################################################################

    self.behind_layout = QHBoxLayout() # create a QHBoxLayout

    self.behind_layout.setSpacing(1) # control space between widgets

    self.behind_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ##################################################################################### end create layout ###########################################################################################

    ######################################################################################## start frames #############################################################################################

    # creating two QFrames
    self.xy_scan_input_left_side = QFrame() # create left
    self.xy_scan_output_right_side = QFrame() # create right

    # manual dimensions
    maintain_aspect_ratio_one_to_one_dimension = 691 # designate fixed dimension variable for image area to be square
    self.xy_scan_output_right_side.setFixedSize(maintain_aspect_ratio_one_to_one_dimension, maintain_aspect_ratio_one_to_one_dimension) # set fixed dimensions of image area

    # adding widgets to background QFrames
    self.behind_layout.addWidget(self.xy_scan_input_left_side) # left
    self.behind_layout.addWidget(self.xy_scan_output_right_side) # right

    # frame edge styling
    self.xy_scan_input_left_side.setFrameShape(QFrame.StyledPanel) # top
    self.xy_scan_output_right_side.setFrameShape(QFrame.StyledPanel) # bottom

    ######################################################################################### end frames ##############################################################################################

    ###################################################################################### start contents #############################################################################################

    self.welcome_title_widget = QLabel("XY Scan Page") # create title widget

    self.welcome_title_widget.setParent(self.xy_scan_input_left_side) # designate parent of title widget

    self.welcome_title_widget.move(100, 100) # position the title

    ####################################################################################### start plot area ###########################################################################################


    ######################################################################################## end plot area ############################################################################################

    plot_res = 5.42
    # self.sc = Plotting_Setup.MplCanvas(self, canvas_width = plot_res, canvas_height = plot_res, canvas_dpi = 110)
    # self.sc.move(400, 400)
    # self.sc.setParent(self.xy_scan_output_left_side) # designate parent of plot area widget
    # self.sc.axes.xaxis.set_tick_params(labelsize = 8)
    # self.sc.axes.yaxis.set_tick_params(labelsize = 8)

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.XY_scan_page.setLayout(self.behind_layout) # display xy scan page UI elements

    ##################################################################################### end finalize page ###########################################################################################
