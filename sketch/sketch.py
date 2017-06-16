try:
    data = open('d:/open_source_software/python/sketch.txt')
    for line in data:
        try:
            (role, spoken) = line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('miss file')

