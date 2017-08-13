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

class RBL(object):

    def __init__(self, _handler):
        self.handler = _handler;

    def get(self, _rbl_id):
        return self.handler.get('rbl/' + _rbl_id);

    def add(self, _args):
        return self.handler.post('rbl/add', _args);

    def update(self, _rbl_id, _args):
        return self.handler.post('rbl/update/' + _rbl_id, _args);

    def pause(self, _rbl_id):
        return self.handler.post('rbl/pause/' + _rbl_id, {});

    def resume(self, _rbl_id):
        return self.handler.post('rbl/resume/' + _rbl_id, {});

    def delete(self, _rbl_id, _authcode):
        return self.handler.post('rbl/delete/' + _rbl_id, {});
