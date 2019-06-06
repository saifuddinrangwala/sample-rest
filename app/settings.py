#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from flask import Flask
from flask_restful import Api
from flask import json
from flask import make_response
from flask_sqlalchemy import SQLAlchemy

from config import Config

class SampleService(object):

    def init(self, options):
        self._config = Config(options.conf)
#        self._config.setlogging()

        self._app = Flask(__name__)
        api = Api(self._app)
        self._api = api
        self._uptime = datetime.datetime.now()

        # Use flask json serializer
        @api.representation('application/json')
        def output_json(data, code, headers=None):
            resp = make_response(json.dumps(data), code)
            resp.headers.extend(headers or {})
            return resp

    @property
    def config(self):
        return self._config

    @property
    def app(self):
        try:
            return self._app
        except AttributeError:
            self.register()
        return self._app

    @property
    def api(self):
        return self._api

    @property
    def uptime(self):
        return self._uptime

    def run_service(self):
        self._app.run(host=self._config.my_ip,
                      port=self._config.port,
                      debug=self._config.debug)

    def register(self):
        import argparse
        parser = argparse.ArgumentParser(description='This is a sample rest service that serves apples and bananas.')
        parser.add_argument("-c", "--conf",
                        help="Configuration file path",
                        default="/sample-rest/etc/sample.conf")
        options = parser.parse_args()
        # Initialize the service
        self.init(options)
        import service_api
        service_api.register_api_set()

global context
context =  SampleService()
app = context.app
