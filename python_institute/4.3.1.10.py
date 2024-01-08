us_mile = 1609.344
us_gallon = 3.785411784

def liters_100km_to_miles_gallon(liters):
    miles = 100 / us_mile
    # print("100 km = ",miles," miles")
    gallon = liters / us_gallon
    # print(liters, "l =", gallon, " US Gallon")
    # print(miles/gallon * 1000)
    return miles/gallon * 1000

def miles_gallon_to_liters_100km(miles):
    km = miles * (us_mile /1000)
    print(miles,"miles = ", km, " km")
    liters = us_gallon / km
    return liters * 100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))