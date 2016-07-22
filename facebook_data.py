from facepy import GraphAPI
import json, os

FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']

graph = GraphAPI(FACEBOOK_ACCESS_TOKEN, version=2.7)

## Pulls all ratings ever, paginates through results, and prints a single json object

# rating_pages = graph.get('USAJOBS/ratings', page=True)

# print '['

# for page in rating_pages:
# 	print json.dumps(page["data"])[1:-1] + ','

# print ']'

## Pulls all posts to USAJOBS from Page Admins and editors

post_pages = graph.get('USAJOBS/posts', page=True)

print '['

for page in post_pages:
	print json.dumps(page["data"])[1:-1] + ','

print ']'
