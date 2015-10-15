import json
import httplib2
from collections import OrderedDict
from pocket.pocket_item import PocketItem


class Retrieve(object):

    @staticmethod
    def parse_json(json_str):
        decoded = json.loads(json_str, object_pairs_hook=OrderedDict)
        return [PocketItem(d) for d in decoded['list'].itervalues()]

    def get_item_list(self):
        http_conn = httplib2.Http(proxy_info=httplib2.proxy_info_from_environment())
        uri = 'https://getpocket.com/v3/get'
        method = 'POST'
        headers = {'Content-Type': 'application/json'}
        body = '''{"consumer_key": "46666-60a7a1a006160f5641381067",
                "access_token": "40cb85d8-a3b9-fa64-3f74-b88315",
                "count": "2",
                "detailType": "simple"}'''

        # print 'Start connection...'
        resp, content = http_conn.request(uri=uri, method=method, headers=headers, body=body)
        # print 'Request over.'
        if resp.status != 200:
            # print resp
            return None
        return self.parse_json(content)

    def get_all_items(self):
        http_conn = httplib2.Http(proxy_info=httplib2.proxy_info_from_environment())
        uri = 'https://getpocket.com/v3/get'
        method = 'POST'
        headers = {'Content-Type': 'application/json'}
        body = '''{"consumer_key": "46666-60a7a1a006160f5641381067",
                    "access_token": "40cb85d8-a3b9-fa64-3f74-b88315",
                    "detailType": "simple"}'''

        try:
            resp, content = http_conn.request(uri=uri, method=method, headers=headers, body=body)
        except Exception, e:
            # print e
            return None
        if resp.status != 200:
            # print resp
            return None
        # print 'success'
        return self.parse_json(content)
