from parse import parse
from spimiInvert import spimiInvert
from merge import merge

# def main(args):
files_list = ['/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-000.sgm']
# files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm','/Users/grey/Desktop/reuters/reut2-001.sgm','/Users/grey/Desktop/reuters/reut2-002.sgm',
#               '/Users/grey/Desktop/reuters/reut2-003.sgm','/Users/grey/Desktop/reuters/reut2-004.sgm','/Users/grey/Desktop/reuters/reut2-005.sgm',
#               '/Users/grey/Desktop/reuters/reut2-006.sgm','/Users/grey/Desktop/reuters/reut2-007.sgm','/Users/grey/Desktop/reuters/reut2-008.sgm',
#               '/Users/grey/Desktop/reuters/reut2-009.sgm']
# files_list = ['/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-000.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-001.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-002.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-003.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-004.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-005.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-006.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-007.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-008.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-009.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-010.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-011.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-012.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-013.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-014.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-015.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-016.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-017.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-018.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-019.sgm',
#               '/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-020.sgm','/Users/grey/Documents/PycharmProjects/InformationRetrieval/reuters/reut2-021.sgm']
parse_obj = parse(files_list)
parse_result = parse_obj.parse()
# print parse_result[:100]

spimiInvert_obj = spimiInvert(parse_result,1)
output_file = spimiInvert_obj.spimi_invert()
# print str(output_file)

# merge_obj = merge(output_file)
# merge_obj.merge_block()
print "end"
# print parse_obj.length_of_document_list
# print parse_obj.number_of_document
# total = 0
# for number in parse_obj.length_of_document_list:
#      total += number
#
# print total
# print total / parse_obj.number_of_document

