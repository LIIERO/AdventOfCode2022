
def main():
    data = txt_into_str()
    n = 14
    for i in range(len(data)-n+1):
        test_slice = data[i:i+n]
        if len(set(test_slice)) == n:
            print(i+n)
            break

