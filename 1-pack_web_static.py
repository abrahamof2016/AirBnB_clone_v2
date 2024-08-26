#!/usr/bin/python3
# A fabric script to create a dated .tgz from AirBnB_clone/web_static

from fabric.api import *
from datetime import datetime

def do_pack():
    """
    generate a .tgz archive of the web_static directory with a timestamp.
    """


    # Create the versions directory if it doesn't exist.
    local("mkdir -p versions")

    # get current date and format for filename
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{now}.tgz"

    # Create the archive using tar (executed locally)
    check = local(f"tar -czvf versions/{archive_name} web_static")
    if check.failed:
        return None
    else:
        return archive_name
