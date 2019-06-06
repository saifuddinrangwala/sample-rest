#!/usr/bin/python
# -*- coding: utf-8 -*-

import traceback
import logging
import uuid
from functools import wraps
from flask_restful import Resource
from flask import request, abort

from settings import context

APPLES = {
        1: {
            "id": 1,
            "color": "red"
            },
        2: {
            "id": 2,
            "color": "green"
            },
        3: {
            "id": 3,
            "color": "yellow"
            }
        }
BANANAS = {}

def register_api_set():
        # Setup all the apis here
        api = context.api
        api.add_resource(VersionsApi, "/versions")
        api.add_resource(UptimeApi, "/v1/uptime")
        api.add_resource(ApplesApiList, "/v1/apples")
        api.add_resource(ApplesApi, "/v1/apples/<int:id>")
        api.add_resource(BananasApi, "/v1/bananas/<string:id>")
        api.add_resource(BananasApiList, "/v1/bananas")


def auth_req(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not getattr(f, 'authenticated', True):
            return f(*args, **kwargs)

        # All apis are unauthenticated currently
        return f(*args, **kwargs)
    return wrapper


class UptimeApi(Resource):
    # Return all the api versions
    def get(self):
        return dict(uptime=context.uptime)


class VersionsApi(Resource):
    # Return all the api versions
    def get(self):
        return context.config.versions

class BananasApi(Resource):
    def get(self, id):
        if id in BANANAS:
            return BANANAS[id]
        abort(404)

class BananasApiList(Resource):
    def post(self):
        id = str(uuid.uuid4())
        obj = request.json
        obj['id'] = id
        BANANAS[id] = obj
        return obj

    def get(self):
        return dict(bananas=list(BANANAS.values()))


class ApplesApi(Resource):
    def get(self, id):
        if id in APPLES:
            return APPLES[id]
        abort(404)

class ApplesApiList(Resource):
    def get(self):
        return dict(apples=list(APPLES.values()))


