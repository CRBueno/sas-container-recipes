#!/usr/bin/env python
"""A smoke test for containers"""

import json
import logging
import os
import pytest
import requests
import time

from kubetest_stdlib import testutils
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Supress warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logger = logging.getLogger(__name__)


class TestSmoke():
    """ Use pytest to execute rest api operations against a container. """

    @classmethod
    def setup_class(cls):
        """
        Setup environment for the upcoming tests. This is basically the constructor for
        this test class. Its used to create the KubeUtils API instance used by some
        tests, retrieve environment variables from the testconfig.yaml and set up any
        structures and variables that might be used by All of the test methods below.

        """
        # Initial setup
        test_target = "consul"
        test_vars = testutils.k8s_test_setup(test_target)
        # Expose variables to test functions
        cls.TARGET_BASE_NAME = test_target
        cls.TARGET_POD_NAME = test_vars.get("target_pod_name")
        cls.NAMESPACE = test_vars.get("namespace")
        cls.kubeutilobj = test_vars.get("kubeutilobj")


    def test_01_consul__not_root(self):
        """
        Check user root
        """
        time.sleep(1)
        cmd = "exec {} whoami".format(self.TARGET_POD_NAME)
        status,result = self.kubeutilobj.kubectl(cmd, self.NAMESPACE)
        error_flag = False
        if "failure" in status.lower() or b"root" in result["output"]:
            error_flag = True
        assert error_flag == False

    def test_02_hostname(self):
        """
        Check consul in hostname
        """
        cmd = "exec {} hostname".format(self.TARGET_POD_NAME)
        status, result = self.kubeutilobj.kubectl(cmd, self.NAMESPACE)
        assert self.TARGET_BASE_NAME in result["output"].decode("utf-8")

    def test_03_agent_self_no_tls(self):
        '''
        Ensure agent member name contains pod name
        http://consul.kubeworker1.sas.com/v1/agent/self

        '''
        url = "http://localhost:8500/v1/agent/self"
        cmd = 'exec {} -- curl -s -o /dev/null -w '.format(self.TARGET_POD_NAME) + \
               str('"%{http_code}"') + ' {}'.format(url)
        status, result = self.kubeutilobj.kubectl(cmd, self.NAMESPACE)
        print(result)
        assert b"200" in result["output"]

    def test_04_agent_member_no_tls(self):
        '''
        http://consul.kubeworker1.sas.com/v1/agent/peers
        '''
        url = "http://localhost:8500/v1/agent/members"
        cmd = 'exec {} -- curl -s -o /dev/null -w '.format(self.TARGET_POD_NAME) + \
               str('"%{http_code}"') + ' {}'.format(url)
        status, result = self.kubeutilobj.kubectl(cmd, self.NAMESPACE)
        print(result)
        assert b"200" in result["output"]

    def test_05_sasops_validate(self):
        '''
        Ensure no errors from sas-ops validate

        '''
        result = testutils.ops_validate(self.TARGET_POD_NAME, \
                                        self.NAMESPACE, \
                                        self.kubeutilobj)
        error_flag = False
        for msg in result:
            if isinstance(msg, dict) and 'error' in msg.get("level").lower():
                error_flag = True
                print("ERROR found: %s: %s", msg.get("id"), msg.get("text"))
        if isinstance(result, str) and "failure" in result.lower():
            error_flag = True
        assert error_flag == False

    def test_06_sasops_env_hostname(self):
        '''
        Ensure target pod name in sas-ops env short hostname

        '''
        result = testutils.ops_env(self.TARGET_POD_NAME, \
                                        self.NAMESPACE, \
                                        self.kubeutilobj)
        shorthost = result.get("Host Information").get("Short hostname")
        assert shorthost in self.TARGET_POD_NAME

    def test_07_sasops_services(self):
        '''
        Ensure sas-ops services list not empty

        '''
        result = testutils.ops_services(self.TARGET_POD_NAME, \
                                        self.NAMESPACE, \
                                        self.kubeutilobj)
        print(result)
        error_flag = False
        if not isinstance(result, list) or len(result) < 1:
            error_flag = True
        assert error_flag == False