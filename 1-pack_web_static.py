#!/usr/bin/python3
"""
Fabric script to generate tgz archive
"""

from datetime import datetime
from fabric.api import *

def do_pack():
    """
    making an archive on web_static
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p version')
    result = local('tar -cvzf version/{} web_static'.format(archive))
    if result.succeeded:
        return 'version/' + archive
    else:
        return None
