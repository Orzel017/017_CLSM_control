"""
File name: "Galvo_Control_Page.py"

Contents: UI elements for XY sanning

Dates:
Originally created: 01-14-2023
Last modifed: 01-27-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:

"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QGridLayout, QLabel) # import submodules from PyQt5.QtWidgets

from PyQt5.QtCore import Qt # Qt module from QtCore

########################################################################################## end package imports ########################################################################################

def build_galvo_control_page(self):

    ################################################################################## start layout setup #############################################################################################

    self.background_layout = QGridLayout() # create highest-level background layout as QGridLayout

    self.background_layout.setSpacing(1) # control space between widgets

    self.background_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ################################################################################## end layout setup ###############################################################################################

    ################################################################################## start window setup #############################################################################################

    self.upper_left_window = QFrame()
    self.upper_left_window.setFrameShape(QFrame.StyledPanel)

    self.upper_right_window = QFrame()
    self.upper_right_window.setFrameShape(QFrame.StyledPanel)

    self.lower_left_window = QFrame()
    self.lower_left_window.setFrameShape(QFrame.StyledPanel)

    self.lower_right_window = QFrame()
    self.lower_right_window.setFrameShape(QFrame.StyledPanel)

    self.background_layout.addWidget(self.upper_left_window, 0, 0)
    self.background_layout.addWidget(self.upper_right_window, 0, 1)
    self.background_layout.addWidget(self.lower_left_window, 1, 0)
    self.background_layout.addWidget(self.lower_right_window, 1, 1)

    #################################################################################### end window setup #############################################################################################

    ################################################################################ start upper left window ##########################################################################################

    self.galvo_mirrors_individual_control_label = QLabel("Control both mirrors manually:")

    ################################################################################ end upper left window ############################################################################################

    self.galvo_control_widget = QLabel("Galvo Control Page") # create label widget

    self.galvo_control_widget.setParent(self.upper_left_window) # designate parent of label widget

    self.galvo_control_widget.move(300, 150) # position the label

    ##################################################################################### start finalize page #########################################################################################

    self.Galvo_control_page.setLayout(self.background_layout) # display galvo control page UI elements

    ##################################################################################### end finalize page ###########################################################################################
