##
## Copyright (C) 2010-2011 Mandriva S.A <http://www.mandriva.com>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
## Author(s): Paulo Belloni <paulo@mandriva.com>
##
##
import os
import logging

__author__  = "Paulo Belloni <paulo@mandriva.com>"
__state__   = "development"
__version__ = "0.8.3"

MANDRIVA_DATA_DIR = '/usr/share/mandriva'
DEFAULT_MPM_DIR = f'{MANDRIVA_DATA_DIR}/mpm'

if os.environ['MPM_ROOT_DIR']:
    MPM_ROOT_DIR = os.environ['MPM_ROOT_DIR']
else:
    MPM_ROOT_DIR = DEFAULT_MPM_DIR

MPM_BACKEND_DIR = f'{MPM_ROOT_DIR}/backend'
MPM_COMPONENTS_DIR = f'{MPM_ROOT_DIR}/components'
MPM_FRONTEND_DIR = f'{MPM_ROOT_DIR}/frontend'
MPM_QML_DIR = f'{MPM_FRONTEND_DIR}/qml'
MPM_IMAGES_DIR = f'{MPM_FRONTEND_DIR}/images'
MPM_CONFIG_DIR = f'{MPM_FRONTEND_DIR}/config'
MPM_JAVASCRIPT_DIR = f'{MPM_FRONTEND_DIR}/js'

MPM_USER_CONFIG_DIR = f"{os.environ['HOME']}/.mandriva/mpm/"
MPM_DEFAULT_LANG = 'en_US'

logger = logging.getLogger(__name__)
#try:
#    _syslog = logging.handlers.SysLogHandler(
#                  address="/dev/log",
#                  facility=logging.handlers.SysLogHandler.LOG_DAEMON
#              )
#    _syslog.setLevel(logging.INFO)
#    _formatter = logging.Formatter("%(name)s: %(levelname)s: "
#                                       "%(message)s")
#    _syslog.setFormatter(_formatter)
#except:
#    pass
#else:
#    logger.addHandler(_syslog)

_console = logging.StreamHandler()
_formatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)s]: "
                                   "%(message)s",
                               "%T")
_console.setFormatter(_formatter)
logger.addHandler(_console)
