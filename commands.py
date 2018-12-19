import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# This is intended to form a conglomearte of possible commands 
# to open my applications on my Mac
d = "/Applications"
records = []
apps = os.listdir(d)
print(apps)

# goes through the list of apps I have on my Mac
# and matches them with their execution commands and
# then stored in elastic search.

for app in apps:
	record = {}
	record['voice_command'] = 'open' + app.split('.app')[0]
	record['sys_command'] = ' open ' +d +'/%s.app' %app.replace(' ','\ ')
	records.append(record)

# open the elastic search client
es = Elasticsearch(['localhost:9200'])
if es.ping():
	print("Connected to elastic search")
bulk(es, records, index = "voice_over", doc_type="text",
	raise_on_error=True)

# performs a query pf the nodes in the elastic search
# and matches up an execution command
def search_es(query):
    res = es.search(index="voice_over", doc_type="text", body={                     
    "query" :{
        "match": {
            "voice_command": {
                "query": query,
                "fuzziness": 2
            }
            }
        },
    })
    print("this is the source" )
    return res['hits']['hits'][0]['_source']['sys_command']
