
from query_term import query_term

print "OR queries must be like XX or XX or XX, AND queries must be like XX and XX and XX, and you can query single word"
print "Input exit to quit"
print "There is no nested query"
print "-------------------------"

list = list()
while True:
    query = raw_input()
    if ' ' in query:
        list = query.split(' ')
    if 'exit' in query:
        break;

    if "or" in list:
        while "or" in list:
            list.remove("or")
        obj = query_term(list)
        result = obj.query_or()
    elif "and" in list:
        while "and" in list:
            list.remove("and")
        obj = query_term(list)
        result = obj.query_and()
    else:
        print "single word!"
        obj = query_term(query)
        result = obj.search(query)

    print "The length of query result:{}".format(len(result))
    print result



