import datetime as date

#Manually construct a block with
#index zero and arbitrary previous hash
def create_genesis_block():
	return Block(0, date.datetime.now(), "Genesis Block", "0")
	
	
