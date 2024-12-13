#Formatted Output
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.4%}'.format(yes_votes, percentage))

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs} {count} {area}')
print(f'Debugging {bugs=} {count=} {area=}')

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))