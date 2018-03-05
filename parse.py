import nltk
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

class parse:
    def __init__(self,file_list):
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = ['.',',','(',')','!','<','>','?','{','}','[',']',';',':','\"','&','-','--',
                            '+','...','\'','``','\n','\r','\b','\x03','\'\'','$','\'s','*','@','=']
        self.stop_words_30 = set(["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it",
             "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they",
             "this", "to", "was", "will", "with"])
        # self.punctuation = string.punctuation
        # self.numbers = string.digits
        self.files_list = file_list
        self.number_of_document = 0
        self.length_of_document = 0
        self.length_of_document_list = list()
        self.dictionary_list = list()

    def isInt(self,value):
        try:
            x = int(value)
        except ValueError:
            return False
        else:
            return True

    def isFloat(self,value):
        try:
            x = float(value)
        except ValueError:
            return False
        else:
            return True

    def removeNum(self,num):
        num_list = ['1','2','3','4','5','6','7','8','9','0']
        for nums in num_list:
            if nums in num:
                return False
        return True

    def parse(self):
        file_tokens_list = list()
        # print self.numbers
        # print self.punctuation
        for file in self.files_list:
            with open(file) as f:
                documents = f.read()
            # soup = BeautifulSoup(documents.decode('utf-8','ignore'))
            parser = BeautifulSoup(documents.decode('utf-8','ignore'),'html.parser')
            articles = parser.find_all('reuters')

            document_tokens_id = list()
            for art in articles:
                art_id = int(art['newid'])
                self.number_of_document = self.number_of_document + 1
                self.length_of_document = 0
                dictionary = dict()

                if art.find('body'):
                    tokens = nltk.word_tokenize(art.body.text)
                    tokens_list = list()
                    for token in tokens:
                        # token = token.lower()
                        self.length_of_document = self.length_of_document + 1
                        if token not in tokens_list:
                            tokens_list.append(token)
                            dictionary[token] = 1
                        else:
                            dictionary[token] = dictionary[token] + 1

                    # print tokens_list
                    tokens_id = [(token, art_id,dictionary[token]) for token in tokens_list]
                    # self.dictionary_list.extend([(token,art_id,dictionary[token]) for token in tokens_list])
                    document_tokens_id.extend(tokens_id)

                self.length_of_document_list.append(self.length_of_document)


            file_tokens_list.extend(document_tokens_id)

        return file_tokens_list


        # print document_tokens_id[:100]
        # print file_tokens_list[:100]

# files_list = ['/Users/grey/Desktop/reuters/reut2-000.sgm']
# parse_obj = parse(files_list)
# parse_result = parse_obj.parse()
# print parse_result[:100]




