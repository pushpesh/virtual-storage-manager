#  Copyright 2014 Intel Corporation, All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Server interface (1.1 extension).
"""

import urllib
from vsmclient import base

class PerformanceMetrics(base.Resource):
    """A vsm is an extra block level storage to the OpenStack instances."""
    def __repr__(self):
        return "<PerformanceMetrics: %s>" % self.id

    def delete(self):
        """Delete this vsm."""
        self.manager.delete(self)

    def update(self, **kwargs):
        """Update the display_name or display_description for this vsm."""
        self.manager.update(self, **kwargs)

    def force_delete(self):
        """Delete the specified vsm ignoring its current state.

        :param vsm: The UUID of the vsm to force-delete.
        """
        self.manager.force_delete(self)

class PerformanceMetricsManager(base.ManagerWithFind):
    """
    Manage :class:`Server` resources.
    """
    resource_class = PerformanceMetrics

    def list(self, search_opts=None):
        """
        Get a list of .
        """
        if search_opts is None:
            search_opts = {}

        qparams = {}

        for opt, val in search_opts.iteritems():
            if val:
                qparams[opt] = val

        query_string = "?%s" % urllib.urlencode(qparams) if qparams else ""

        ret = self._list("/performance_metrics/get_list%s" % (query_string),"performance_metrics")
        return ret

    def get_iops_or_width(self, search_opts=None):
        """
        Get a list of .
        """
        if search_opts is None:
            search_opts = {}

        qparams = {}

        for opt, val in search_opts.iteritems():
            if val:
                qparams[opt] = val

        query_string = "?%s" % urllib.urlencode(qparams) if qparams else ""

        ret = self._list("/performance_metrics/get_iops_or_banwidth%s" % (query_string),"performance_metrics")
        return ret

    def get_lantency(self, search_opts=None):
        """
        Get a list of .
        """
        if search_opts is None:
            search_opts = {}

        qparams = {}

        for opt, val in search_opts.iteritems():
            if val:
                qparams[opt] = val

        query_string = "?%s" % urllib.urlencode(qparams) if qparams else ""

        ret = self._list("/performance_metrics/get_lantency%s" % (query_string),"performance_metrics")
        return ret


