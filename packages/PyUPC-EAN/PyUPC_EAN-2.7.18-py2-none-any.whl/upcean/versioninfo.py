'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2020 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2011-2020 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: versioninfo.py - Last Update: 12/3/2019 Ver. 2.7.18 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import datetime;

getcuryear = datetime.date.today().year;
if(getcuryear <= 2015):
 getcuryear = 2016;
getcuryear = str(getcuryear);
__author__ = "Kazuki Przyborowski";
__copyright__ = "(C) Game Maker 2k @ 2011-"+getcuryear;
__credits__ = ["Kazuki Przyborowski", "Game Maker 2k"];
__copyright_year__ = "2011-"+getcuryear;
__license__ = "Revised BSD License";
__license_string__ = """-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
		    Revised BSD License

Copyright (C) 2011-2020 Game Maker 2k. 
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

  2. Redistributions in binary form must reproduce the above copyright 
     notice, this list of conditions and the following disclaimer in 
     the documentation and/or other materials provided with the distribution.

  3. Neither the name of Game Maker 2k nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Game Maker 2k.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""";
__maintainer__ = "Kazuki Przyborowski";
__email__ = "kazuki.przyborowski@gmail.com";
__status__ = "Production";
__project__ = "PyUPC-EAN";
__project_url__ = "https://pypi.python.org/pypi/PyUPC-EAN";
__version_info__ = (2, 7, 18, "RC 1", 1);
__build_time__ = {"timestamp": 1575369741, "year": 2019, "month": 12, "day": 3, "hour": 4, "minute": 42, "second": 21};
__build_time_utc__ = {"timestamp": 1575391341, "year": 2019, "month": 12, "day": 3, "hour": 10, "minute": 42, "second": 21};
__build_python_info__ = {'node': 'DESKTOP-FV86102', 'machine': 'x86_64', 'python_revision': '', 'platform': 'Linux-4.4.0-18362-Microsoft-x86_64-with-glibc2.2.5', 'python_branch': '', 'python_implementation': 'CPython', 'python_build': ('default', 'Oct 22 2019 09:14:09'), 'mac_ver': ('', ('', '', ''), ''), 'system': 'Linux', 'win32_ver': ('', '', '', ''), 'python_version_tuple': ('2', '7', '17'), 'uname': ('Linux', 'DESKTOP-FV86102', '4.4.0-18362-Microsoft', '#476-Microsoft Fri Nov 01 16:53:00 PST 2019', 'x86_64', ''), 'version': '#476-Microsoft Fri Nov 01 16:53:00 PST 2019', 'libc_ver': ('glibc', '2.2.5'), 'architecture': ('64bit', 'ELF'), 'java_ver': ('', '', ('', '', ''), ('', '', '')), 'release': '4.4.0-18362-Microsoft', 'python_compiler': 'GCC 9.2.0', 'linux_distribution': ('', '', ''), 'processor': '', 'python_version': '2.7.17'};
def get_build_python_info(infotype=None):
 global __build_python_info__;
 python_info = __build_python_info__;
 if(infotype is None):
  return python_info;
 if(infotype is not None):
  return python_info.get(infotype, python_info);
__revision__ = __version_info__[3];
__revision_id__ = "$Id: f681652f671a9ccf481ff965799410bc704a7afa $";
if(__version_info__[3] is not None):
 __version__ = "{major}.{minor}.{build} {release}".format(major=__version_info__[0], minor=__version_info__[1], build=__version_info__[2], release=__version_info__[3]);
if(__version_info__[3] is None):
 __version__ = "{major}.{minor}.{build}".format(major=__version_info__[0], minor=__version_info__[1], build=__version_info__[2]);
__version_alt__ = "{major}.{minor}.{build}".format(major=__version_info__[0], minor=__version_info__[1], build=__version_info__[2]);
def version_info():
 if(__version_info__[3] is not None):
  return {"major": __version_info__[0], "minor": __version_info__[1], "build": __version_info__[2], "release": __version_info__[3]};
 if(__version_info__[3] is None):
  return {"major": __version_info__[0], "minor": __version_info__[1], "build": __version_info__[2], "release": None};
__version_date_info__ = (2019, 12, 3, "RC 1", 1);
def version_date():
 if(__version_date_info__[3] is not None):
  return {"year":__version_date_info__[0], "month": __version_date_info__[1], "day": __version_date_info__[2], "release": __version_date_info__[3]};
 if(__version_date_info__[3] is None):
  return {"year":__version_date_info__[0], "month": __version_date_info__[1], "day": __version_date_info__[2], "release": None};
__version_date__ = "{year}.{month}.{day}".format(year=__version_date_info__[0], month=__version_date_info__[1], day=__version_date_info__[2]);
__version_date_alt__ = "{year}.{month}.{day} {release}".format(year=__version_date_info__[0], month=__version_date_info__[1], day=__version_date_info__[2], release=__version_date_info__[2]);
