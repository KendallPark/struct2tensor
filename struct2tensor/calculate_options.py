# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Set options for struct2tensor.

This object can be passed to several methods. It is passed
as an argument to calculate, get_sparse_tensor, and get_ragged_tensor.

"""

from __future__ import absolute_import
from __future__ import division

from __future__ import print_function


class Options(object):
  """Options for calculate functions.

  Do not construct Options directly. The preferred method of creating an object
  is calling get_default_options() or get_options_with_minimal_checks() below.
  Any fine-tuning can be done by modifying the properties of the Options object
  after creation.

  When a method takes an optional Options object but none is provided, it will
  replace it with get_default_options() .

  """

  def __init__(self, ragged_checks, sparse_checks):
    """Create options."""
    self.ragged_checks = ragged_checks
    self.sparse_checks = sparse_checks

  def __str__(self):
    return ("{ragged_checks:" + str(self.ragged_checks) + ", sparse_checks: " +
            str(self.sparse_checks) + "}")


def get_default_options():
  """Get the default options."""
  return Options(ragged_checks=True, sparse_checks=True)


def get_options_with_minimal_checks():
  """Options for calculation with minimal runtime checks."""
  return Options(ragged_checks=False, sparse_checks=False)
