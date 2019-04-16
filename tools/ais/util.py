import xlrd
import datetime

class WordnetUtil:
    def __init__(self,wordnet_path):
        #self.wordnet
        if wordnet_path:
            self.wordnet = xlrd.open_workbook(wordnet_path)

    def count_total_synonyms_per_category(self,list_of_category=["n","v","a","r","e"]):
        list_of_sheets = []
        count = 0
        total_synonyms = 0
        for i in range(0,len(list_of_category)):
            sheet = self.wordnet.sheet_by_index(i)
            for j in range(1,sheet.ncols):
                for k in range(0,sheet.nrows):
                    if sheet.cell_value(k,j) != '':
                        count += 1
            print("sheet ",list_of_category[i]," : ",count,'synonyms at ',datetime.datetime.now())
            list_of_sheets.append(count)
            total_synonyms += count
            count = 0
        print("total syns: ",total_synonyms)
        return total_synonyms

    def count_ambiguous_words(self,list_of_category=['n','v','a','r','e']):
        list_of_ambiguous = []
        count = 0
        total_ambiguous = 0
        for i in range(0,len(list_of_category)):
            sheet = self.wordnet.sheet_by_index(i)
            for j in range(0,sheet.nrows):               
                if sheet.cell_value(j,0) == sheet.cell_value(j,1):
                    count += 1
            print("sheet ",list_of_category[i]," has : ",count, " ambiguous shits")
            list_of_ambiguous.append(count)
            total_ambiguous += count
            count = 0
        print("total ambiguous: ",total_ambiguous)
        return total_ambiguous
        


