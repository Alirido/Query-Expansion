import requests

# 1. import text file
f = open("query-text.trec", "r")
if f.mode == "r":
    contents = f.readlines()
    queries = []
    for row in contents:
        if (row[0]!='<'):
            queries.append(row)

# 3. Hit API
headers = {
    "accept": "application/json"
}
for query in queries:
    parameters = {
        "text": query
    }
    response = requests.get("https://api.dbpedia-spotlight.org/en/spot", params=parameters, headers=headers)
    if (response.status_code == 200):
        print(response.json())
        data = response.json()
        highlighted_terms = {}
        if (not data["annotation"].get("surfaceForm")):
            print("SurfaceForm exist")
            for row in data["annotation"]["surfaceForm"]:
                highlighted_terms.append(row["name"])
            print(highlighted_terms)
        else:
            print("surfaceForm empty")
        print()
        
    else:
        print(response.status_code)


# 3a. Put the result words to set std