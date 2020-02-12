n = int(input())
student_marks = {}
total = 0.0
for _ in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))

"""for i in range(len(line)):
	for keys in student_marks.keys():
		if keys == query_name:
			total += float(student_marks[query_name][i])
print(format(total/3,'.2f'))
"""

"""
O/P:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores)))

"""