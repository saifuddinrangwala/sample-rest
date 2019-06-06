#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
from configparser import ConfigParser


class Config(object):

    DEFAULT_LOG_FILE = "/var/log/ansible-service.log"

    def __init__(self, configfile):

        self._configfile = configfile

        # Read the config file
        self._configparser = ConfigParser()
        self._configparser.read(configfile)

        self._debug = False

        # Set global logging parameters

    def setlogging(self):
        # Create logging root
        log_dir = os.path.dirname(self.log_file)
        if len(log_dir) > 0 and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        try:
            loglevel = self._configparser.get('DEFAULT', 'loglevel')
        except ConfigParser.NoOptionError:
            loglevel = "INFO"
        FORMAT = '%(levelname)s %(asctime)-15s %(message)s'
        logging.basicConfig(filename=self.log_file, level=loglevel, format=FORMAT)
        logging.debug("Config File:" + self._configfile)

        if loglevel.lower() == "debug":
            self._debug = True
        else:
            self._debug = False

    @property
    def debug(self):
        return self._debug

    @property
    def configfile(self):
        return self._configfile

    @property
    def log_file(self):
        try:
            return self._log_file
        except AttributeError:
            pass
        try:
            logfile = self._configparser.get('DEFAULT', 'log_file')
        except ConfigParser.NoOptionError:
            logfile = self.DEFAULT_LOG_FILE
        self._log_file = logfile
        return self._log_file

    @property
    def my_ip(self):
        try:
            return self._my_ip
        except AttributeError:
            pass
        try:
            my_ip = self._configparser.get('DEFAULT', 'my_ip')
        except ConfigParser.NoOptionError:
            my_ip = "127.0.0.1"
        self._my_ip = my_ip
        return self._my_ip

    @property
    def environment(self):
        try:
            return self._environment
        except AttributeError:
            pass
        try:
            environment = self._configparser.get('DEFAULT', 'environment')
        except ConfigParser.NoOptionError:
            environment = 'prod'
        self._environment = environment
        return self._environment

    @property
    def max_background_threads(self):
        try:
            return self._max_bg_threads
        except AttributeError:
            pass
        try:
            max_threads = self._configparser.getint('DEFAULT',
                                                    'max_background_threads')
        except ConfigParser.NoOptionError:
            # No limit on number of threads process can create
            max_threads = 65536
        if max_threads <= 0:
            max_threads = 65536
        self._max_bg_threads = max_threads
        return self._max_bg_threads

    @property
    def port(self):
        try:
            return self._port
        except AttributeError:
            pass
        try:
            port = self._configparser.getint('DEFAULT', 'port')
        except ConfigParser.NoOptionError:
            port = 3601
        self._port = port
        return self._port

    @property
    def versions(self):
        return {
                "versions": [
                    {
                        "id": "v1.0",
                        "status": "CURRENT",
                        "updated": "TBD",
                        "links": [
                            {
                                "href": "http://" + self.my_ip + ":" +
                                        str(self.port) + "/v1",
                                "rel": "self"
                            }
                        ]
                    }
                ]
            }

    @property
    def ansible_playbook(self):
        try:
            return self._ansible_playbook
        except AttributeError:
            pass
        try:
            ansible_playbook = self._configparser.get('ANSIBLE', 'ansible_exe')
        except ConfigParser.NoOptionError:
            ansible_playbook = "/usr/local/bin/ansible-playbook"
        self._ansible_playbook = ansible_playbook
        return self._ansible_playbook

    @property
    def stage_dir(self):
        try:
            return self._stage_dir
        except AttributeError:
            pass
        try:
            stage_dir = self._configparser.get('ANSIBLE', 'stage_dir')
        except ConfigParser.NoOptionError:
            stage_dir = "/tmp"

        if not os.path.exists(stage_dir):
            os.makedirs(stage_dir)

        self._stage_dir = stage_dir
        return self._stage_dir
