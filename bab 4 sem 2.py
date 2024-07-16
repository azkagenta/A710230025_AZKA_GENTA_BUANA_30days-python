# Contoh penggunaan duck typing
def print_all(items):
    for item in items:
        print(item, end=' ')
    print()  # Untuk newline setelah semua item dicetak

# List
my_list = [1, 2, 3]

# Tuple
my_tuple = (4, 5, 6)

# String
my_string = "Hello, world!"

# Memanggil fungsi print_all dengan parameter my_list, my_tuple, dan my_string
print_all(my_list)   # output: 1 2 3
print_all(my_tuple)  # output: 4 5 6
print_all(my_string) # output: H e l l o ,   w o r l d !