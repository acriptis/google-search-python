import os
from google_search import GoogleCustomSearch

# define environmental variables:
try:
    SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
except Exception as e:
    print("Missed Environmental variable SEARCH_ENGINE_ID. "
          "Retrieve Search Engine ID at https://cse.google.com/")
    raise e

try:
    API_KEY = os.environ['GOOGLE_CLOUD_API_KEY']
except Exception as e:
    print("Missed Environmental variable GOOGLE_CLOUD_API_KEY. "
          "Retrieve GOOGLE_CLOUD_API_KEY at "
          "https://developers.google.com/custom-search/v1/introduction")

    raise e

api = GoogleCustomSearch(SEARCH_ENGINE_ID, API_KEY)

# sample output
for result in api.search("Когда родился Пушкин?"):
    print("*"*80)
    print("Title")
    print(result['title'])
    print('link')
    print(result['link'])
    print('snippet')
    print(result['snippet'])

