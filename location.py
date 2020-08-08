import geocoder
import math
from virus_stats_with_api import statistics
#ul.three-column li
class Location:
    def __init__(self):
        pass
    def get_user_location(self):
        g = geocoder.ip('me')
        self.user_location = g.latlng
    def find_loc(self, city):
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(city + " California")
        self.citylatitude = location.raw['lat']
        self.citylongitude = location.raw['lon']
    def get_statistics(self):
        a = statistics()
        a.request_api()
        self.stats = a.parse_response()
        #print(self.stats)
    def compare_location(self):
        for entry in self.stats:
            if entry['confirmed'] >= 10000:
                self.find_loc(entry['county_name'])
                if math.sqrt((abs(float(self.citylatitude)-float(self.user_location[0])))**2+(abs(float(self.citylongitude)-float(self.user_location[1])))**2)<=1:
                    print('Alert, you are near a placer with a lot of coronavirus cases: ',entry['county_name'])
                    return ''
        print('You are safe.')

        #print(self.user_location[0],self.user_location[1])





l = Location()
l.get_user_location()
l.find_loc('Los Angeles')
l.get_statistics()

l.compare_location()
