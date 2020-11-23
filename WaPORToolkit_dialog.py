# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WaporToolkitDialog
                                 A QGIS plugin
 This plugin helps retrieving and analysing data from the WaPOR server for a
 specified area
                             -------------------
        begin                : 2020-11-18
        copyright            : (C) 2020 by Celray James
        email                : celray.chawanda@outlook.com
        institution          : Vrije Universiteit Brussel
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads the .ui file so that PyQt can populate the plugin with the elements
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'WaPORToolkit_dialog_base.ui'))


class WaporToolkitDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WaporToolkitDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() access any designer object by doing
        # self.<objectname>, and I can use autoconnect slots
        # Reference: http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
