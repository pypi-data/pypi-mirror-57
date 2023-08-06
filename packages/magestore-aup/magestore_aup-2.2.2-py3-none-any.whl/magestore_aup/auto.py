# -*- coding: utf-8 -*-

import os
from fabric import Connection, Config, transfer
import uuid
import logging
import requests
import json
from packaging import version

_logger = logging.getLogger(__name__)

BUILT_REPO_OWNER = 'Magestore'
BUILT_REPO_NAME = 'go-built-packages'


# GITHUB API
def get_previous_newest_release_tag_names(repo_info):
    """
    Reference: https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository
    In case the newest tag name not available in built packages repo, we'll get the nearly newest tag name instead
    :param repo_info: (type:dict)
        repo_owner: (type:str)
        repo_name: (type:str)
        tag_name: (type:str)
    :return: (type:str) nearly newest tag name
    """
    _logger.info('Get previous newest release tag name instead')
    url = "https://api.github.com/repos/{repo_owner}/{repo_name}/releases".format(
        repo_owner=repo_info.get('repo_owner'),
        repo_name=repo_info.get('repo_name')
    )
    headers = {"Authorization": "token {token}".format(token=repo_info.get('access_token'))}
    try:
        resp = requests.get(url, headers=headers)
        newest_tag = [t.get('tag_name') for t in json.loads(resp.content)]
        newest_tag = sorted(newest_tag, key=lambda tag: version.parse(tag), reverse=True)
        prefix_tag_name = repo_info.get('tag_name').split('.')[0]
        nearly_newest_tag = [t for t in newest_tag if
                             t.split('.')[0] == prefix_tag_name and t != repo_info.get('tag_name')]
        return nearly_newest_tag[0] if nearly_newest_tag else False

    except Exception as e:
        print(e)
    return False


def get_almost_newest_release_by_tag_name(repo_info):
    """
    Get release before newest release, because sometime Automation API
    build not done before we need that
    """
    tag_name = repo_info.get('tag_name')
    url = "https://api.github.com/repos/{repo_owner}/{repo_name}/releases".format(
        repo_owner=repo_info.get('repo_owner'),
        repo_name=repo_info.get('repo_name')
    )
    headers = {"Authorization": "token {token}".format(token=repo_info.get('access_token'))}
    try:
        resp = requests.get(url, headers=headers)
        releases = json.loads(resp.content)
        for r in releases:
            check_version = r.get('tag_name').replace('v', '')
            newest_version = tag_name.replace('v', '')
            if newest_version[0] == check_version[0] and version.parse(newest_version) > version.parse(check_version):
                return r

    except Exception as e:
        _logger.error(e)
        return get_previous_newest_release_tag_names(repo_info)
    return False


def get_release_by_tag_name(repo_info):
    """
    Reference: https://developer.github.com/v3/repos/releases/#get-a-release-by-tag-name
    :param repo_info: (type:dict)
        repo_owner: (type:str)
        repo_name: (type:str)
        tag_name: (type:str)
    :return: (type:dict) release object
    """
    url = "https://api.github.com/repos/{repo_owner}/{repo_name}/releases/tags/{tag_name}".format(
        repo_owner=repo_info.get('repo_owner'),
        repo_name=repo_info.get('repo_name'),
        tag_name=repo_info.get('tag_name')
    )
    headers = {"Authorization": "token {token}".format(token=repo_info.get('access_token'))}
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return json.loads(resp.content)
    except Exception as e:
        _logger.error(e)
    return False


