from Cache import Cache
import sys

parameters = sys.argv[1].split(':')
cache = Cache(int(parameters[0]),int(parameters[1]),int(parameters[2]))
file = open(sys.argv[2], 'r')
in_address = file.readlines()
i = 0
for address in in_address:
	cache.get(address)
	i += 1
	if i % 10000 == 0:
		print('Processing...')
cache.statistic()
file.close()