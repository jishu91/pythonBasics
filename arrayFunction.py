my_list = []

def insert_element(value):
	my_list.append(value)
def delete_element(value):
	if value in my_list:
		my_list.remove(value)
def display():
	print(my_list)
insert_element(770)
insert_element(200)
insert_element(54)
delete_element(770)
display()
