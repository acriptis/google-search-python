# site:wikipedia.org Когда родился Пушкин?
from google_search import GoogleCustomSearch


# SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
SEARCH_ENGINE_ID = "005711384174884746282:l1hoqyznj4a"
# API_KEY = os.environ['GOOGLE_CLOUD_API_KEY']
API_KEY = "AIzaSyBknezKiE9xznOQ1ZsWry5K-s1IdfK_Rwc"

api = GoogleCustomSearch(SEARCH_ENGINE_ID, API_KEY)
import ipdb; ipdb.set_trace()

for result in api.search("Когда родился Пушкин?"):
    print("*"*80)
    print("Title")
    print(result['title'])
    print('link')
    print(result['link'])
    print('snippet')
    print(result['snippet'])

