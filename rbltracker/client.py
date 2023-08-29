#
# This file is part of the RBLTracker Python Wrapper package.
#
# (c) Mike Pultz <mike@mikepultz.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import re

from .exception.exception import RBLTrackerException
from .api.requesthandler import RequestHandler

from .api.acls import ACLs

from .api.check import Check

from .api.listings import Listings

from .api.host import Host
from .api.hosts import Hosts

from .api.contact import Contact
from .api.contacts import Contacts

from .api.contact_group import ContactGroup
from .api.contact_groups import ContactGroups

from .api.rbl import RBL
from .api.rbls import RBLs

from .api.rbl_profile import RBLProfile
from .api.rbl_profiles import RBLProfiles

from .api.monitoring_profile import MonitoringProfile
from .api.monitoring_profiles import MonitoringProfiles

class Client(object):

    def __init__(self, _account_sid, _api_token):

        #
        # Python library version
        #
        self.version = '1.1.0'

        #
        # validate account SID
        #
        if re.match(r'^[A-Z]{2}[0-9a-f]{32}$', _account_sid):
            self.account_sid = _account_sid
        else:
            raise RBLTrackerException('ERROR: invalid API acount sid provided: ' + _account_sid)

        #
        # validate the APi token
        #
        if re.match(r'^[0-9a-f]{64}$', _api_token):
            self.api_token = _api_token
        else:
            raise RBLTrackerException('ERROR: invalid API access token provided: ' + _api_token)

        #
        # the default API settings
        #
        self.options = {
            'url': 'https://api.rbltracker.com/3.0/'
        }

        self.request = RequestHandler(self.account_sid, self.api_token, self.options);

        #
        # acls
        #
        self.acls = ACLs(self.request)

        #
        # manual check
        #
        self.check = Check(self.request)

        #
        # listings
        #
        self.listings = Listings(self.request)

        #
        # hosts
        #
        self.host = Host(self.request)
        self.hosts = Hosts(self.request)

        #
        # contacts
        #
        self.contact = Contact(self.request)
        self.contacts = Contacts(self.request)

        #
        # contact groups
        #
        self.contact_group = ContactGroup(self.request)
        self.contact_groups = ContactGroups(self.request)

        #
        # RBLs
        #
        self.rbl = RBL(self.request)
        self.rbls = RBLs(self.request)

        #
        # RBL profiles
        #
        self.rbl_profile = RBLProfile(self.request)
        self.rbl_profiles = RBLProfiles(self.request)

        #
        # Monitoring profiles
        #
        self.monitoring_profile = MonitoringProfile(self.request)
        self.monitoring_profiles = MonitoringProfiles(self.request)
