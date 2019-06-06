#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import argparse
import socket

from settings import context


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is a sample rest service that serves apples and bananas.')
    parser.add_argument("-c", "--conf",
                        help="Configuration file path",
                        default="/sample-rest/etc/sample.conf")
    options = parser.parse_args()
    # Initialize the service
    socket.setdefaulttimeout(900)
    context.init(options)
    import service_api
    service_api.register_api_set()
    context.run_service()
