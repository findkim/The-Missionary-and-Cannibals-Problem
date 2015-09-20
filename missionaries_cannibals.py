#!/usr/bin/env python

# Kim Ngo
# CSE40171: Artificial Intelligence
# Sept. 13, 2015
# S. M. Niaz Arifin

# Program solves the Missionaries and Cannibals problem using uniform cost search

import operator
import Queue

START = [3,3,1]
WRONGSIDE = 1
NUM_MISS, NUM_CANN, NUM_BOAT = range(3)
ACTIONS = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
GOAL = [0,0,0]

class Node:
	def __init__(self, value):
		self.state = value
		self.action = []
		self.depth = 0
		self.children = []
		self.parent = None
		self.expanded = 0

	def set_expanded(self, expanded):
		self.expanded = expanded

	def get_expanded(self):
		return self.expanded

	def set_parent(self, parent):
		self.parent = parent

	def get_parent(self):
		return self.parent

	def set_action(self, action):
		self.action = action

	def get_state(self):
		return self.state

	def get_action(self):
		return self.action

	def set_depth(self, depth):
		self.depth = depth

	def get_depth(self):
		return self.depth

	def get_children(self):
		return self.children

	def set_children(self, visited):
		# Sets possible children from current state
		if len(self.children) == 0:
			# Calculates child depending on boat side
			for action in ACTIONS:
				child = None
				if self.state[NUM_BOAT] == WRONGSIDE:
					child = node(map(operator.sub, self.state, action))
				elif self.state[NUM_BOAT] != WRONGSIDE:
					child = node(map(operator.add, self.state, action))
				
				# Keep list of children that are new states
				if tuple(child.state) not in visited:
					child.set_action(action)
					child.set_depth(self.depth+1)
					child.set_parent(self)
					self.children.append(child)
					visited.add(tuple(child.state))

	def valid_children(self):
		# Goes through possible children and discards invalid states
		if len(self.children) == 0:
			return
		valid_children = []
		for child in self.children:
			if self.valid(child.state):
				valid_children.append(child)
		self.children = valid_children
		return self.children

	def valid(self, state):
		# num_cannibals > num_missionaries are invalid states and are removed from consideration
		if state[NUM_CANN] <= state[NUM_MISS] and all(i >= 0 for i in state) and state[NUM_CANN] <= 3 and state[NUM_MISS] <= 3:
			return True
		return False



def all(iterable):
	for element in iterable:
		if not element:
			return False
	return True


def concat_line(state, action, nodes_expanded):
	# Concatenates into proper output
	# state [0,0,0], action [0,0,0], # of nodes expanded
	return '<' + ','.join(map(str,state)) + '>, <' + ','.join(map(str,action)) + '>, ' + str(nodes_expanded)

def print_path(root, leaf):
	# Prints path from root to leaf
	stack = []
	node = leaf
	stack.append(concat_line(leaf.get_state(), [0,0,0], leaf.get_expanded()))
	while node != root:
		stack.append(concat_line(node.get_parent().get_state(), node.get_action(), node.get_expanded()))
		node = node.get_parent()
	while stack:
		print stack.pop()
	return


def breadth_first_search(root):
	print "Algorithm: breadth-first search"
	DONE = None
	q = Queue.Queue()
	q.put(root)
	explored = set()
	current_depth = 0
	expanded = 0
	children = [] # Temporary list of children for current depth: [action, state] 
	while not q.empty():
		state = q.get()	# python remove and return item from queue

		# For each depth, add valid children to queue
		if current_depth != state.get_depth():
			for child in children:
				if state.valid(child.get_state()):
					if child.get_state() == GOAL:
						DONE = child
					child.parent.children.append(child)
					child.set_expanded(expanded)
			if DONE != None:
					print_path(root, DONE)
					return 
			children = []
			current_depth += 1

		# Ignore invalid states
		if not state.valid(state.get_state()):
			continue

		# Find actions that lead to new states
		for action in ACTIONS:
			child = None

			# Calculates child depending on boat side
			if state.get_state()[NUM_BOAT] == WRONGSIDE:
				child = Node(map(operator.sub, state.get_state(), action))
			elif state.get_state()[NUM_BOAT] != WRONGSIDE:
				child = Node(map(operator.add, state.get_state(), action))
			child.set_action(action)

			# Keep list of children that are new states
			if child != state and child not in explored:
				expanded += 1
				child.set_depth(state.depth+1)
				child.set_parent(state)
				children.append(child)
				explored.add(child)
				q.put(child)



if __name__ == '__main__':
	root = Node(START)
	breadth_first_search(root)
