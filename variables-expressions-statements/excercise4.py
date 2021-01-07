'''
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
'''
start_time = 6+52/60
easy_pace_time = (8+15/60)/60
tempo_pace_time = (7+12/60)/60
running_time = 2*easy_pace_time + 3*tempo_pace_time
breakfasttime_hr = start_time + running_time
print(breakfasttime_hr)