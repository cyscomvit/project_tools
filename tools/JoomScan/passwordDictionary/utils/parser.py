def parse(input):
	if type(input) == str:
		return {"status":True}
	else:
		return {"status":False,"error":"input type not valid"}