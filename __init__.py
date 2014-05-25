# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Export_all
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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Export_all class from file Export_all
    from export_all import Export_all
    return Export_all(iface)
