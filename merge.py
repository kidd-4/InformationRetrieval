from files import files
from block import block
import os

class merge:
    def __init__(self,input_file):
        self.input_file = input_file
        self.merge_num = 1;
        self.directory = '/Users/grey/Desktop/Test/'
        self.flag = False
        # self.output_file = output_file



    def merge_block(self):
        # output_file_path = '/Users/grey/Desktop/Test/Merge.txt'
        # open(output_file_path,'w')
        open_file =[file.open_file() for file in self.input_file]

        # open_file = [open(f.file_path,'r') for f in self.input_file]
        # print len(open_file)-1
        # lines = [f.readline() for f in open_file]
        for index in range(1,len(open_file)):
            if(index == 1):
                temp = self.merge_two_blocks(open_file[0],open_file[1])
                self.merge_num += 1
            else:
                # if os.path.isfile(temp):
                #     print "Yes"
                # else:
                #     print "No"
                temp_file = open(temp,'r')
                temp = self.merge_two_blocks(temp_file,open_file[index])
                self.merge_num += 1



    def merge_two_blocks(self,file1, file2):
        line1 = file1.readline()
        line2 = file2.readline()
        # list1 = list()
        # list2 = list()
        list1 = self.parseLine(line1)
        list2 = self.parseLine(line2)

        # term_list = list()
        while line1 or line2:
            # print "running"
            new_list = dict()
            if list1 and list2:
                if(list1[0] > list2[0]):
                    new_list = [list2[0],list2[1]]
                    # term_list.append(line2[0])
                    self.WriteBlockToDisk(list2[0],list2[1])
                    line2 = file2.readline()
                    list2 = self.parseLine(line2)
                elif(list1[0] < list2[0]):
                    new_list = [list1[0],list1[1]]
                    # term_list.append(line1[0])
                    self.WriteBlockToDisk(list1[0],list1[1])
                    line1 = file1.readline()
                    list1 = self.parseLine(line1)
                else:
                    new_list = [list1[0],list1[1]+list2[1]]
                    # term_list.append(line1[0])
                    self.WriteBlockToDisk(list1[0],(list1[1]+list2[1]))
                    line2 = file2.readline()
                    list2 = self.parseLine(line2)
                    line1 = file1.readline()
                    list1 = self.parseLine(line1)
            elif list1 and not list2:
                new_list = [list1[0], list1[1]]
                # term_list.append(line1[0])
                self.WriteBlockToDisk(list1[0], list1[1])
                line1 = file1.readline()
                list1 = self.parseLine(line1)
            elif list2 and not list1:
                new_list = [list2[0], list2[1]]
                # term_list.append(line2[0])
                self.WriteBlockToDisk(list2[0], list2[1])
                line2 = file2.readline()
                list2 = self.parseLine(line2)
        self.flag = True
        return self.WriteBlockToDisk(None,None)
        # print "end"




    def WriteBlockToDisk(self, term,posting_list):


        file_name = "%s%d.%s" % ('Merge', self.merge_num, 'txt')
        # print file_name
        file_path = self.directory + file_name
        # print file_path
        # if not os.path.exists(file_path):
        #     os.mknod(file_path)
        file = files(file_path)
        file.open_file('a')
        # file = open(file_path,'w')
        if self.flag:
            file.close_file()
            self.flag = False
            return file_path
        # for term in sorted_iterms:
            # print dictionary[term]
            # file.write_file(content)
        # print posting_list
        else:
            file.write_file(block(term, posting_list))

        # file.close_file()


    def parseLine(self,line):
        if line:
            temp = line.split(' ')
            return [temp[0],[int(docID) for docID in temp[1:]]]
        else:
            return False