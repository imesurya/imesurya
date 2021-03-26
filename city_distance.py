from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0


input1 = input('City 1:')
input2 = input('City 2:')

proc_input1 = input1.split(',')
proc_input2 = input2.split(',')

lat1 = radians(float((proc_input1[0].split(' ')[0])))
lon1 = radians(float((proc_input1[1].split(' ')[1])))
lat2 = radians(float((proc_input2[0].split(' ')[0])))
lon2 = radians(float((proc_input2[1].split(' ')[1])))

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Output: City 1 and City 2 are "+str(distance)+" km apart" )