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

class Contact(object):

    def __init__(self, _handler):
        self.handler = _handler;

    def get(self, _contact_id):
        return self.handler.get('contact/' + _contact_id);

    def add(self, _args):
        return self.handler.post('contact/add', _args);

    def update(self, _contact_id, _args):
        return self.handler.post('contact/update/' + _contact_id, _args);

    def pause(self, _contact_id):
        return self.handler.post('contact/pause/' + _contact_id, {});

    def resume(self, _contact_id):
        return self.handler.post('contact/resume/' + _contact_id, {});

    def resend(self, _contact_id):
        return self.handler.post('contact/resend/' + _contact_id, {});

    def confirm(self, _contact_id):
        return self.handler.post('contact/confirm/' + _contact_id, { authcode: _authcode });

    def delete(self, _contact_id, _authcode):
        return self.handler.post('contact/delete/' + _contact_id, {});
