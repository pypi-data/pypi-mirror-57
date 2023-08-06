import re
import json
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import requests

site_url = 'https://www.metal-archives.com/'
url_search_songs = 'search/ajax-advanced/searching/songs?'
url_lyrics = 'release/ajax-view-lyrics/id/'
lyrics_not_available = '(lyrics not available)'
lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
band_name_re = re.compile(r'title="(?P<name>.*)\"')
tags_re = re.compile(r'<[^>]+>')

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def get_songs_data(band_name, song_title):
    """Search on metal-archives for song coincidences"""
    params = dict(bandName=band_name, songTitle=song_title)
    url = site_url + url_search_songs + urlencode(params)

    return json.load(urlopen(Request(url, headers=hdr)))['aaData']


def get_lyrics_by_song_id(song_id):
    """Search on metal-archives for lyrics based on song_id"""
    url = site_url + url_lyrics + song_id
    return tags_re.sub('', urlopen(Request(url, headers=hdr)).read().strip().decode())


def iterate_songs_and_print(songs):
    '''Iterate over returned song matches. If the lyrics are different than\
    "(lyrics not available)" then break the loop and print them out.\
    Otherwise the last song of the list will be printed.'''
    for song in songs:
        band_name = band_name_re.search(song[0]).group("name")
        song_title = song[3]
        song_id = lyric_id_re.search(song[4]).group("id")
        lyrics = get_lyrics_by_song_id(song_id)
        if lyrics != lyrics_not_available:
            break

    return lyrics


# ----------------------------------------------------------------------
def get_lyrics(artist, album, title):
    """"""
    songs_data = get_songs_data(artist, title)

    if len(songs_data):
        return iterate_songs_and_print(songs_data)
    else:
        return None

