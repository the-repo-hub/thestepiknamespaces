def add(namespace, var):
    dictionary[namespace]['variables'].add(var)
    return 0


def create(namespace, var):
    dictionary[namespace] = {'parent': var, 'variables': set()}
    return dictionary[namespace]


def get(namespace, var):
    if var in dictionary[namespace]['variables']:
        return namespace
    elif dictionary[namespace]['parent'] is not None:
        for keys in dictionary.keys():
            if var in dictionary[keys]['variables']:
                return keys
            else:
                continue
    return None


i = int(input())
dictionary = {'global': {'parent': None, 'variables': set()}}  # honorably stolen from comments
get_list = []
for j in range(i):
    command, namespace, var = input().split()
    if command == 'add':
        add(namespace, var)
    elif command == 'create':
        create(namespace, var)
    elif command == 'get':
        get_list.append(get(namespace, var))
for k in get_list:
    print(k)
