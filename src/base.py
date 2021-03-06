#!/bin/env python3

## Python 2.7.X -> 3.0.X
## Base class: a common class to wrap all the shared method
## Author: Isham J. Araia @ None

import re
import sys
import requests as rq
import json
import logging as log
import datetime

class Base(object):
    """
    Class used to wrap all the common methods
    """
    def __init__(self):
        pass

    def _valid_url(self, host):

        """
        Check if the URL syntax it's valid.
        """

        cpattern = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'consulmod|' #test...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(cpattern, host) == None:
            return False
        else: 
            return True

    def log(self, message, level):
        """
        Method used to log across all the package.
        Lv -> 1 INFO
        Lv -> 2 WARN
        Lv -> 3 ERR
        Lv -> 4 CRITICAL
        """

        if not message or not level:
            message = '2 valid arguments are required: "message" and "level". See help().'
            level = 4
        
        lvs = {
            1 : "INFO", 
            2 : "WARN",
            3 : "ERR",
            4 : "CRITICAL"
        }

        date = datetime.datetime.utcnow()
        stm = "{}: {} - {}".format(lvs[level], date, message)
        return stm

    def _put(self, headers, item, data={}):
        """
        Method to put info from the consul backend.
        """

        # Compose url to call
        url = "{}{}/{}".format(
            self.host, 
            self.path,
            item
        )

        resp = rq.put(url, headers=headers, data=json.dumps(data))
        return resp.content
    
    def _get(self, headers, item):
        """
        Method to get info from the consul backend.
        """

        # Compose url to call
        url = "{}{}/{}".format(
            self.host, 
            self.path,
            item
        )

        resp = rq.get(url, headers=headers)
        return resp.content

    
    def _delete(self, headers, item, data={}):
        """
        Method to delete from the consul backend.
        """

        # Compose url to call
        url = "{}{}/{}".format(
            self.host, 
            self.path,
            item
        )
        resp = rq.delete(url, headers=headers, data=json.dumps(data))
        return resp.content

    def _post(self, headers, item, data={}):
        """
        Method to put info from the consul backend.
        """

        # Compose url to call
        url = "{}{}/{}".format(
            self.host, 
            self.path,
            item
        )
        resp = rq.post(url, headers=headers, data=json.dumps(data))
        return resp.content