#
# This file is part of the RBLTracker Python Wrapper package.
#
# (c) Mike Pultz <mike@mikepultz.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import requests

from ..exception.exception import RBLTrackerException

class RequestHandler(object):

    def __init__(self, _account_sid, _api_token, _options):

        self.account_sid = _account_sid
        self.api_token = _api_token
        self.options = _options

    def get(self, _path, _params = {}):

        #
        # build the API URL using the path provided
        #
        url = self.options['url'] + _path + '.json';

        #
        # make the post request
        #
        res = requests.get(url, params = _params, auth=(self.account_sid, self.api_token))

        #
        # catch any JSON parsing exceptions
        #
        try:
            self.json = res.json()
        except ValueError:
            raise RBLTrackerException('ERROR: failed to parse JSON response')

        return self.json

    def post(self, _path, _params):

        #
        # build the API URL using the path provided
        #
        url = self.options['url'] + _path + '.json';

        #
        # make the post request
        #
        res = requests.post(url, data = _params, auth=(self.account_sid, self.api_token))

        #
        # catch any JSON parsing exceptions
        #
        try:
            self.json = res.json()
        except ValueError:
            raise RBLTrackerException('ERROR: failed to parse JSON response')

        return self.json
