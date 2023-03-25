

def txt_into_array(name: str = 'input'):
    with open('data/' + name + '.txt', 'r') as f:
        return [line.strip() for line in f]

def txt_into_array_raw(name: str = 'input'):
    with open('data/' + name + '.txt', 'r') as f:
        return [line.rstrip('\n') for line in f]

def txt_into_int_array(name: str = 'input'):
    with open('data/' + name + '.txt', 'r') as f:
        return [None if not len(line.strip()) else int(line.strip()) for line in f]

def txt_into_str(name: str = 'input'):
    with open('data/' + name + '.txt', 'r') as f:
        data_str = ''
        for line in f:
            data_str += str(line.strip())
        return data_str

def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def nested_append(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]].append(value)
