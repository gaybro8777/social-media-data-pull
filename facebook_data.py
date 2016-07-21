from facepy import GraphAPI
import json

ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']

graph = GraphAPI(ACCESS_TOKEN, version=2.7)
pages = graph.get('204902959720/ratings', page=True)

print '['

for page in pages:
	print json.dumps(page["data"])[1:-1] + ','

print ']'
