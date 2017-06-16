import pickle
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
    with open('d:/open_source_software/python/man_file_b.txt', 'wb') as man_file,\
            open('d:/open_source_software/python/other_file_b.txt', 'wb') as other_file:
        # print(man, file=man_file)
        # print(other, file=other_file)
        pickle.dump(man, file=man_file)
        pickle.dump(other, file=other_file)
except IOError as ioe:
    print("file error:" + str(ioe))
except pickle.PickleError as pe:
    print("pickle error:" + str(pe))
try:
    with open('d:/open_source_software/python/man_file_b.txt', 'rb') as man_file,\
            open('d:/open_source_software/python/other_file_b.txt', 'rb') as other_file:
        man_list = pickle.load(man_file)
        other_list = pickle.load(other_file)
        print(man_list)
        print(other_list)
except IOError as e:
    print("file error:" + str(e))
except pickle.PickleError as pe:
    print("pickle error:" + str(pe))




