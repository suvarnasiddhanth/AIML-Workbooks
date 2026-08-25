class ListNode:
	def __init__(self, val: int):
		self.value = val
		self.next = None
def nomatchmsg(flag):
	if flag == 0:
		print("\nNo match found\n")
def insertnode(val: int, head):
	newNode = ListNode(val)
	newNode.next = head
	return newNode
def traverse(val, head):
	curr = head
	prev = None
	flag = 0
	while curr != None:
		if curr.value == val:
			flag = 1
			return curr, prev
		prev = curr
		curr = curr.next
	nomatchmsg(flag)
	return None, None
def insertafterfirstfoundnode(insertval: int, val: int, head):
	curr, prev = traverse(val, head)
	if curr != None:
		temp=insertnode(insertval,head)
		temp.next=curr.next
		curr.next = temp
# Below doesn't work rn, fix later
#def insertafterlastfoundnode(insertval: int, val: int, head):
#	curr, prev = traverse(val, head)
#	while curr != None:
#		newcurr = curr
#		newprev = prev
#		curr, prev=traverse(val, curr.next)
#	temp=insertnode(insertval,head)
#	temp.next=newcurr.next
#	newcurr.next = temp
def popnode(head):
	nextnode = head
	head = nextnode.next
	return head
def displaylist(head):
	end = head
	while end != None:
		print("",end.value)
		print("_|_")
		end = end.next
	print("End")
def traverse_till_hit(val: int, head):
	end = head
	flag=0
	while end != None:
		if end.value == val:
			print("",end.value,"<---")
			flag=1
		else:
			print("",end.value)
		print("_|_")
		end = end.next
	print("End")
	nomatchmsg(flag)
def deletefirstfoundnode(val: int, head):
		curr, prev = traverse(val, head)
		traverse_till_hit(val, head)
		flag=0
		if curr != None:
			prev.next = curr.next
			print(curr.value,"deleted.")
			flag=1
			return
		prev=curr			
		curr = curr.next
		print("End")
		nomatchmsg(flag)
def deletelastfoundnode(val: int, head):
		curr = head
		lastmatch=None
		prev=None
		traverse_till_hit(val, head)
		flag=0
		while curr != None:
			if curr.value == val:
				lastmatch=curr
				lastmatchprev=prev
				flag=1 if flag != 1 else flag
			prev=curr
			curr = curr.next
		nomatchmsg(flag)
		if flag == 1:
			lastmatchprev.next = lastmatch.next
def deleteallnode(val: int, head):
		curr = head
		prev=None
		traverse_till_hit(val, head)
		flag=0
		while curr != None:
			if curr.value == val:
				prev.next = curr.next
				print(curr.value,"deleted.")
				flag=1
			prev=curr			
			curr = curr.next
		print("End")
		nomatchmsg(flag)
head = None
head = insertnode(5, head)
head = insertnode(7, head)
head = insertnode(6, head)
head = insertnode(7, head)
#head = popnode(head)
head = insertnode(8,head)
#displaylist(head)
#deleteallnode(7,head)
#deletelastfoundnode(7,head)
#traverse_till_hit(5,head)
#insertafterlastfoundnode(2,7,head)
displaylist(head)