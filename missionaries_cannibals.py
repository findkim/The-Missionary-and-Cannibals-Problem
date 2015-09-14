#!/usr/bin/env python

# Kim Ngo
# CSE40171: Artificial Intelligence
# Sept. 13, 2015
# S. M. Niaz Arifin

# Program solves the Missionaries and Cannibals problem using uniform cost search

import operator
import Queue

WRONGSIDE = 1
NUM_MISS, NUM_CANN, NUM_BOAT = range(3)
ACTIONS = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
GOAL = [0,0,0]

class node:
	def __init__(self, value):
		self.value = value
		self.children = []

	def get_value(self):
		return self.value

	def valid(self, value):
		# num_cannibals > num_missionaries are invalid states and are removed from consideration
		if value[NUM_CANN] <= value[NUM_MISS] and all(i >= 0 for i in value) and value[NUM_CANN] <= 3 and value[NUM_MISS] <= 3:
			return True
		return False

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
		for action in ACTIONS:
			child = None
			if state.value[NUM_BOAT] == WRONGSIDE:
				child = node(map(operator.sub, state.value, action))
			elif state.value[NUM_BOAT] != WRONGSIDE:
				child = node(map(operator.add, state.value, action))
			if state.valid(child.get_value()) and child not in explored and child != state:
				if child.get_value() == GOAL:
					print_line(child.get_value(), [0,0,0], q.qsize())
					return child
				else:
					q.put(child)
					print_line(child.get_value(), action, q.qsize())

#	return current_state, action, nodes_expanded

def print_line(value, action, nodes_expanded):
	print '<' + ','.join(map(str,value)) + '>, <' + ','.join(map(str,action)) + '>, ' + str(nodes_expanded)

if __name__ == '__main__':
	initial_state = [3,3,1]

	print "Algorithm: breadth-first search"
	init = node(initial_state)
	breadth_first_search(init)
