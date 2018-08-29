import numpy as np

input_dict = dict()
with open('gathered.txt') as infile:
    for line in infile:
        token = line.split()
        #print(token)
        if token[0] in input_dict:
            input_dict[token[0]].append(float(token[1]))
        else:
            input_dict[token[0]] = [float(token[1]),]
    for value in input_dict.itervalues():
        assert len(value) == 20
    for item in input_dict.iteritems():
        print("%s,%f,%f" % (item[0], np.mean(item[1]), np.std(item[1])))