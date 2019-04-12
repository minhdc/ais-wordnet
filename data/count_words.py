import xlrd 
  
loc = ("wordnet10-4-2019.xlsx") 
  
wb = xlrd.open_workbook(loc) 


n_sheet = wb.sheet_by_index(0)   
count = 0

for i in range(1,n_sheet.ncols): 
    for j in range (0,n_sheet.nrows):
        if n_sheet.cell_value(j,i) != '':
            count += 1
            print(n_sheet.cell_value(j,i))
print(" n = ",count)
        
a_sheet = wb.sheet_by_index(1)   
count = 0

for i in range(1,a_sheet.ncols): 
    for j in range (0,a_sheet.nrows):
        if a_sheet.cell_value(j,i) != '':
            count += 1
print(" a = ",count)
        
v_sheet = wb.sheet_by_index(2)   
count = 0

for i in range(1,v_sheet.ncols): 
    for j in range (0,v_sheet.nrows):
        if v_sheet.cell_value(j,i) != '':
            count += 1
print(" v = ",count)
        
