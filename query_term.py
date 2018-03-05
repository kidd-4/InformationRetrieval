
class query_term:
    def __init__(self,keywords):
        self.directory = '/Users/grey/Documents/PycharmProjects/InformationRetrieval/Test/Merge8.txt'
        self.keywords = keywords

    def query_or(self):
        posting_list_list = list()
        for key in self.keywords:
            posting_list_list.append(self.search(key))

        for index in range(1,len(posting_list_list)):
            if(index == 1):
                temp = self.combine(posting_list_list[0],posting_list_list[1])
            else:
                temp = self.combine(temp,posting_list_list[index])
        # print "or"
        return temp



    def query_and(self):
        posting_list_list = list()
        for key in self.keywords:
            posting_list_list.append(self.search(key))
        for index in range(1,len(posting_list_list)):
            if(index == 1):
                temp = self.intersect(posting_list_list[0],posting_list_list[1])
            else:
                temp = self.intersect(temp,posting_list_list[index])
        # print "and"
        return temp


    def parseLine(self,line):
        if not line:
            return False
        temp = line.split(' ')
        return [temp[0],[int(docID) for docID in temp[1:]]]

    def search(self,key):
        file = open(self.directory, 'r')
        line = file.readline()
        list = self.parseLine(line)
        while key != list[0]:
            line = file.readline()
            if not line:
                return []
            list = self.parseLine(line)
        return list[1]

    def combine(self,list1,list2):
        result = list()
        iter1 = iter(list1)
        iter2 = iter(list2)
        flag1 = True
        flag2 = True
        try:
            docID1 = iter1.next()
        except StopIteration:
            flag1 = False
        try:
            docID2 = iter2.next();
        except StopIteration:
            flag2 = False
        while flag1 or flag2:
            if flag1 and flag2:
                if(docID1 == docID2):
                    result.append(docID1)
                    try:
                        docID2 = iter2.next()
                    except StopIteration:
                        flag2 = False
                    try:
                        docID1 = iter1.next()
                    except StopIteration:
                        flag1 = False
                elif docID1 > docID2:
                    result.append(docID2)
                    try:
                        docID2 = iter2.next()
                    except StopIteration:
                        flag2 = False
                else:
                    result.append(docID1)
                    try:
                        docID1 = iter1.next()
                    except StopIteration:
                        flag1 = False
            elif flag1 and not flag2:
                result.append(docID1)
                try:
                    docID1 = iter1.next()
                except StopIteration:
                    flag1 = False
            elif flag2 and not flag1:
                result.append(docID2)
                try:
                    docID2 = iter2.next()
                except StopIteration:
                    flag2 = False

        return result

    def intersect(self,list1,list2):
        result = list()
        iter1 = iter(list1)
        iter2 = iter(list2)
        flag1 = True
        flag2 = True
        try:
            docID1 = iter1.next()
        except StopIteration:
            return []
        try:
            docID2 = iter2.next()
        except StopIteration:
            return []
        while flag1 and flag2:
            if(docID1 == docID2):
                result.append(docID1)
                try:
                    docID2 = iter2.next()
                except StopIteration:
                    flag2 = False
                try:
                    docID1 = iter1.next()
                except StopIteration:
                    flag1 = False
            elif docID1 < docID2:
                try:
                    docID1 = iter1.next()
                except StopIteration:
                    flag1 = False
            else:
                try:
                    docID2 = iter2.next()
                except StopIteration:
                    flag2 = False
        return result