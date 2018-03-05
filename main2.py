from parse import parse
from spimiInvert import spimiInvert
from merge import merge
from query_term import query_term
import math



# files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm']
# files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm','/Users/grey/Desktop/reuters/reut2-001.sgm','/Users/grey/Desktop/reuters/reut2-002.sgm',
#               '/Users/grey/Desktop/reuters/reut2-003.sgm','/Users/grey/Desktop/reuters/reut2-004.sgm','/Users/grey/Desktop/reuters/reut2-005.sgm',
#               '/Users/grey/Desktop/reuters/reut2-006.sgm','/Users/grey/Desktop/reuters/reut2-007.sgm','/Users/grey/Desktop/reuters/reut2-008.sgm',
#               '/Users/grey/Desktop/reuters/reut2-009.sgm']
files_list = ['/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-000.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-001.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-002.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-003.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-004.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-005.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-006.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-007.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-008.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-009.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-010.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-011.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-012.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-013.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-014.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-015.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-016.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-017.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-018.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-019.sgm',
              '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-020.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-021.sgm']
parse_obj = parse(files_list)
parse_result = parse_obj.parse()
# print parse_result[:100]

spimiInvert_obj = spimiInvert(parse_result,1)
output_file = spimiInvert_obj.spimi_invert()
# # print str(output_file)
#
# merge_obj = merge(output_file)
# merge_obj.merge_block()
print "running"
# print parse_obj.length_of_document_list
# print parse_obj.number_of_document

def parseLine(line):
    if not line:
        return False
    temp = line.split(' ')
    return [temp[0], [int(docID) for docID in temp[1:]]]

def parseLine2(line):
    if not line:
        return False
    temp = line.split(' ')
    return [temp[0], temp[1:]]

def make_posting_list_dictionary():
    temp = dict()
    directory = '/Users/grey/Documents/PycharmProjects/InformationRetrieval/Test/Merge8.txt'
    file = open(directory, 'r')
    line = file.readline()
    list = parseLine(line)
    while line:
        temp[list[0]] = len(list[1])
        line = file.readline()
        if not line:
            break
        list = parseLine(line)
    return temp

def numberOfTf(parse_result,term,docID):
    for terms in parse_result.keys():
        if terms == term:
            for dodID_tf in parse_result.get(terms):
                if dodID_tf[0] == docID:
                    return dodID_tf[1]

    return 0

    # directory = '/Users/grey/Desktop/Test/block1.txt'
    # file = open(directory, 'r')
    # line = file.readline()
    # list = parseLine2(line)
    # while line:
    #     if term != list[0]:
    #         line = file.readline()
    #         if not line:
    #             break
    #         list = parseLine2(line)
    #     else:
    #         for temp1 in list[1]:
    #             if temp1[0] == docID:
    #                 return temp1[1]
    #                 break
    # return 0

    # parse_result = iter(parse_result)
    # flag = True
    # while flag:
    #     try:
    #         tokens = parse_result.next()
    #         if tokens[0] == term and tokens[1] == docID:
    #             return tokens[2]
    #             break
    #     except StopIteration:
    #         flag = False
    # return 0


def calculate(query,result,k1,b,temp):

    dictionary = dict()
    # final_result = dict()
    # print query
    # print type(query) is list
    # print type(query) == list
    for docs in result:
        cal = 0
        df = 0
        tf = 0
        lengthOfDocument = 0
        if (type(query) is list) :
            for term in query:
                df = temp.get(term)
                if b == 0:
                    if df != 0 and df != None:
                        cal += math.log10(21578 / df)
                else:
                    tf = numberOfTf(output_file,term,docs)
                    lengthOfDocument = parse_obj.length_of_document_list[docs-1]
                    if df != 0 and df != None:
                        cal += math.log10(21578/df) * ((k1+1)* tf) / (k1 * ((1-b) + b*(lengthOfDocument / 133)) + tf)
                    # else:
                    #     print df
        else:
            df = temp.get(query)
            if b == 0:
                if df != 0 and df != None:
                    cal += math.log10(21578 / df)
            else:
                tf = numberOfTf(output_file, query, docs)
                lengthOfDocument = parse_obj.length_of_document_list[docs - 1]
                if df != 0 and df != None:
                    cal = math.log10(21578 / df) * ((k1 + 1) * tf) / (k1 * ((1 - b) + b * (lengthOfDocument / 133)) + tf)
                # else:
                #     print df
        dictionary[docs] = cal;

    # for term2 in sorted(dictionary.keys()):
    #     print term2
    print sorted(dictionary.items(), key=lambda dictionary: dictionary[1], reverse=True)
    print "The length of query list:{}".format(len(dictionary.keys()))
    # print sorted(dictionary.values(), reverse=True)
    # for term in sorted(dictionary.values(), reverse=True):
    #     # dict.keys()[dict.values().index(value)]
    #     final_result[(dictionary.keys()[dictionary.values().index(term)])] = term

    # print final_result
    # return final_result

print "OR queries must be like XX or XX or XX, AND queries must be like XX and XX and XX, and you can query single word"
print "Input exit to quit"
print "There is no nested query"
print "-------------------------"

list1 = []
k1 = 3
b = 0.5
temp = make_posting_list_dictionary()
while True:
    query = raw_input()
    if ' ' in query:
        list1 = query.split(' ')
    if 'exit' in query:
        break;

    if "or" in list1:
        while "or" in list1:
            list1.remove("or")
        obj = query_term(list1)
        result = obj.query_or()
        calculate(list1, result, k1, b,temp)
    elif "and" in list1:
        while "and" in list1:
            list1.remove("and")
        obj = query_term(list1)
        result = obj.query_and()
        calculate(list1, result, k1, b,temp)
    else:
        print "single word!"
        obj = query_term(query)
        result = obj.search(query)
        calculate(query, result, k1, b,temp)


    # print "The length of query result:{}".format(len(result2))
    # print "The length of query list:{}".format(len(list1))
    # print result2

