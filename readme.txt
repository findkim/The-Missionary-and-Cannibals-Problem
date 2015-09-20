Kim Ngo
CSE 40171: Artificial Intelligence
Sept. 13, 2015
Professor S. M. Niaz Arifin

missionaries_cannibals.py is a program that solves the Missionaries and
Cannibals problem using breadth-first search

run: ./missionaries_cannibals.py
or run: python missionaries_cannibals.py

The program is complete with a correct solution: 
Algorithm: breadth-first search
<3,3,1>, <1,1,1>, 5
<2,2,0>, <1,0,1>, 20
<3,2,1>, <1,1,1>, 45
<2,1,0>, <0,1,1>, 130
<2,2,1>, <1,1,1>, 295
<1,1,0>, <1,0,1>, 880
<2,1,1>, <1,1,1>, 2175
<1,0,0>, <0,1,1>, 6740
<1,1,1>, <1,1,1>, 18055
<0,0,0>, <0,0,0>, 18055

A tree is created from the start state, <3,3,1>. Each state is represented by
a node that stores the state of where the missionaries, cannibals, and boat
are, the action taken to get to the state, the depth of the node, the parent and children of the node, and the number of nodes expanded (cumultative). As the BFS algorithm proceeds from the node, visited states and invalid states are not expanded. Once the goal state <0,0,0> is reached, the algorithm stops expanding beyond the depth of the goal state and prints out the path from the start state to the goal state.
