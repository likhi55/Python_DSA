from LinkedList import LinkedList

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1, 4)

print('\nLL after set_value():')
my_linked_list.print_list()
