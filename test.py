existing = {"user" : {"username": "test", "aura": 0}}
new = {"user1" : {"username": "emil", "aura": 0}}
for key, value in new.items():
	existing[key] = value
	for k,v in value.items():
		existing[key][k] = v

print(existing)
