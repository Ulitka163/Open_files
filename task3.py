def write_file(files):
    number_str = {}
    for file in files:
        with open(file, encoding='utf-8') as file_1:
            number_str[file] = (len(file_1.readlines()))
    with open('4.txt', 'a', encoding='utf-8') as document:
        for key in sorted(number_str, key=number_str.get):
            with open(key, encoding='utf-8') as file_2:
                document.write(key + '\n' + str(number_str.get(key)) + '\n' + file_2.read() + '\n')
    return number_str.values()

write_file(['1.txt', '2.txt', '3.txt'])