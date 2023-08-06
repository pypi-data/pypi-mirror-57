""" Utilities for deploying applications to Sermos.

    Example CLI Usage:

        honcho run -e .env sermos_deploy
        --> Pipeline UUID: {abc-123}
        honcho run -e .env sermos_status {abc-123}

    Example Programmatic Usage:

        from sermos_utils.deploy import SermosDeploy

        sd = SermosDeploy(
            os.environ.get("SERMOS_DEPLOY_KEY", None),
            client_pkg_dir="sermos_demo_client"
        )

        # To Invoke
        status = sd.invoke_deployment()
        print(status)

        # To Check Status:
        status = sd.get_deployment_status(command_id)
        print(status)
"""
import os
import json
import subprocess
import base64
import logging
import requests
from sermos_utils.constants import ENV_VAR_DEPLOY_KEY, ENV_VAR_CLIENT_DIR,\
    DEFAULT_DEPLOY_URL, DEFAULT_YAML_NAME

logger = logging.getLogger(__name__)


def get_deploy_key(deploy_key: str = None):
    """ Verify deploy key provided, get from environment if not, exit if neither
    """
    deploy_key = deploy_key if deploy_key\
        else os.environ.get(ENV_VAR_DEPLOY_KEY, None)
    if deploy_key is None:
        msg = "Unable to find `deploy-key` in CLI arguments nor in "\
            "environment under `{}`".format(ENV_VAR_DEPLOY_KEY)
        logger.error(msg)
        raise ValueError(msg)
    return deploy_key


def get_client_pkg_dir(client_pkg_dir: str = None):
    """ Verify pkg dir provided, get from environment if not, exit if neither
    """
    client_pkg_dir = client_pkg_dir if client_pkg_dir\
        else os.environ.get(ENV_VAR_CLIENT_DIR, None)
    if client_pkg_dir is None:
        msg = "Unable to find `client-pkg-dir` in CLI arguments nor in "\
            "environment under `{}`".format(ENV_VAR_CLIENT_DIR)
        logger.error(msg)
        raise ValueError(msg)
    return client_pkg_dir


class SermosDeploy():
    def __init__(self, deploy_key: str = None, client_pkg_dir: str = None,
                 sermos_yaml_path: str = None, commit_hash: str = None,
                 deploy_url: str = None):
        """ Primary Sermos Deployment class for invocation and status updates.

            Arguments:
                deploy_key (optional): Deployment key, issued by Sermos, that
                    dictates the environment into which this request will be
                    deployed. Defaults to checking the environment for
                    `SERMOS_DEPLOY_KEY`. If not found, will exit.
                client_pkg_dir (optional): Directory name for your Python
                    package. e.g. my_package_name . If none provided, will check
                    environment for `SERMOS_CLIENT_PKG_DIR`. If not found,
                    will exit.
                sermos_yaml_path (optional): Path to find your `sermos.yaml`
                    configuration file. Defaults to
                    {{client_pkg_dir}}/sermos.yaml
                commit_hash (optional): The specific commit hash of your git repo
                    to deploy. If not provided, then current HEAD as of invocation
                    will be used. This is the default usage, and is useful in the
                    case of a CI/CD pipeline such that the Sermos deployment is
                    invoked after your integration passes.
                deploy_url (optional): Defaults to primary sermos deployment
                    endpoint. Only modify this if there is a specific, known reason
                    to do so.
        """
        super(SermosDeploy, self).__init__()
        self.deploy_key = get_deploy_key(deploy_key)
        self.client_pkg_dir = get_client_pkg_dir(client_pkg_dir)
        self.sermos_yaml_path = sermos_yaml_path if sermos_yaml_path\
            else "{}/{}".format(self.client_pkg_dir, DEFAULT_YAML_NAME)
        self.commit_hash = commit_hash
        self.encoded_sermos_yaml = None  # Established later, only on `invoke`
        self.deploy_payload = None  # Established later, only on `invoke`
        self.deploy_url = deploy_url if deploy_url\
            else DEFAULT_DEPLOY_URL
        self.headers = {
            'Content-Type': 'application/json',
            'apikey': self.deploy_key
        }

    def _set_commit_hash(self):
        """ Retrieve the commit hash of the current git state and set to
            current deployment object.
        """
        if self.commit_hash is None:
            self.commit_hash = subprocess.check_output(
                ["git", "rev-parse", "--verify", "HEAD"]
            ).strip().decode('utf-8')

    def _set_encoded_sermos_yaml(self):
        """ Provide the b64 encoded sermos.yaml file as part of request.
            Primarily used to get the custom workers definitions, etc. so
            the deployment endpoint can generate the values.yaml.
        """
        with open(self.sermos_yaml_path, 'r') as f:
            sermos_yaml = f.read()
            self.encoded_sermos_yaml =\
                base64.b64encode(sermos_yaml.encode('utf-8')).decode('utf-8')

    def _set_deploy_payload(self):
        """ Set the deployment payload correctly.
        """
        self._set_commit_hash()
        self._set_encoded_sermos_yaml()
        self.deploy_payload = {
            "sermos_yaml": self.encoded_sermos_yaml,
            "commit_hash": self.commit_hash,
        }

    def get_deployment_status(self, pipeline_uuid: str):
        """ Info on a specific pipeline
        """
        this_url = self.deploy_url + '/' + pipeline_uuid
        r = requests.get(this_url, headers=self.headers)
        return r

    def invoke_deployment(self):
        """ Invoke a Sermos AI Deployment

            If no commit_hash was provided, use the "current" commit hash
            of the client package during this invocation.

            Required convention is that your client's python package
            version number is specified in the file `my_package/__init__.py`
            and is defined as a string assigned to the variable `__version__`,
            e.g. `__version__ = '0.1.0'`
        """
        self._set_deploy_payload()

        # Make request to your environment's endpoint
        r = requests.post(
            self.deploy_url,
            headers=self.headers,
            data=json.dumps(self.deploy_payload)
        )
        return r
