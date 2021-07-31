def parse(port,type_scan):
	print(port,type_scan)
	if type(port) == str and port > 0 and port <= 65535 and type_scan in ['1','2','3','4','5']:
		return { "status":True }
	else:
		return {"status":False, "payload":"input is invalid" }