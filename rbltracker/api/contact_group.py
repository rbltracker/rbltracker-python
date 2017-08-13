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

class ContactGroup(object):

    def __init__(self, _handler):
        self.handler = _handler;

    def get(self, _contact_group_id):
        return self.handler.get('contactgroups/' + _contact_group_id);

    def add(self, _args):
        return self.handler.post('contactgroups/add', _args);

    def update(self, _contact_group_id, _args):
        return self.handler.post('contactgroups/update/' + _contact_group_id, _args);

    def delete(self, _contact_group_id, _authcode):
        return self.handler.post('contactgroups/delete/' + _contact_group_id, {});
