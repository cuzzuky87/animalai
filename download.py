from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
from os.path import join, dirname
from dotenv import load_dotenv

# APIキーの情報
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
FLICKR_API_KEY = os.environ.get("FLICKR_API_KEY")
FLICKR_API_SECRET_KEY = os.environ.get("FLICKR_API_SECRET_KEY")
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET_KEY, format='parsed-json')
result = flickr.photos.search(
    text=animalname,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q,licence'
)

photos = result['photos']

for photo_num, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + "/" + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
