#get the ids
import json
#import urllib
import urllib2

from secret import key

key=key()

#import foursquare
#client = foursquare.Foursquare(
#    client_id=ClientID(), 
#    client_secret=ClientSecret()
#)


second =  0.00027 # just about 100 feet
min_lat =38.96001
max_lat =38.97265 
min_lon =-95.23603
max_lon =-95.23603

def main ():
    pos = min_lat
    while pos < max_lat :
        pos = pos + second
        url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=100&sensor=false&key=%s' % (pos,min_lon,key)
        
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://www.openlawrence.com/')
        r = urllib2.urlopen(req)
        print url
        data_raw = r.read()
        print data_raw
#        data = json.loads(data_raw)
#        print data


main()
