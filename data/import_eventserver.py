"""
Import sample data for classification engine
"""

import predictionio
import csv
import argparse

def import_events(client, file):
	count = 0
	with open(file, 'rb') as f:
		reader = csv.DictReader(f)
		print "Importing data..."
		for row in reader:
			plan = row['categorie'] 
			text = row['text']
			label = row['label']
			print plan,',',text,label
			client.create_event(
			event="documents",
			entity_type="source",
			entity_id=str(count), # use the count num as user ID
			properties= {
			"text" : text,
			"category" : plan,
			"label" : float(label)
			}
			)
			count += 1
	f.close()
	print "%s events are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for classification engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/Twitter140sample.txt")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
