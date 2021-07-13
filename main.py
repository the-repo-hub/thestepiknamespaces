# add global a | a = 0
# create foo (in) global | def foo()
# add foo b | in def foo():
#                   b = 0
# create bar foo
# add bar a

i = int(input())
dictionary = {}
output_list = [''] * i
counter = 0
for j in range(0, i):
    command, namespace, var = input().split()
    if command == 'add':
        dictionary[var] = namespace
    elif command == 'create':
        dictionary[namespace] = var
    elif command == 'get':
        output_list[counter] = dictionary.get(var)
        counter += 1

for k in range(0, counter + 1):
    print(output_list[k])
