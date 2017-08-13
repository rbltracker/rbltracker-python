#
# This file is part of the RBLTracker Python Wrapper package.
#
# (c) Mike Pultz <mike@mikepultz.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import re

from .requesthandler import RequestHandler
from ..exception.exception import RBLTrackerException

class RBLProfile(object):

    def __init__(self, _handler):
        self.handler = _handler;

    def get(self, _rbl_profile_id):
        return self.handler.get('rblprofile/' + _rbl_profile_id);

    def add(self, _args):
        return self.handler.post('rblprofile/add', _args);

    def update(self, _rbl_profile_id, _args):
        return self.handler.post('rblprofile/update/' + _rbl_profile_id, _args);

    def delete(self, _rbl_profile_id, _authcode):
        return self.handler.post('rblprofile/delete/' + _rbl_profile_id, {});
