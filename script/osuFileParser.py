import sys

def searchSublevel(x, y):
	with open(sys.argv[1], 'r') as my_file:
		lines = my_file.readlines()
		line_iter = iter(lines)
		find = False
		target = "[" + x + "]"
		for line in line_iter:
			if target in line:
				find = True
				break
		if (find):
			for line in line_iter:
				if len(line.strip()) != 0:
					if y in line:
						l, r = line.split(':')
						print(r.strip())
						break
				else: 
					print("No such infomation in " + x)
					break			
		else:
			print( "No such infomation in file")
