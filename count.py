def parseLine(line):
    if not line:
        return 0
    temp = line.split(' ')
    count = 0;
    for docID in temp[1:]:
        count +=1
    return count

directory = '/Users/grey/Desktop/Test/Merge4.txt'
file = open(directory, 'r')
line = file.readline()
count = parseLine(line)
term_num = 1
posting_list_num = count
# print posting_list_num
while line:
    line = file.readline()
    count = parseLine(line)
    posting_list_num += count
    term_num += 1

print term_num
print posting_list_num


