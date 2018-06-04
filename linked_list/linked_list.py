class Node(object):
	"""
	class to hold data and next of a node
	use node = Node(data) to initialize a new node
	"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""
	Class that wraps all operations of a linked list
	"""
	
	def __init__(self):
		self.head = None
	
	def print_list(self):
		"""
		print data of all nodes in a linked list
		"""
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def push(self, data):
		"""
		insert a new node with a given a value for data at beginning of a linked list.
		"""
		node = Node(data)
		node.next = self.head
		self.head = node

	def insert_after(self, prev_node, data):
		"""
		insert a new node after a given node
		"""
		node = Node(data)
		node.next = prev_node.next
		prev_node.next = node

	def append(self, data):
		"""
		insert a new node at end of linked list
		"""
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			last = self.head
			while(last.next):
				last = last.next
			last.next = node

	def delete_node(self, data):
		"""
		delete a (first) node if given data matches with data of a node
		"""
		temp = self.head
		if temp.data == data:
			self.head = temp.next
			temp = None
			return
		while(temp is not None):
			if temp.data == data:
				break
			prev = temp
			temp = temp.next
		if temp is None:
			return
		prev.next = temp.next
		temp = None

	def get_node_count(self):
		"""
		return number of nodes of a linked list
		"""
		temp = self.head
		count = 0
		while(temp):
			count += 1
			temp = temp.next
		return count

	def search(self, data):
		"""
		search for a node with a given data. If found returns true else false.
		"""
		current = self.head
		while current is not None:
			if current.data ==  data:
				return True
			current = current.next
		return False

	def get_element_at_index(self, index):
		"""
		returns data of an element at a given index
		"""
		current = self.head
		count = 0
		while(current):
			if count == index:
				return current.data
			count += 1
			current = current.next
		return False

	def get_element_count(self, data):
		"""
		returns number of occurences of a given element
		"""
		current = self.head
		count = 0
		while(current is not None):
			if current.data == data:
				count += 1
			current = current.next
		return count

	def detect_loop(self):
		current = self.head
		traversed_nodes = set()
		while(current):
			if current in traversed_nodes:
				return True
			traversed_nodes.add(current)
			current = current.next
		return False

	def detectLoop(self):
		slow_p = self.head
		fast_p = self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p:
				print "Found Loop"
				return

    
