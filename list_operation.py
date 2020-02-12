"""if __name__ == '__main__':
    N = int(input())
    list_empty = []

    list_empty.insert(0,5)
    list_empty.insert(1,10)
    list_empty.insert(0,6)
    print(list_empty)
    list_empty.remove(6)
    list_empty.append(9)
    list_empty.append(1)
    list_empty.sort()
    print(list_empty)
    list_empty.pop()
    list_empty.reverse()
    print(list_empty)
"""
if __name__ == '__main__':
	n = int(input())
	l = []
	for i in range(n):
		s = input().split()
		cmd = s[0]  
		args = s[1:]
		if cmd != "print":
			eval('l.{0}{1}'.format(cmd,tuple(map(int,args))))
			
		"""cmd += "("+ ",".join(args) +")"
	    	eval("l."+cmd)
	    	"""
		else:
			print(l)

"""
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
