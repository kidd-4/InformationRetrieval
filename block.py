class block:
    def __init__(self,term,posting_lists):
        self.term = term
        self.posting_lists = posting_lists


    def __str__(self):
        return "%s %s\n" % (self.term, ' '.join([str(docID) for docID in self.posting_lists]))