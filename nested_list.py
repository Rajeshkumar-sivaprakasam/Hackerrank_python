"""def get_data(n):	
	for i in range(0,n):
		name = input("Name\t")
		mark = float(input("Mark\t"))
		collection.append([name,mark])
		marklist.append(mark)

def check_high(marklist):
	marklist.remove(max(marklist))
	print(max(marklist))

collection = []
marklist = []N
print(get_data(int(input("Enter no of student"))))
print(collection)
print(marklist)
check_high(marklist)

"""
collection = []
marklist = []
for i in range(int(input())):
		name = input()
		mark = float(input())
		collection.append([name,mark])
		marklist.append(mark)
second_highest = sorted(list(dict.fromkeys(marklist)))[1]
for a,c in sorted(collection):
	if c == second_highest:
		print(a)

#methoed two

"""
score_list = []
for _ in range(int(input())):
	name = input()
	score = float(input())
	mark_sheet.append([name,score])
	score_list.append(score)


second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

for name,marks in sorted(mark_sheet):
	if marks == second_lowest_mark:
		print(name)
"""