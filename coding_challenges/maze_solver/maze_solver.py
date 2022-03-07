# F-Secure Intern Technical Assesment
# Candidate: Abdullah Ansari

import sys
from bs4 import BeautifulSoup
from collections import deque


import requests

url = "https://pg-0451682683.fs-playground.com/"
cookies = {".AspNetCore.Session":"CfDJ8DgYhT7piRNBmlddqbrvsA2Zql6g8Q1VgXEABnNHHjZOKbVKB0cnjgzoJCqdtiH6UWlNWCjFrzXiKnvOEQKKJbu9jLpLCM5a4DPu%2FXeZHpx%2BoUqBOiGOm3i2xpP6FMap%2FUwGk38eMIXcE8nnBnogOs7ipit0SCMDA1%2BtJ8BvwIko"}

def get_maze():

	raw_html = requests.get(url, cookies=cookies)
	
	soup = BeautifulSoup(raw_html.text,"html.parser")

	tableTag = soup.find("table", attrs={"class":"center"})

	rowTags = str(tableTag).split('</tr>')

	global maze 
	maze = []

	for tr in rowTags:

		row = []

		dataTags = str(tr).split('</td>')

		for tag in dataTags:

			tag = tag.strip("/n").strip(" ")

			if "start" in tag:

				row.append(0)

			elif "end" in tag:

				row.append(2)

			elif "empty" in tag:

				row.append(0)

			elif "full" in tag:

				row.append(1)

			else:

				continue
			
		if len(row) > 0:

			maze.append(row)

def print_maze(maze):

	for row in maze:

		for item in row:

			print(item, end='')

		print()

def path_finder():

	global maze2
	maze2 = maze

	rows = len(maze2)
	cols = len(maze2[0])

	queue = deque()
	queue.append((0,0,''))

	directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
	key_mapping = {0:"R",1:"L",2:"D",3:"U"}
	
	visited = []

	for row in range(rows):
		visited.append([False]*cols)

	visited[0][0] = True

	while len(queue) != 0:

		coord = queue.popleft()

		if maze2[coord[0]][coord[1]] == 2:

			print(coord[2])

			sys.exit()

		for index, move in enumerate(directions):

			new_row = coord[0]+move[0]
			new_col = coord[1]+move[1]

			if (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols):

				continue

			if (maze2[new_row][new_col] == 1):

				continue

			if (visited[new_row][new_col] == True):

				continue
				 
			queue.append((new_row,new_col,coord[2]+key_mapping[index]))
			visited[new_row][new_col] = True

if 1 == 1:

	get_maze()
	#print_maze(maze)
	path_finder()