def get_built_package_donwload_url(repo_info):
    built_repo_info = {
        'repo_name': BUILT_REPO_NAME,
        'repo_owner': BUILT_REPO_OWNER,
        'tag_name': "{repo_name}-{tag_name}".format(repo_name=repo_info.get('repo_name'),
                                                    tag_name=repo_info.get('tag_name')),
        'access_token': repo_info.get('access_token')
    }
    release = get_release_by_tag_name(built_repo_info)
    if not release:
        almost_newest_release = get_almost_newest_release_by_tag_name(repo_info)
        built_repo_info.update({
            'tag_name': "{repo_name}-{tag_name}".format(repo_name=repo_info.get('repo_name'),
                                                        tag_name=almost_newest_release.get('tag_name'))
        })
        release = get_release_by_tag_name(built_repo_info)
    release_not_found = False

    if not release or not release.get('assets'):
        release_not_found = True
    else:
        assert_name = "%s.tar.gz" % built_repo_info.get('tag_name')
        asset_url = [asst.get('url') for asst in release.get('assets') if asst.get('name') == assert_name][0]
        if not asset_url:
            release_not_found = True
        if not release_not_found:
            asset_url += "?access_token={access_token}".format(access_token=repo_info.get('access_token'))
            return asset_url

    if release_not_found:
        raise Exception("Can't find any asset matched the tag name %s in %s-%s repository" % (
            built_repo_info.get('tag_name'), built_repo_info.get('repo_owner'), built_repo_info.get('repo_name')))


def install_required_lib(conn):
    try:
        conn.sudo("apt-get install -y curl", hide="both")
    except Exception as e:
        pass


def get_absolute_path(relative_path):
    """
    :param relative_path: relative path of the file to the current directory of auto.py file
    :return:
    """
    # current directory path that contain this file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return "{0}/{1}".format(dir_path, relative_path)


def get_connection(host, user, su_pass='', key_path=''):
    if key_path:
        c = Connection(host, user, connect_kwargs={'key_filename': key_path})
    else:
        config = Config(overrides={'sudo': {'password': su_pass, "prompt": "[sudo] password: \n"}})
        c = Connection(host, user, connect_kwargs={"password": su_pass}, config=config)
    return c


def send_files_to_remote_server(connection, source_path, dest_path):
    """
    :param connection: connection to remote server
    :param source_path: path to file on local server
    :param dest_path: path to folder will be contain file on remote server
    :return: None
    """
    transfer_obj = transfer.Transfer(connection)
    transfer_obj.put(source_path, dest_path)


def update_deploy_script_path(repo_info, instance_info, unique_str):
    raw_deploy_script_path = get_absolute_path('data/raw_deploy.sh')
    deploy_script_path = "/tmp/%s-deploy.sh" % unique_str
    built_package_download_url = get_built_package_donwload_url(repo_info)

    with open(raw_deploy_script_path, 'r') as f:
        content = f.read()
        content_keys = {
            "<repo_name>": repo_info.get('repo_name'),
            "<repo_owner>": repo_info.get('repo_owner'),
            "<tag_name>": repo_info.get('tag_name'),
            "<access_token>": repo_info.get('access_token'),
            "<source_folder>": instance_info.get('source_folder'),
            "<web_container_id>": instance_info.get('web_container_id', ''),
            "<unique_str>": unique_str,
            "<built_package_download_url>": built_package_download_url
        }
        for key in content_keys:
            content = content.replace(key, content_keys.get(key))

    with open(deploy_script_path, 'w') as f:
        f.write(content)

    return deploy_script_path


def deploy(repo_info, instance_info):
    conn = get_connection(
        host=instance_info.get('ip'),
        user=instance_info.get('user'),
        su_pass=instance_info.get('password', ''),
        key_path=instance_info.get('local_key_file_path') or instance_info.get('key_path', '')
    )
    unique_str = str(uuid.uuid4())
    deploy_script_path = update_deploy_script_path(repo_info, instance_info, unique_str)
    send_files_to_remote_server(conn, deploy_script_path, '/tmp')
    install_required_lib(conn)

    print("Deploying package to server ... ")
    conn.run("bash %s > /dev/null" % deploy_script_path, hide="both", warn=True)
    conn.run('rm -rf %s' % deploy_script_path, hide='both', warn=True)
    os.system('rm -rf %s' % deploy_script_path)
    return True
