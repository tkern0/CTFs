"""
This problem isn't really that much of a challenge when you have built in timezone handling - or so
 I thought
I still don't really know what I was doing wrong but I kept getting runtime errors
I ended up somewhat abusing the verification system to try work out where these errors were, hence
 my 14 attempts (and I still solved it first :D )
I would put a block of code into a try/except, print the sample answer if it errored, else nothing
If it solved the sample question then I knew that block errored, if it printed nothing then that
 would be shown on the submission as a different error, so I knew my code didn't error, and if there
 was still a runtime error then I knew I had the wrong error type
"""

from sys import stdin
from datetime import *

dep_name = stdin.readline()[:-1]
mon, day, dep_time = stdin.readline()[:-1].split(" ")
dep_zone = stdin.readline()[:-1]
dest_name = stdin.readline()[:-1]
dest_zone = stdin.readline()[:-1]
flight_time = stdin.readline()[:-1]

def convertZoneString(zone):
	if zone == "00:00":
		return timedelta()
	multi = 1 if zone[0] == "+" else -1
	h, m = zone[1:].split(":")
	return timedelta(hours=multi * int(h), minutes=multi * int(m))

def convertTimeString(t):
	h, m = t.split(":")
	return datetime(year=2019, month=9, day=7, hour=int(h), minute=int(m))

def convertTimeDelta(t):
	h, m = t.split(":")
	return timedelta(hours=int(h), minutes=int(m))


dep_tz = convertZoneString(dep_zone)
dest_tz = convertZoneString(dest_zone)
tz_diff = dest_tz - dep_tz

dep_dt = convertTimeString(dep_time)
flight_td = convertTimeDelta(flight_time)
arrival_dt = dep_dt + flight_td + tz_diff


same_day = "same" if dep_dt.day == arrival_dt.day else "following"
time_str = f"{arrival_dt.hour:0>2}:{arrival_dt.minute:0>2}"

print("Departs " + dep_name + " " + mon + " " + day + " " + dep_time)
print("Arrives " + dest_name + " " + time_str + " " + same_day + " day")
