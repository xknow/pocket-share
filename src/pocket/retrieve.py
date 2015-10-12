import json
import httplib2
from collections import OrderedDict
from pocket.pocket_item import PocketItem

class Retrieve(object):

    def parse_json(self, json_str):
        decoded = json.loads(json_str, object_pairs_hook=OrderedDict)
        return [PocketItem(d) for d in decoded['list'].itervalues()]

    def get_item_list(self):
        http_conn = httplib2.Http()
        uri = 'https://getpocket.com/v3/get'
        method = 'POST'
        headers = {'Content-Type': 'application/json'}
        body = {"consumer_key": "46666-60a7a1a006160f5641381067",
                "access_token": "40cb85d8-a3b9-fa64-3f74-b88315",
                "count": "10",
                "detailType": "simple"}

        print 'Start connection...'
        resp, content = http_conn.request(uri=uri, method=method, headers=headers, body=body)
        print 'Request over.'
        return self.parse_json(content)