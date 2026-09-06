"""Checklist											Completed
	1. 			Display list								✓
		1.1 	Display list in reverse  					✓
	2. 			Insert					  					✓
		2.1 	Insert at the beginning 					✓
		2.1.1 	Insert bulk at the beginning 				✓
		2.2 	Insert at the end			 				✓
		2.2.1 	Insert bulk at the end						✓
		2.3 	Insert after given value					✓
		2.3.1 	Insert bulk after given value				✓
		2.4 	Insert after given value (reverse search)	✓
		2.4.1 	Insert bulk after given value				✓
		2.5		Insert at position							✓
	3. 			Pop											✓
		3.1 	Pop from the beginning						✓
		3.2 	Pop from the end							✓
		3.3		Pop specified value							✓
		3.3.1	Pop specified value (reverse search)		✓
		3.4		Pop all instance of specified value			✓
	4. 			Traverse									✓
		4.1		Traverse from the beginning					✓
		4.2		Traverse from the end						✓


"""
import inspect
size = 0
debug = 0
head = None
tail = None
class ListNode:
	def __init__(self, val: int, nextnode=None, prevnode=None):
		self.value = val
		if nextnode != None:
			nextnode.prev = self
			self.next = nextnode
		else:
			self.next = None
		if prevnode != None:
			prevnode.next = self
			self.prev = prevnode
		else:
			self.prev =None
def DebugPrint(nodepointer, loc=0):
	nodenext = nodepointer.next
	nodeprev = nodepointer.prev
	if loc == -1:
		try:
			print(f"Prev: {nodeprev.value:5} <-- {nodepointer.value}")
		except AttributeError:
			print("AttributeError when checking prev value.")
	elif loc == 1:
		try:
			print(f"Next:\t\t{nodepointer.value} --> {nodenext.value}")
		except AttributeError:
			print("AttributeError when checking next value.")
	else:
		try:
			print("Curr:\t   ", nodepointer.value)
		except AttributeError:
			print("AttributeError when checking current node value.")
def NoMatchMsg(flag):
	if flag == 0:
		print("\nNo match found\n")
def sizeincrement():
	global size
	size += 1
def sizedecrement():
	global size
	size -= 1
def assignhead(node):
	global head
	head = node
def assigntail(node):
	global tail
	tail = node
#Function to add node before specified node
def InsertNodeBefore(val: int, before=None):
	global head, tail
	#If no node is passed, take head as default value
	before = head if before is None else before
	#If first arg is not None or the head, take note of the prev node
	if before!=None and before.prev !=None: previous=before.prev
	else: previous = None    #Required?
	newNode = ListNode(val, before, previous)
	if head == None or newNode.next == head: assignhead(newNode)
	if tail == None: assigntail(newNode)
	if debug: 
		DebugPrint(before, -1)
		DebugPrint(before, 1)
	sizeincrement()
	return newNode
#Funttion to add node after specified node
def InsertNodeAfter(val: int, after=None):
	global head, tail
	after = tail if after is None else after
	if after!=None and after.next !=None: nextnode=after.next
	else: nextnode = None
	newNode = ListNode(val, nextnode, after)
	if head == None: assignhead(newNode)
	if tail == None or newNode.prev == tail: assigntail(newNode)
	if debug: 
		DebugPrint(tail, -1)
		DebugPrint(tail, 1)
	sizeincrement()
	return newNode
#Traverse list till required value is found
def traverse(val):
	global head
	curr = head
	flag = 0
	while curr != None:
		if curr.value == val:
			flag = 1
			return curr
		curr = curr.next
	NoMatchMsg(flag)
	return None
def traverseReverse(val):
	global tail
	curr = tail
	flag = 0
	while curr != None:
		if curr.value == val:
			flag = 1
			return curr
		curr = curr.prev
	NoMatchMsg(flag)
	return None
def InsertNodeAfterGivenValue(insertval, val, checkfromend=None):
	curr = traverse(val) if checkfromend == None else traverseReverse(val)
	if debug == 1: DebugPrint(curr)
	if curr != None:
		if type(insertval) == int:
			InsertNodeAfter(insertval, curr)
		else:
			InsertMultipleNode(insertval, 'End', -1, curr)
