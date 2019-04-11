from underthesea import pos_tag
import xlsxwriter
import os

INCLUDING_TAGS = ['N','V','A']

current_set_of_words = set()

for each_file in os.listdir():
	if each_file.endswith('txt'):
		with open(each_file,"r") as f:
			for each_chunk in f.readlines():
				for each in pos_tag(each_chunk):
					if each[1] in INCLUDING_TAGS:
						current_set_of_words.add(each)
	

workbook = xlsxwriter.Workbook('wordnet.xlsx')
n = workbook.add_worksheet('n')
a = workbook.add_worksheet('a')
v = workbook.add_worksheet('v')
adv = workbook.add_worksheet('adv')

col = 0
n_row = 0
a_row = 0
v_row = 0
adv_row = 0

for each_word in current_set_of_words:
	if each_word[1] == 'N' or each_word[1] == 'Nb' or each_word[1] == 'Ny':
		n.write(n_row,col,each_word[0].replace('.','').strip())
		n_row += 1
	elif each_word[1] == 'V' or each_word[1] == 'Vb' or each_word[1] == 'Vy':
		v.write(v_row,col,each_word[0].replace('.','').strip())
		v_row += 1
	elif each_word[1] == 'A' or each_word[1] == 'Ab':
		a.write(a_row,col,each_word[0].replace('.','').strip())
		a_row += 1
	elif each_word[1] == 'R':
		adv.write(a_row,col,each_word[0].replace('.','').strip())
		adv_row += 1

print('done!')
print("a = ",a_row)
print("v = ",v_row)
print("n = ",n_row)
print("adv = ",adv_row)
workbook.close()
