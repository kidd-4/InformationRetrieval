from compression import compression
from spimiInvert import spimiInvert
from compression_merge import merge
# files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm']
# files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm','/Users/grey/Desktop/reuters/reut2-001.sgm','/Users/grey/Desktop/reuters/reut2-002.sgm',
#               '/Users/grey/Desktop/reuters/reut2-003.sgm','/Users/grey/Desktop/reuters/reut2-004.sgm','/Users/grey/Desktop/reuters/reut2-005.sgm',
#               '/Users/grey/Desktop/reuters/reut2-006.sgm','/Users/grey/Desktop/reuters/reut2-007.sgm','/Users/grey/Desktop/reuters/reut2-008.sgm',
#               '/Users/grey/Desktop/reuters/reut2-009.sgm']
files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm','/Users/grey/Desktop/reuters/reut2-001.sgm','/Users/grey/Desktop/reuters/reut2-002.sgm',
              '/Users/grey/Desktop/reuters/reut2-003.sgm','/Users/grey/Desktop/reuters/reut2-004.sgm','/Users/grey/Desktop/reuters/reut2-005.sgm',
              '/Users/grey/Desktop/reuters/reut2-006.sgm','/Users/grey/Desktop/reuters/reut2-007.sgm','/Users/grey/Desktop/reuters/reut2-008.sgm',
              '/Users/grey/Desktop/reuters/reut2-009.sgm','/Users/grey/Desktop/reuters/reut2-010.sgm','/Users/grey/Desktop/reuters/reut2-011.sgm',
              '/Users/grey/Desktop/reuters/reut2-012.sgm','/Users/grey/Desktop/reuters/reut2-013.sgm','/Users/grey/Desktop/reuters/reut2-014.sgm',
              '/Users/grey/Desktop/reuters/reut2-015.sgm','/Users/grey/Desktop/reuters/reut2-016.sgm','/Users/grey/Desktop/reuters/reut2-017.sgm',
              '/Users/grey/Desktop/reuters/reut2-018.sgm','/Users/grey/Desktop/reuters/reut2-019.sgm','/Users/grey/Desktop/reuters/reut2-020.sgm',
              '/Users/grey/Desktop/reuters/reut2-021.sgm']

compression_obj = compression(files_list,2)
result = compression_obj.parse()

spimiInvert_obj = spimiInvert(result,1)
output_file = spimiInvert_obj.spimi_invert()
# print str(output_file)

merge_obj = merge(output_file)
merge_obj.merge_block()
print merge_obj.term_num
print merge_obj.posting_list_num


