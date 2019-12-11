# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet14.Ui_PMagnet14 import (
    Ui_PMagnet14,
)


class Gen_PMagnet14(Ui_PMagnet14):
    def setupUi(self, PMagnet14):
        Ui_PMagnet14.setupUi(self, PMagnet14)
        # Setup of in_Hmag
        txt = self.tr(u"""magnet radial height [m]""")
        self.in_Hmag.setWhatsThis(txt)
        self.in_Hmag.setToolTip(txt)

        # Setup of lf_Hmag
        self.lf_Hmag.validator().setBottom(0)
        txt = self.tr(u"""magnet radial height [m]""")
        self.lf_Hmag.setWhatsThis(txt)
        self.lf_Hmag.setToolTip(txt)

        # Setup of in_Wmag
        txt = self.tr(u"""magnet bottom width [rad]""")
        self.in_Wmag.setWhatsThis(txt)
        self.in_Wmag.setToolTip(txt)

        # Setup of lf_Wmag
        self.lf_Wmag.validator().setBottom(0)
        txt = self.tr(u"""magnet bottom width [rad]""")
        self.lf_Wmag.setWhatsThis(txt)
        self.lf_Wmag.setToolTip(txt)

        # Setup of in_Rtopm
        txt = self.tr(u"""radius of the circular top shape [m]""")
        self.in_Rtopm.setWhatsThis(txt)
        self.in_Rtopm.setToolTip(txt)

        # Setup of lf_Rtopm
        self.lf_Rtopm.validator().setBottom(0)
        txt = self.tr(u"""radius of the circular top shape [m]""")
        self.lf_Rtopm.setWhatsThis(txt)
        self.lf_Rtopm.setToolTip(txt)