def InsertNodeBeforeGivenValue(insertval, val, checkfromend=None):
	curr = traverse(val) if checkfromend == None else traverseReverse(val)
	if debug == 1: DebugPrint(curr)
	if curr != None:
		if type(insertval) == int:
			InsertNodeBefore(insertval, curr.prev)
		else:
			InsertMultipleNode(insertval, 'Start', -1, curr)
def PopNode(node):
	global head
	if node == None:
		print("Emply list, nothing to pop.")
		return
	elif type(node) != type(head):
		print("Invalid argument for pop.")
		return
	prevnode = node.prev
	nextnode = node.next
	if prevnode != None:
		prevnode.next = nextnode
	if nextnode != None:
		nextnode.prev = prevnode
	if head == node: assignhead(nextnode)
	if tail == node: assigntail(prevnode)
	sizedecrement()
	print(f"{node.value} has been deleted.")
def displaylist():
	end = head
	print("\nSTART")
	while end != None:
		print(f" {end.value} {"<== Head" if end == head else ("<== Tail" if end == tail else "")}")
		print(" ^")
		print(" |")
		print(" v")
		end = end.next
	print("END\n")
def displaylist_reverse(head, tail):
	end = tail
	print("\nSTART")
	while end != None:
		print(f" {end.value} {"<== Head" if end == head else ("<== Tail" if end == tail else "")}")
		print(" ^")
		print(" |")
		print(" v")
		end = end.prev
	print("END\n")
def traverse_till_hit(val):
	global head
	end = head
	flag=0
	while end != None:
		if end.value == val:
			print("",end.value,"<---")
			flag=1
		else:
			print("",end.value)
		print(" ^")
		print(" |")
		print(" v")
		end = end.next
	print("End")
	NoMatchMsg(flag)
def deletefirstfoundnode(val):
		curr = traverse(val)
		traverse_till_hit(val)
		if curr != None: PopNode(curr)
def deletelastfoundnode(val):
		curr = traverseReverse(val)
		traverse_till_hit(val)
		if curr != None: PopNode(curr)
def deleteallnode(val):
		curr = traverse(val)
		traverse_till_hit(val)
		while curr != None:
			PopNode(curr)
			curr = traverse(val)
#Insert multiple nodes: (list of nodes to be added, Start or end, -1, node pointer)
def InsertMultipleNode(l, pos, InsertInGivenOrder = None, start =None):
	global head, tail
	start = head if start is None else start
	try:
		l=list(l)
		newstart = InsertNodeBefore(l[0],start) if pos == 'Start' else InsertNodeAfter(l[0])
		if InsertInGivenOrder != None:
			for x in l[1:]:
				newstart = InsertNodeAfter(x, newstart)
		else:
			for x in l[1:]:
				newstart = InsertNodeBefore(x,newstart)
	except TypeError:
		print(type(l),"is not iterable.")
	return newstart
def InsertNodeAtPos(val, pos):
	global head
	curr = head
	if pos > (size): 
		print("Index out of bounds")
		return
	elif pos == size:
		InsertNodeAfter(val)
		return
	counter = 0
	while counter != pos:
		curr = curr.next
		counter += 1
	InsertNodeBefore(val,curr)
def DeleteNodeAtPos(pos):
	global head
	curr = head
	if pos > (size): 
		print("Index out of bounds")
		return
	counter = 0
	while counter != pos:
		curr = curr.next
		counter += 1
	PopNode(curr)
l1 = [1,2,31,61]
neww=InsertNodeBefore(100)
InsertNodeBefore(150)
InsertNodeBefore(200, neww)
InsertNodeAfter(266)
InsertNodeAfter(50,neww)
InsertMultipleNode(l1, 'Start')
InsertMultipleNode([77], 'End')
PopNode(head)
InsertMultipleNode([89, 63, 999, 888], 'Start', -1, neww)
PopNode(tail)
InsertNodeAfter(2)
InsertNodeBefore(2)
#deleteallnode(2)
#deletelastfoundnode(2,head)
#traverse_till_hit(5,head)
InsertNodeAfterGivenValue(20,2)
InsertNodeBeforeGivenValue(l1,2,-1)
InsertNodeAtPos(500,7)
deletelastfoundnode(2)
DeleteNodeAtPos(8)
#displaylist()
#traverse_till_hit(2)
#displaylist_reverse(head, tail)
print(size)
