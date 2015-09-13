#!/usr/bin/env python

# Kim Ngo
# CSE40171: Artificial Intelligence
# Sept. 13, 2015
# S. M. Niaz Arifin

# Program solves the Missionaries and Cannibals problem using uniform cost search

import operator
import Queue

NUM_MISS, NUM_CANN, NUM_BOAT = range(3)
ACTIONS = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
GOAL = [0,0,0]

class node:
	def __init__(self, value):
		self.value = value
		self.children = []
		self.actions = ACTIONS
		#self.create_children()

	def get_value(self):
		return self.value

	def get_children(self):
		return self.children

	def create_children(self):
		# Creates child nodes with 5 posssible actions
		for action in self.actions:
			child_value = map(operator.sub, self.value, action)
			self.children.append(node(child_value))
		self.valid_children() # ensures only valid children remain

	def valid_children(self):
		# num_cannibals > num_missionaries are invalid states and are removed from consideration
		valid_children = []
		for child in self.get_children():
			if child.get_value()[NUM_CANN] <= child.get_value()[NUM_MISS] and all(i >= 0 for i in child.get_value()):
				valid_children.append(child)
		self.children = valid_children

def all(iterable):
	for element in iterable:
		if not element:
			return False
	return True

def breadth_first_search(current_state):
	q = Queue.Queue()
	q.put(current_state)
	explored = set()
	while not q.empty():
		state = q.get()
		explored.add(state)
		state.create_children()
		print state.get_value(), len(state.get_children())
		for child in state.get_children():
			if child not in explored and child != state:
				if child == GOAL:
					print "GOALLL"
					return child
				q.put(child)
				print "QUEUE SIZE: ", q.qsize()

#	return current_state, action, nodes_expanded


if __name__ == '__main__':
	initial_state = [3,3,1]
	current_state = initial_state

	print "breadth-first search"
	init = node(initial_state)
	breadth_first_search(init)
