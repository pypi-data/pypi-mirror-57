# Copyright 2019 Francesco Ceccon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Collects variables from logs and saves them to csv for later analysis."""

from argparse import ArgumentParser

import pandas as pd

from galini_io.reader import MessageReader


def main():
    parser = ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('output')
    args = parser.parse_args()

    records = []
    with open(args.filename, 'rb') as f:
        reader = MessageReader(f, stream=False)

        for msg in reader:
            if not msg.HasField('update_variable'):
                continue

            update_variable = msg.update_variable
            record = {
                'module': msg.name,
                'run_id': msg.run_id,
                'timestamp': msg.timestamp,
                'variable': update_variable.name,
                'value': update_variable.value,
            }

            for idx, iteration in enumerate(update_variable.iteration):
                record['iteration_{}'.format(idx)] = iteration

            records.append(record)

    data = pd.DataFrame.from_records(records)
    data.to_csv(args.output, index=False)
