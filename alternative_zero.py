##############################################################################
#
# alternative_zero.py <timbob@bigpond.com>
#
# Assign another key, for example the backtick, to trigger the 0 button.
# Extended to allow for multiple assignments.
#
##############################################################################

from mnemosyne.core import *
from mnemosyne.pyqt_ui.plugin import get_main_widget
from qt import *
import sys

class AlternativeZero(Plugin):
    version = "1.0.0"

    main_dlg = get_main_widget()
    keymaps = [("`", main_dlg.grade_0_button.animateClick),
	       ("m", main_dlg.grade_0_button.animateClick),
	       ("j", main_dlg.grade_1_button.animateClick),
	       ("k", main_dlg.grade_2_button.animateClick),
	       ("l", main_dlg.grade_3_button.animateClick),
	       ("u", main_dlg.grade_4_button.animateClick),
	       ("i", main_dlg.grade_5_button.animateClick)
	      ]

    def description(self):
	return ("Assign extra keys to trigger grades. (v" + version + ")")

    def load(self):
	self.main_dlg = get_main_widget()

	self.actions = []
	for (key, func) in self.keymaps:
	    action = QAction(self.main_dlg, "action_" + key)
	    action.setAccel(QKeySequence(key))
	    self.main_dlg.connect(action, SIGNAL("activated()"), func)
	    self.actions.append((action, func))

    def unload(self):
	for (action, func) in self.actions:
	    self.main_dlg.disconnect(action, SIGNAL("activated()"), func)
	    action.setAccel(0)
	del self.actions

p = AlternativeZero()
p.load()

