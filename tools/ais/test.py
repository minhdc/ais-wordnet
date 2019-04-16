from ais import wordnet
from ais import sentence

from urllib.parse import unquote
from http.server import BaseHTTPRequestHandler,HTTPServer

import json
import socket
import os, sys
import time

import util

sample_wordnet = wordnet.Wordnet('wordnet10-4-2019.xlsx')
tag_list = ['n','v','a','e']
'''
class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global sample_wordnet

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        xxx =unquote(unquote(self.path))
        arr = xxx.split("/")
        results = sample_wordnet.get_ez_synsets_as_row(xxx)
        self.wfile.write(bytes(json.dumps(results),"utf-8"))
'''


test_data = ['phòng','đảng','chính quyền','làm chủ','ban','đảng viên']



#get synset
for each in test_data:
    print(sample_wordnet.get_ez_synsets_as_row(each))


text = 'thế lực thù địch có những âm mưu gì'

s = sentence.Sentence(text,tag_list)
print(s.get_similar_sentences_as_list(sample_wordnet))

u = util.WordnetUtil('wordnet10-4-2019.xlsx')
u.count_total_synonyms_per_category()
u.count_ambiguous_words()