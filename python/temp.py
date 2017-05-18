with open('./datasets/pubfig/pubfig_full.txt') as file_input:
    neg_folds = dict()
    pos_folds = dict()
    
    file_list = file_input.readlines()
    for index in range(len(file_list)):
        file_list[index] = file_list[index].replace(' ', '_').strip().split('\t')
    
    index = 0;
    while str(file_list[index][0]).startswith('#'):
        index += 1
    
    cur_fold = 0
    num_folds = int(file_list[index][0])
    index += 1
    
    while index < len(file_list):
        if not str(file_list[index][0]).startswith('#'):
            num_pos = int(file_list[index][0])
            num_neg = int(file_list[index][1])
            index += 1
            
            pos_list = list()
            for inner in range(index, num_pos + index):
                pos_list.append(file_list[inner])
                index += 1
            
            neg_list = list()
            for inner in range(index, num_neg + index):
                neg_list.append(file_list[inner])
                index += 1

            pos_folds[cur_fold] = pos_list
            neg_folds[cur_fold] = neg_list
            cur_fold += 1
        else:
            index += 1

print('Done')
for item in neg_folds.iteritems():
    print(item[0], len(item[1]))

