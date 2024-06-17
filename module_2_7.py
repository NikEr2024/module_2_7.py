def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'Helloy', True]
values_dict = {'a': 4, 'b': 5, 'c': 6}

print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

#def append_to_list(item, list_my=None):
#    if list_my is None:
#        list_my = [1, 2]
#        list_my.append(item)
#    print(list_my)
#
#append_to_list()