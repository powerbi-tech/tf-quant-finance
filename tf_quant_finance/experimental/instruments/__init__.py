# Lint as: python3
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Instruments."""

from tf_quant_finance.experimental.instruments import eurodollar_futures
from tf_quant_finance.experimental.instruments import forward_rate_agreement
from tf_quant_finance.experimental.instruments import rate_curve
from tf_quant_finance.experimental.instruments import rates_common
from tensorflow.python.util.all_util import remove_undocumented  # pylint: disable=g-direct-tensorflow-import

EurodollarFutures = eurodollar_futures.EurodollarFutures
ForwardRateAgreement = forward_rate_agreement.ForwardRateAgreement
RateCurve = rate_curve.RateCurve
InterestRateMarket = rates_common.InterestRateMarket
DayCountBasis = rates_common.DayCountBasis

_allowed_symbols = [
    'EurodollarFutures',
    'ForwardRateAgreement',
    'RateCurve',
    'InterestRateMarket',
    'DayCountBasis',
]

remove_undocumented(__name__, _allowed_symbols)
