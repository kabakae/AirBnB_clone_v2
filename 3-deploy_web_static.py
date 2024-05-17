#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, run, put, local
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the servers
env.user = 'ubuntu'  # SSH username
env.key_filename = 'my_ssh_private_key'  # SSH private key path
env.hosts = ['100.26.252.79', '34.232.69.77']  # IP addresses as strings


def do_pack():
    """
    Creates an archive from the web_static folder locally
    """
    try:
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Create the directory
        os.makedirs("versions", exist_ok=True)

        # Create a custom HTML file
        with open("web_static/my_index.html", "w") as f:
            f.write("<html><head></head><body>Hello world!</body></html>")

        # Tar the folder
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        logger.error("Error occurred while creating archive: %s", e)
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        logger.error("Archive %s not found.", archive_path)
        return False

    try:
        # Upload the archive to /tmp/ directory of the web servers
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/<archive filename >
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]
        releases_path = '/data/web_static/releases/'

        run('mkdir -p {}{}'.format(releases_path, archive_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_filename,
            releases_path, archive_name))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(archive_filename))

        # Move files from extracted folder to the correct location
        run('mv {}{}/web_static/* {}{}/'.format(releases_path, archive_name,
            releases_path, archive_name))

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(releases_path,
            archive_name))

        logger.info("New version deployed!")
        return True
    except Exception as e:
        logger.error("Error occurred while deploying: %s", e)
        return False


def deploy():
    """
    Deploy the web_static archive to the web servers
    """
    # Create the archive
    archive_path = do_pack()
    if archive_path is None:
        return False

    # Deploy locally
    local_deployed = local("tar -xzf {} -C ./versions/".format(archive_path))
    if local_deployed.failed:
        logger.error("Local deployment failed")
        return False

    # Deploy remotely
    return do_deploy(archive_path)


deploy()
