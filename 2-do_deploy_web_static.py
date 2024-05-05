#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, run, put
import os

# Define the servers
env.user = 'ubuntu'  # SSH username
env.key_filename = 'my_ssh_private_key'  # SSH private key path
env.hosts = ['100.26.252.79', '34.232.69.77']  # IP addresses as strings


def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
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

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
