def print_id_of_param(the_list):
    print(id(the_list))
    print(the_list)
    the_list.append(2)
    print(id(the_list))
    print(the_list)


eggs = ['cat', 'dog', 'eel']
print(id(eggs))
print(eggs)
print()

print_id_of_param(eggs)

print()
print(eggs)
