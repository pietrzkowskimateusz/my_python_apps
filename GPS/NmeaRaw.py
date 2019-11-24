import pynmea2
import utm
import math


def distance(pos1, pos2):
    print("P1:", pos1)
    print("P2:", pos2)
    x = math.pow(pos1[0] - pos2[0], 2)
    y = math.pow(pos1[1] - pos2[1], 2)
    z = math.sqrt(x+y)
    print("X:",x)
    print("Y:",y)
    print("Z:",z)
    return z


nmea = '$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
nmeaObj = pynmea2.parse(nmea)
for i in range(len(nmeaObj.fields)):
    print(nmeaObj.fields[i][1], '\t', nmeaObj.data[i])
print(nmeaObj.sentence_type)
# loc = (nmeaObj.latitude, nmeaObj.longitude)
loc = (51.535543, 19.625121)
print("Loc1:",loc)
newPositionInUtm = utm.from_latlon(loc[0], loc[1])
print("Position1:",newPositionInUtm)
Point1 = (newPositionInUtm[0], newPositionInUtm[1])

# position1 = (1,4)
# position2 = (-4,6)
# print(distance(position1,position2))

nmea2 = '$GPGGA,123519,4807.048,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*40'
nmeaObj2 = pynmea2.parse(nmea2)
# loc2 = (nmeaObj2.latitude, nmeaObj2.longitude)
loc2 = (51.535102, 19.625583)
print("Loc2:",loc2)
newPositionInUtm2 = utm.from_latlon(loc2[0], loc2[1])
print("Position2:",newPositionInUtm2)
Point2 = (newPositionInUtm2[0], newPositionInUtm2[1])

print("---------------")
print("Distance:", distance(Point1, Point2))
