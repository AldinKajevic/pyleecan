# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.PWSlot26
SlotW26 Setup Page
@date Created on Tue Mar 01 17:45:37 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

import PyQt5.QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.Gen_PWSlot26 import Gen_PWSlot26
from pyleecan.Methods.Slot.Slot.check import SlotCheckError

translate = PyQt5.QtCore.QCoreApplication.translate


class PWSlot26(Gen_PWSlot26, QWidget):
    """Page to set the Slot Type 26
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for Slot combobox
    slot_name = "Slot Type 26"
    slot_type = SlotW26

    def __init__(self, lamination=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot26
            A PWSlot26 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.lamination = lamination
        self.slot = lamination.slot
        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_R1.unit = "m"
        self.lf_R2.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_H0,
            self.unit_H1,
            self.unit_R1,
            self.unit_R2,
        ]
        for wid in wid_list:
            wid.setText(gui_option.unit.get_m_name())
        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H1.setValue(self.slot.H1)
        self.lf_R1.setValue(self.slot.R1)
        self.lf_R2.setValue(self.slot.R2)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_R1.editingFinished.connect(self.set_R1)
        self.lf_R2.editingFinished.connect(self.set_R2)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot26
            A PWSlot26 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot26
            A PWSlot26 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PWSlot26
            A PWSlot26 object
        """
        self.slot.H1 = self.lf_H1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R1(self):
        """Signal to update the value of R1 according to the line edit

        Parameters
        ----------
        self : PWSlot26
            A PWSlot26 object
        """
        self.slot.R1 = self.lf_R1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R2(self):
        """Signal to update the value of R2 according to the line edit

        Parameters
        ----------
        self : PWSlot26
            A PWSlot26 object
        """
        self.slot.R2 = self.lf_R2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.W0 is None:
            return translate("You must set W0 !", "PWSlot26 check")
        elif lam.slot.H0 is None:
            return translate("You must set H0 !", "PWSlot26 check")
        elif lam.slot.H1 is None:
            return translate("You must set H1 !", "PWSlot26 check")
        elif lam.slot.R1 is None:
            return translate("You must set R1 !", "PWSlot26 check")
        elif lam.slot.R2 is None:
            return translate("You must set R2 !", "PWSlot26 check")
        # Check that everything is set right
        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PWSlot26 check") + str(
                error
            )
        if yoke_height <= 0:
            return translate(
                "The slot height is greater than the lamination !", "PWSlot26 check"
            )
