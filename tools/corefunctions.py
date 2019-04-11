from xlrd import open_workbook

from pandas import ExcelFile,read_excel
from numpy import where

def get_workbook(file_path):
    if file_path:
        return open_workbook(file_path)
    return "Error: filepath is nall"
        


def count_words(xlrd_workbook,category,synonym_only=False):
    
    xlrd_sheet = xlrd_workbook.sheet_by_name(category)
    count = 0
    starting_point = 0
    if synonym_only:
        starting_point = 1
    for i in range(starting_point,xlrd_sheet.ncols):
        for j in range(0,xlrd_sheet.nrows):
            if xlrd_sheet.cell_value(j,i) != '':
                count += 1
    return count

#return Int64Index object
def get_row_index(xlsx_file_loc,input_word):
    wordnet = ExcelFile(xlsx_file_loc)
    n_sheet = read_excel(wordnet,'n',header=None)
    return n_sheet.index[n_sheet[0] == input_word]

def get_single_synset(data_frame,input_word):
    return data_frame[data_frame[0] == input_word]