#!/usr/bin/env python

import xml.etree.ElementTree as ET
import urllib2
import json
from cookielib import CookieJar
import os
import errno

def download_images_from_codecombat():
    headers = {'User-Agent': 'Code Combat Thang Downloader/0.1'}
    cookie_jar = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    urllib2.install_opener(opener)

    # Cookies need to be set properly to load the search page, so we make a request to their thang editor first
    request = urllib2.Request('http://codecombat.com/editor/thang', None, headers)
    urllib2.urlopen(request)

    request = urllib2.Request('http://codecombat.com/db/thang.type/search?project=true', None, headers)
    page_contents = urllib2.urlopen(request).read()
    parsed_page_contents = json.loads(page_contents)


    root_directory = os.path.dirname(os.path.realpath(__file__))
    for sprite_information in parsed_page_contents:
        url_on_codecombat = 'http://codecombat.com/file/db/thang.type/{}/portrait.png'.format(sprite_information['original'])
        file_path = os.path.join(root_directory, 'thangs/{}/'.format(sprite_information['kind']).lower())
        filename_to_save = os.path.join(file_path, '{}.png'.format(sprite_information['slug']))
        try:
            os.makedirs(file_path)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(file_path):
                pass
            else:
                raise

        request = urllib2.Request(url_on_codecombat, None, headers)
        if not os.path.exists(filename_to_save):
            with open(filename_to_save, 'wb') as f:
                try:
                    f.write(urllib2.urlopen(request).read())
                except urllib2.HTTPError:
                    # TODO maybe log?
                    pass
            print "Saved {}".format(filename_to_save)
        else:
            print "File {} already exists!".format(filename_to_save)

if __name__ == '__main__':
    download_images_from_codecombat()