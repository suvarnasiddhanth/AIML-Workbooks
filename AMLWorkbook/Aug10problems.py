def create_handle(uid, bank_id):
	return (uid, bank_id)
def read_id(upihandle):
	return upihandle[0]
def read_bank_id(upihandle):
	return upihandle[1]

class upitx:
	def __init__(self, source_handle, reciever_handle, amount):
		# self.tx_id = ???
		# self.sender = sender
		# self.reciever = reciever
		# self.amount = amount
		...
class upipaymentstx(upitx):
	def __init__(self, source_handle, reciever_handle, amount):
		...
class upireciepttx(upitx):
	def __init__(self, source_handle, reciever_handle, amount):
		...

print(read_id(create_handle(9741001590,"hdfc")))