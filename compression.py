import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

class compression:
    def __init__(self,file_list,flag):
        self.stop_words = stopwords.words('english')
        self.punctuation = ['.',',','(',')','!','<','>','?','{','}','[',']',';',':','\"','&','-','--',
                            '+','...','\'','``','\n','\r','\b','\x03','\'\'','$','\'s','*','@','=']
        self.stop_words_30 = set(["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it",
             "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they",
             "this", "to", "was", "will", "with"])
        self.files_list = file_list
        self.flag = flag

    def removeNum(self,num):
        num_list = ['1','2','3','4','5','6','7','8','9','0']
        for nums in num_list:
            if nums in num:
                return False
        return True

    def parse(self):
        file_tokens_list = list()
        term_num = 0;
        posting_list_num = 0;

        for file in self.files_list:
            with open(file) as f:
                documents = f.read()
            parser = BeautifulSoup(documents.decode('utf-8','ignore'),'html.parser')
            articles = parser.find_all('reuters')
            # print len(self.stop_words)
            # print self.stop_words
            document_tokens_id = list()
            for art in articles:
                art_id = int(art['newid'])

                if art.find('body'):
                    tokens = nltk.word_tokenize(art.body.text)
                    tokens_list = list()
                    for token in tokens:
                        if self.flag >= 1:
                            token = self.case_folding(token)
                        if self.flag >= 3:
                            if (token not in self.stop_words[:150] and  self.removeNum(str(token))):
                                tokens_list.append(token)
                        elif self.flag >= 2:
                            if (token not in self.stop_words_30 and self.removeNum(str(token))):
                                tokens_list.append(token)
                        elif self.flag >= 0:
                            if (self.removeNum(str(token))):
                                tokens_list.append(token)
                        else:
                            tokens_list.append(token)


                    tokens_id = [(token, art_id) for token in tokens_list]
                    document_tokens_id.extend(tokens_id)


            file_tokens_list.extend(document_tokens_id)

        # print("Found {} tokens total.".format(len(file_tokens_list)))
        return file_tokens_list

    def case_folding(self,token):
        return token.lower()