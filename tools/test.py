import wordnet

test_data = ['đảng','chính quyền','làm chủ','ban','đảng viên']

sample = wordnet.Wordnet('wordnet10-4-2019.xlsx')

for each in test_data:
    print(sample.get_ez_synsets_as_row(each))


