"""
This problem actually has quite a simple solution
Load the people into an array, then check the relevant index and read the value there into the new
 index to check again, repeat until you get stuck in a loop or find the target
The real problem is the optimization - there are up to 100000 people and 100000 queries

Now I tried and I tried but couldn't quite squeeze enough out
The basic idea is to cache what we can and can't reach as we go down those paths the first time
Then if we ever return we can immediantly stop

First comes the issue of storing that info - for each entry we might want to store if it can reach
 every other one, a 100000*100000 array will timeout before it's created, and dicts of that size
 will spend forever querying each entry, so I opted to kind of merge the two, use an array of dicts

Next optimization was to store every possible step we explore - at first I was just storing the
 individual steps as follows:
    index 1 points to 2 - store 1->2 = 1
    index 2 points to 3 - store 2->3 = 1
But you can relatively cheaply also work out that 1->3 = 2 and store that
This greatly increaces the amount of paths we cache

Especially with randomly generated input, most of the time there won't actually be valid paths
This means that just storing what's possible doesn't actually help much
In fact when exploring some myself I found out many of the queries tend to die in the same loops

When I found a loop I was already saving it as impossible for everything along the path
If you were looking for 1->5 and had the path 1 -> 2 -> 3 -> 4 -> 2, I would store 1-4 -> 5 = -1
If you have 100000 other values though they all have to find that loop to decide it's not possible
So the next optimization would be to mark these loops
I was running out of time at this point, so I did it by saving all other paths involving the values
 inside the loop as -1
I hindsight, this is incredibly slow, you have to set possibly hundreds of thousands of values at
 once, and if the loop isn't commonly used you're never going to get that time investment back
The better way to do it requires a bit of thinking about the problem

You can intepret our group of people as a transition graph - each person is a node, with an unlimted
 amount of paths in but only one out
The imortant thing to note is that there is no end state, each node points to another valid node
This means all possible paths have to eventually end up in a loop
Even if there is a valid path between two specific nodes, if you keep going afterwards you will
 eventually find the loop
Though note that not all nodes are on a loop, some just point into one
What this means is that once you find a loop, you have found every valid path for the nodes you've
 travesed, both in and out of the loop

So what does this mean for our caching?
Simple - you don't store invalid paths
Instead you do one of two things:
A. Fully explore each path until you find the loop
B. Store if you've fully explored an index, and if not then the index to continue from
I have not tried this so I don't know which is better
In case A you spend a bit of extra time processing things in return for more caching and a simpler
 storage format

In both cases the following logic holds:
If you have an unexplored index you follow it and cache the path as normal
If you find a new loop then make sure to cache it entirely - i.e. 1 -> 2 -> 3 -> 4 -> 2 stores:
    1 -> 2 = 1,  1 -> 3 = 2,  1 -> 4 = 3
    2 -> 3 = 1,  2 -> 4 = 2
    3 -> 4 = 1,  3 -> 2 = 2
    4 -> 2 = 1,  4 -> 3 = 2
If you come across an index that's already been explored then you can stop, check if it leads to
 your goal, and add all paths it reaches to the nodes you've visited
Using the loop from the last example, if you later found 5 -> 6 -> 1 you'd already store:
    5 -> 6 = 1,  5 -> 1 = 2
    6 -> 1 = 1
Then you'd check what index 1 can reach
    1 -> 2 = 1,  1 -> 3 = 2,  1 -> 4 = 3
And add on the steps it takes to reach index 1 from each of your starting nodes
    5 -> 2 = 3,  5 -> 3 = 4,  5 -> 4 = 5
    6 -> 2 = 2,  6 -> 3 = 3,  6 -> 4 = 4

I belive this would've pushed me past the limit and let me solve the problem, though I didn't
 realize it in time to check
"""

from sys import stdin

N = int(stdin.readline().split(" ")[0])
T = [int(i) for i in stdin.readline().strip().split(" ")]

canReach = [{} for _ in range(N)]

for line in stdin:
	A, B = line.split(" ")
	A = int(A)
	B = int(B)

	if B in canReach[A]:
		print(canReach[A][B])
		continue

	visited = []
	currentIndex = A
	found = False
	passes = 0


	while True:
		visited.append(currentIndex)
		currentIndex = T[currentIndex]
		passes += 1

		for i in range(len(visited)):
			steps = len(visited) - i
			if currentIndex in canReach[visited[i]]:
				current = canReach[visited[i]][currentIndex]
				canReach[visited[i]][currentIndex] = min(current, steps)
			else:
				canReach[visited[i]][currentIndex] = steps

		try:
			reach = canReach[currentIndex][B]
			found = reach != -1
			if found:
				passes += reach
			break
		except:
			pass

		if currentIndex == B:
			found = True
			break

		if currentIndex in visited:
			repeatIndex = 0
			for i in range(len(visited)):
				if visited[i] == currentIndex:
					repeatIndex = i
					break
			blackhole = visited[repeatIndex:]
			for i in blackhole:
				for j in range(N):
					if j not in blackhole:
						canReach[i][j] = -1

	if not found:
		passes = -1
		for index in visited:
			canReach[index][B] = -1

	print(passes)
