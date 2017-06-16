try:
    with open('d:/open_source_software/python/sketch.txt') as data:
        man = []
        other = []
        for line in data:
            try:
                (role, spoken) = line.split(':', 1)
                spoken = spoken.strip()
                if role == 'Man':
                    man.append(spoken)
                elif role == "Other Man":
                    other.append(spoken)
            except ValueError:
                pass
except IOError:
    print('miss file')
try:
    with open('d:/open_source_software/python/man_file.txt', 'w') as man_file,\
            open('d:/open_source_software/python/other_file.txt', 'w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)
except IOError as ioe:
    print("file error:" + str(ioe))
finally:
    print("finish")




