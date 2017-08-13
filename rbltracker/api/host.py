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

class Host(object):

    def __init__(self, _handler):
        self.handler = _handler;

    def get(self, _host_id):
        return self.handler.get('host/' + _host_id);

    def add(self, _args):
        return self.handler.post('host/add', _args);

    def update(self, _host_id, _args):
        return self.handler.post('host/update/' + _host_id, _args);

    def pause(self, _host_id):
        return self.handler.post('host/pause/' + _host_id, {});

    def resume(self, _host_id):
        return self.handler.post('host/resume/' + _host_id, {});

    def delete(self, _host_id):
        return self.handler.post('host/delete/' + _host_id, {});
