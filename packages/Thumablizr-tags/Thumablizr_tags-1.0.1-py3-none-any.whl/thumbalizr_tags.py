# -*- coding: utf-8 -*-
# Copyright 2019 Julien Sobrier
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django import template
from django.template.defaultfilters import stringfilter

from settings import USER_SETTINGS
from thumbalizr import Thumbalizr

register = template.Library()

client = Thumbalizr(USER_SETTINGS['API_KEY'], USER_SETTINGS['SECRET'])



@register.filter
@stringfilter
def thumbalizr(url, width=''):
    """ Generate the URL of the Thumbalizr image

        Arguments:
             width: the width of the thumbnail
    """
    return client.url(url, {
      'bwidth': USER_SETTINGS['BWIDTH'], 'width': width or USER_SETTINGS['WIDTH'],
      'bheight': USER_SETTINGS['BHEIGHT'], 'height': USER_SETTINGS['HEIGHT'],
      'size': USER_SETTINGS['SIZE'], 'country': USER_SETTINGS['COUNTRY'], 'delay': USER_SETTINGS['DELAY']
    }); 
