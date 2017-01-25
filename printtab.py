def print_tab(the_list,level=0):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_tab(each_item,level+1)
		else:
			for i in each_item:
				print ("\t")
			print(each_item)

list1=["1","2",'3','test',[1,2,3],100*6]		
print_tab(list1,2)	