import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import geocoder

file = raw_input("Specify source filepath:")

f = open(file, 'r')

output = open('output.csv', 'w')
output.write("\address\",\"lon\",\"lat\",\"matchcode\" \n")

for line in f:
	gc = geocoder.osm(line)
	newaddr = gc.address.replace(',','')
	output.write(newaddr + ',' + str(gc.lat) + ',' + str(gc.lng) + ',' + str(gc.accuracy) + '\n')
output.close
f.close