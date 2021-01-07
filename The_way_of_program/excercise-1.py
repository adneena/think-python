'''
If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).
'''
distKm = 10.0
distMi = (distKm * (1.0 / 1.61))  #distance in miles
seconds = ((43.0 * 60.0) + 30.0)
hours = (43.5 / 60.0)


def timePerMile(distMi, seconds):
    seconds_per_mile = seconds / distMi,
    print('seconds per mile:', seconds_per_mile)


def avgSpeed(distMi, hours):
    miles_per_hour = distMi / hours
    print('miles per hour:', miles_per_hour)

 
timePerMile(distMi, seconds)
avgSpeed(distMi, hours)