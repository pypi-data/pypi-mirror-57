# Copyright 2015 IBM Corp.
#
# All Rights Reserved.
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

"""Wrappers used for multiple types of PCM data."""


class Info(object):

    def __init__(self, utilInfo):
        self.version = utilInfo.get('version')
        self.metric_type = utilInfo.get('metricType')
        self.monitoring_type = utilInfo.get('monitoringType')
        self.mtms = utilInfo.get('mtms')
        self.name = utilInfo.get('name')
