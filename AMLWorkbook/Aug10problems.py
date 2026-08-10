def create_handle(uid, bank_id):
	return (uid, bank_id)
def read_id(uh):
	return uh[0]
def read_bank_id(uh):
	return uh[1]
print(read_id(create_handle(9741001590,"hdfc")))