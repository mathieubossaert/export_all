# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Export_allDialog
                                 A QGIS plugin
 export all
                             -------------------
        begin                : 2014-05-16
        copyright            : (C) 2014 by CEN L-R
        email                : sig@cenlr.org
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

from PyQt4 import QtCore, QtGui

from qgis.core import *
from qgis.gui import *

from ui_export_all import Ui_Export_all
# create the dialog for zoom to point

class Export_allDialog(QtGui.QDialog, Ui_Export_all):
        def __init__(self, iface):
                QtGui.QDialog.__init__(self)
                self.setupUi(self)
                self.iface = iface
                
                self.toolButton_Browse.clicked.connect(self.outputDir)                
        
        def outputDir(self):
		self.outDir = str(QtGui.QFileDialog.getExistingDirectory(self, u"Repertoire de destination des selections exportées"))
		if self.outDir == None:
			return
		self.lineEdit.clear()
		self.lineEdit.setText(self.outDir)


