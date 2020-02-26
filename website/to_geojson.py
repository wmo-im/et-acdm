# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2019 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import csv
import io
import json

dict_ = {
    'type': 'FeatureCollection',
    'features': []
}

with io.open('members.csv') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        if row['url'] == '':
            url = None
        else:
            url = '<a target="_member" href="{}">{}</a>'.format(row['url'], row['wdc'])
        dict_['features'].append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [float(row['long']), float(row['lat'])]
            },
            'properties': {
                'member': row['member'],
                'role': row['role'],
                'wdc': row['wdc'],
                'url': url,
                'affiliation': row['affiliation'],
                'location': row['location']
            }
        })

print(json.dumps(dict_, ensure_ascii=False, indent=4))
