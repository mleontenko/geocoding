import geocoder

file = raw_input("Specify source filepath:")

f = open(file, 'r')

for line in f:
	print line

#gc = geocoder.osm('Dore Pfanove 11 ZAgreb')
#print gc.latlng
#print gc.accuracy
#print gc.address
