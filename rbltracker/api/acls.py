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

class ACLs(object):

    def __init__(self, _handler):
        self.handler = _handler;

    def get(self, _args = {}):
        return self.handler.get('acls', _args);
