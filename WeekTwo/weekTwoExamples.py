from datetime import datetime, date, time
from platform import java_ver

# UNIX Time starts at midnight January 1st 1970 and is the seconds since that time.

# datetime - for instances in time
# date - for calander date
# time - for time regardless of day
today = date.today()
print(today)

tomorrow = date(2020, 8, 19)
print(tomorrow)

next_week = date.fromisoformat('2020-08-24')
print(next_week)

right_now = datetime.now()
print(right_now)

print(right_now.timestamp())

# Time stamps are useful for storing dates in a database or storing logging information.
my_date = datetime.fromtimestamp(14581293912)
print(my_date)

# Sets

cats = set() # creates an empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)

cats.add('Cheetah')

print(cats)

birds = { 'owl', 'robin',  'swan'}

print(birds)
birds.add('robin') # does not add a second copy of robin
print (birds)

birds.remove('owl')
birds.add('cardinal')
print(birds)

# can convert lists into sets and it will automatically remove duplicates

bird_list = ['robin','swan','swan','eagle','cardinal','swan','robin']
# Will lose order, so need to resort if order maters
bird_list_no_dupes = list(set(bird_list))
print(bird_list_no_dupes)