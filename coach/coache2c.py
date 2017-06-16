def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, sec) = time_string.split(splitter)
    return(mins + '.' + sec)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return ({'Name': temp1.pop(0), 'DOB': temp1.pop(0), 'Times' : str(sorted(set([sanitize(t) for t in temp1]))[0:3])})
    except IOError as ioe:
        print('File error:' + str(ioe))
        return None


james = get_coach_data('D:/open_source_software/python/hfpy_ch6_data/james2.txt')
julie = get_coach_data('D:/open_source_software/python/hfpy_ch6_data/julie2.txt')
mikey = get_coach_data('D:/open_source_software/python/hfpy_ch6_data/mikey2.txt')
sarah = get_coach_data('D:/open_source_software/python/hfpy_ch6_data/sarah2.txt')

print(james['Name'] + "'s fastest times are : " + james['Times'])
print(julie['Name'] + "'s fastest times are : " + julie['Times'])
print(mikey['Name'] + "'s fastest times are : " + mikey['Times'])
print(sarah['Name'] + "'s fastest times are : " + sarah['Times'])