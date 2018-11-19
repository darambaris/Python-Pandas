def handleList():
	#lists syntax 
	my_list = ['a',1,True,3.14]
	print(my_list)

	#print the first items
	print(my_list[0])

	#print the 3 first values
	print(my_list[:3])

	#add item in list
	my_list.append('append new value! :)')
	print(my_list)

	return my_list

def handleTuple():
	#tuple syntax (immutables values)
	my_tuple = ('a',1,True,3.14)
	print(my_tuple)

	#error (tuple is immutable!)
	#my_tuple[0]='zzzz'
	#print(my_tuple)

	#error (There is no method append())
	#my_tuple.append('zzzz')
	#print(my_tuple)
	return my_tuple

def handleDict():
	#key and value
	my_dict = {}
	my_dict['first_name'] = 'Jessika'
	my_dict['last_name'] = 'Darambaris'

	print(my_dict)

	#other syntax
	my_dict_2 = {'first_name': 'Jessika', 'last_name': 'Darambaris'}
	print(my_dict_2)

	#get key values
	print('1:' +my_dict['first_name'] +
		'\n2:' +my_dict_2.get('first_name'))

	### method get return 'none' in invalid keys, 
	### however first method return KeyError

	#print all the dict keys
	print(my_dict.keys())

	#print all the dict values
	print(my_dict.values())

	return my_dict


def slicingValues():
	
	#start zero, left inclusive and right not inclusive
	l = ['dog','cat','bird','bear','snake','lion']

	#inclusive dog l[0], not inclusive cat l[1]
	print(l[0:1])

	#start 0 (inclusive) and end 4 (not inclusive)
	print(l[:4])

	#start 3 (inclusive) and end last element
	print(l[3:])

	#step 2 (jump 1 position each step)
	print(l[::2])

	#start 1 and end 4 step 2
	print(l[1:4:2])

def rangeInterval():
	
	#create a interval with 5 values
	r = range(5)

	#return a generator (= xrange in Python 2)
	print (r)
	print (type(r))

	#convert generator to list
	lr = list(range(5))
	print (lr)


if __name__ == '__main__':
	my_list  =  handleList()
	my_tuple =  handleTuple()
	my_dict  =  handleDict()
	
	my_dict['first_name'] = my_tuple
	my_dict['last_name']  = my_list

	#print all dict pair keys-values	
	#each key-value pair returns like a tuple
	print(my_dict.items())

	print('\n>>>Slicing Values')
	slicingValues()

	print('\n>>> Range Interval')
	rangeInterval()