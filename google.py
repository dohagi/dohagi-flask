from googleapiclient.discovery import build

Google_API_KEY = "AIzaSyBe0A59NBLpkNtW5kqCmmZ_m5tm-zrDWKE"
Google_CSE_ID = "001421750801758554529:d658quydjmi"

""" If we use flask,
>>> def add_routes(app):
...     app.route("/api/getReview/")(search)
"""
def search(query):
    service = build("customsearch", "v1", developerKey = Google_API_KEY)
    results = service.cse().list(q=query, cx=Google_CSE_ID).execute()
    links = []
    #print(results)
    try:
        for result in results['items']:
            links.append(result['link'])
    except Exception:
        pass
    return links
