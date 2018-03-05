import sys
from files import files
from block import block

class spimiInvert:
    def __init__(self,token_stream,memory_limit):
        self.token_stream = token_stream
        self.memory_limit = memory_limit
        self.directory = '/Users/grey/Documents/PycharmProjects/InformationRetrieval/Test/'
        self.block_num = 0
        self.td_list = list()

    def spimi_invert(self):
        self.token_stream = iter(self.token_stream)
        output_file = list()
        flag = True
        dictionary = dict()
        while flag:
            try:
                # while sys.getsizeof(dictionary) / 1024 / 1024 <= self.memory_limit:

                tokens = self.token_stream.next()
                if tokens[0] not in dictionary:
                    dictionary[tokens[0]] = list()
                    posting_list = dictionary[tokens[0]]
                else:
                    posting_list = dictionary[tokens[0]]
                # if full(posting_list):
                #     posting_list = DoublePostingList(dictionary,tokens[0])
                posting_list.append([tokens[1],tokens[2]])
            except StopIteration:
                flag = False

        # sorted_terms = [term for term in sorted(dictionary.keys())]
        # self.block_num += 1
        # block_file = self.WriteBlockToDisk(sorted_terms,dictionary,output_file)
        # output_file.append(block_file)
        # print output_file

        # return output_file
        sorted(dictionary.keys())
        return dictionary


        # def full(self,posting_list):


        # def DoublePostingList(self,dictionary,term):

    def WriteBlockToDisk(self, sorted_iterms, dictionary, output_file):
        file_name = "%s%d.%s" % ('block', self.block_num, 'txt')
        print file_name
        file_path = self.directory + file_name
        print file_path
        # if not os.path.exists(file_path):
        #     os.mknod(file_path)
        file = files(file_path)
        file.open_file('w')
        # file = open(file_path,'w')

        for term in sorted_iterms:
            # print dictionary[term]
            # file.write_file(content)
            file.write_file(block(term, dictionary[term]))

        # file.close_file()
        file.close_file()
        return file






