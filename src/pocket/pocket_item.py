'''
    item_id - A unique identifier matching the saved item. This id must be used to perform any actions through the v3/modify endpoint.
    resolved_id - A unique identifier similar to the item_id but is unique to the actual url of the saved item. The resolved_id identifies unique urls. For example a direct link to a New York Times article and a link that redirects (ex a shortened bit.ly url) to the same article will share the same resolved_id. If this value is 0, it means that Pocket has not processed the item. Normally this happens within seconds but is possible you may request the item before it has been resolved.
    given_url - The actual url that was saved with the item. This url should be used if the user wants to view the item.
    resolved_url - The final url of the item. For example if the item was a shortened bit.ly link, this will be the actual article the url linked to.
    given_title - The title that was saved along with the item.
    resolved_title - The title that Pocket found for the item when it was parsed
    favorite - 0 or 1 - 1 If the item is favorited
    status - 0, 1, 2 - 1 if the item is archived - 2 if the item should be deleted
    excerpt - The first few lines of the item (articles only)
    is_article - 0 or 1 - 1 if the item is an article
    has_image - 0, 1, or 2 - 1 if the item has images in it - 2 if the item is an image
    has_video - 0, 1, or 2 - 1 if the item has videos in it - 2 if the item is a video
    word_count - How many words are in the article
    tags - A JSON object of the user tags associated with the item
    authors - A JSON object listing all of the authors associated with the item
    images - A JSON object listing all of the images associated with the item
    videos - A JSON object listing all of the videos associated with the item
'''

__author__ = 'zxy'


class PocketItem(object):
    __item_id = 0
    __given_url = ''
    __excerpt = ''
    __resolved_title = ''

    def __init__(self, json_dict):
        print type(json_dict)
        self.__item_id = json_dict['item_id']
        self.__given_url = json_dict['given_url']
        self.__excerpt = json_dict['excerpt']
        self.__resolved_title = json_dict['resolved_title']

    def item_id(self):
        return self.__item_id

    def given_url(self):
        return self.__given_url

    def excerpt(self):
        return self.__excerpt

    def resolved_title(self):
        return self.__resolved_title

    def __str__(self):
        print type(self.excerpt())
        return self.__item_id + '\t' + self.given_url() + '\t' + self.excerpt()

