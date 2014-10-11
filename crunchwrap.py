import json
import urllib2
import urllib


def geocodeAddress(address):
	request_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+urllib.quote(str(address))+'&sensor=false'
	req = urllib2.Request(request_url)
 	results = urllib2.urlopen(req)
	jsonresults = json.loads(results.read())
	lat = jsonresults['results'][0]['geometry']['location']['lat']
	lng = jsonresults['results'][0]['geometry']['location']['lng']
	return lat,lng
	

	
def getStores(lat,lng): 
	request_url = 'http://www.tacobell.com/storelocatorjson/BsdsJSONHandler.ashx'
	data = json.dumps({"id":0,"method":"findNearbyStores","params":{ "latitude" : lat, "longitude" : lng, "distance" : 25 }})
	req = urllib2.Request(request_url, data, {'Content-Type': 'application/json'})
	stores = urllib2.urlopen(req)
	return json.loads(stores.read())
	

def getStoresByAddress(address):
	lat,lng = geocodeAddress(address)
	return getStores(lat,lng)

if __name__ == "__main__":
	print getStoresByAddress('long island city')
