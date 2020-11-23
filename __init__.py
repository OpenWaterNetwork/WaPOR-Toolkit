# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WaporToolkit
                                 A QGIS plugin
 This plugin helps retrieving and analysing data from the WaPOR server for a
 specified area
                             -------------------
        begin                : 2020-11-19
        copyright            : (C) 2020 by Celray James
        email                : celray.chawanda@outlook.com

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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WaporToolkit class from file WaporToolkit.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .WaPORToolkit import WaporToolkit
    return WaporToolkit(iface)
