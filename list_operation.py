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