def one_list(list1,list2):
	nums=iter(list1+list2)
	list3=[]
	try:
		while(True):
			list3.append(next(nums))
	except StopIteration:
		pass
	return list3
