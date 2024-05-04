#!/usr/bin/python3
"""
Fabric script to generate tgz archive
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Create a compressed archive of the web_static folder
    """
    # Get the current time
    time = datetime.now()
    
    # Define the name of the archive
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    
    # Create the 'versions' directory if it doesn't exist
    local('mkdir -p versions')
    
    # Compress the web_static folder into the archive
    result = local('tar -cvzf versions/{} web_static'.format(archive_name))
    
    # Check if the archiving process was successful
    if result.succeeded:
        print("web_static packed: versions/{} -> {}Bytes".format(archive_name, result.return_code))
        return 'versions/' + archive_name
    else:
        return None
