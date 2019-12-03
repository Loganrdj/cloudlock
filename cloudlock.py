
def main():
	return_list = []
	substring = "File Name: "
	f = open("cmdbtext.txt", "r")
	fileLines = f.readlines()

	for x in fileLines:
		if substring in x:
			x.strip()
			tempString = x[41:]
			tempString2 = tempString[:-7]
			# print(x[41:])
			# print(tempString2)
			return_list.append(tempString2)
	return_list = list(set(return_list))
	# print(return_list)
	for i in return_list:
		print(i)



if __name__ == '__main__':
	main()