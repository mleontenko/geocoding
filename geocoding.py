import geocoder

gc = geocoder.osm('Dore Pfanove 11 ZAgreb')
print gc.latlng
print gc.accuracy
print gc.address
