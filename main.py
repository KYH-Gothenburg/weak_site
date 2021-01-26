import hashlib


def main():
    words = ['apa', 'banan', 'citron']
    salt = '21382873hfkjls'
    in_data = 'citron'
    
    salted_data = salt + in_data
    md5 = hashlib.md5()
    md5.update(salted_data.encode('utf-8'))
    hash_value = md5.hexdigest()

    for i in range(10000):
        md5.update(hash_value.encode('utf-8'))
        hash_value = md5.hexdigest()
    print(hash_value)
    
    for word in words:
        md5.update(word.encode('utf-8'))
        hash_value = md5.hexdigest()
        print(word, ' = ', hash_value)
    


if __name__ == '__main__':
    main()