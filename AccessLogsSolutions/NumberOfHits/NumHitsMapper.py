import sys

for line in sys.stdin:
	data = line.strip().split(" ")

	if len(data) == 10:
		ip , identity, username, time, timezone , requestType, requestTo , protocolversion , status, size = data
		print requestTo.strip()