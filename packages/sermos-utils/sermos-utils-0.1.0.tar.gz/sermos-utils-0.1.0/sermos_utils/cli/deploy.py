""" Command Line Utilities for Sermos
"""
import os
import logging
import click
from sermos_utils.deploy import SermosDeploy

logger = logging.getLogger(__name__)


@click.command()
@click.option('--deploy-key', required=False, default=None)
@click.option('--client-pkg-dir', required=False, default=None)
@click.option('--sermos-yaml-path', required=False, default=None)
@click.option('--commit-hash', required=False, default=None)
@click.option('--deploy-url', required=False, default=None)
def deploy(deploy_key: str = None, client_pkg_dir: str = None,
           sermos_yaml_path: str = None, commit_hash: str = None,
           deploy_url: str = None):
    """ Invoke a Sermos build for your application.

        Arguments:
            deploy-key (optional): Defaults to checking the environment for
                `SERMOS_DEPLOY_KEY`. If not found, will exit.
            client-pkg-dir (optional): Directory name for your Python package.
                e.g. my_package_name
                If none provided, will check environment for
                `SERMOS_CLIENT_PKG_DIR`. If not found, will exit.
            sermos-yaml-path (optional): Path to find your `sermos.yaml`
                    configuration file. Defaults to
                    {{client_pkg_dir}}/sermos.yaml
            commit-hash (optional): The specific commit hash of your git repo
                to deploy. If not provided, then current HEAD as of invocation
                will be used. This is the default usage, and is useful in the
                case of a CI/CD pipeline such that the Sermos deployment is
                invoked after your integration passes.
            deploy-url (optional): Defaults to primary sermos deployment
                endpoint. Only modify this if there is a specific, known reason
                to do so.
    """
    # Instantiate SermosDeploy
    sd = SermosDeploy(
        deploy_key=deploy_key, client_pkg_dir=client_pkg_dir,
        sermos_yaml_path=sermos_yaml_path, commit_hash=commit_hash,
        deploy_url=deploy_url
    )

    # Invoke deployment
    result = sd.invoke_deployment()
    content = result.json()
    if result.status_code < 300:
        logger.info("{}".format(content['message']))
        print("{}".format(content['message']))
    else:
        logger.error("{}".format(content))
    return


@click.command()
@click.argument('pipeline-uuid')
@click.option('--deploy-key', required=False, default=None)
@click.option('--deploy-url', required=False, default=None)
def status(pipeline_uuid: str, deploy_key: str = None, deploy_url: str = None):
    """ Check on the status of a Sermos build.

        Arguments:
            pipeline-uuid (required): Pipeline UUID reported by the invoke step.
            deploy-key (optional): Defaults to checking the environment for
                `SERMOS_DEPLOY_KEY`. If not found, will exit.
            deploy-url (optional): Defaults to primary sermos deployment
                endpoint. Only modify this if there is a specific, known reason
                to do so.
    """
    # Instantiate SermosDeploy
    sd = SermosDeploy(
        deploy_key=deploy_key, deploy_url=deploy_url
    )

    # Check deployment status
    result = sd.get_deployment_status(pipeline_uuid)
    content = result.json()
    if result.status_code < 300:
        logger.info("{}".format(content['message']))
        print("{}".format(content['message']))
    else:
        logger.error("{}".format(content))
    return
