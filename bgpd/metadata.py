# -*- coding: utf-8 -*-
"""Project metadata

Information describing the project.
"""
from datetime import datetime

# The package name, which is also the "UNIX name" for the project.
package = 'bgpd'
project = "Border Gateway Protocol Implementation"
project_no_spaces = project.replace(' ', '')
# Please follow https://www.python.org/dev/peps/pep-0440/
version = '0.0'
description = project
author = 'Christiaan Frans Rademan'
email = 'chris@fwiw.co.za'
license = 'Proprietary and Confidential'
copyright = '2021-%s %s' % (datetime.now().year, author,)
url = 'https://github.com/cfrademan/bgpd'
identity = project + ' v' + version

# Classifiers
# <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.6',
    ]
