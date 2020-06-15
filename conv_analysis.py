import re
import numpy as np
import json

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image

# read config
def readConfig():
	with open('config.json', 'r') as f:
		config = json.load(f)

		global raw_file_path
		global img_path
		global font_path

		raw_file_path = config['raw_file_path']
		img_path = config['img_path']
		font_path = config['font_path']

# PreProcess
def refine_message():
	# read file
	msg_list = []
	with open(raw_file_path, "r", encoding='utf-8') as f:
		msg_list = f.readlines()
	
	# regex
	# date line (--------------- 2019년 8월 14일 수요일 ---------------) >> 삭제
	# user date ([사람] [오전 8:41]) >> 삭제
	# 사진 >> 삭제
	# 이모티콘 >> 삭제
	date_line_pattern = re.compile("--------------- ([0-9]+년 [0-9]+월 [0-9]+일 [월|화|수|목|금|토|일]요일) ---------------")
	user_date_pattern = re.compile("\[([\S\s]+)\] \[(오전|오후) ([0-9:\s]+)\] ")
	picture_pattern = re.compile("사진")
	emoticon_pattern = re.compile("이모티콘")

	refine_msg_list = []
	for msg in msg_list:
		msg = re.sub(date_line_pattern, '', str(msg))
		msg = re.sub(user_date_pattern, '', str(msg))
		msg = re.sub(picture_pattern, '', str(msg))
		msg = re.sub(emoticon_pattern, '', str(msg))

		if msg is not None and msg != '\n':
			refine_msg_list.append(msg.rstrip('\n'))

	return refine_msg_list

def extract_noun(msg_list):	
	nlpy = Okt()
	nouns = nlpy.nouns(" ".join(msg_list))
	count = Counter(nouns)
	noun_list = count.most_common(700)
	
	return noun_list

def visualize(noun_list):
	if img_path is not None and img_path != '':
		mask = np.array(Image.open(img_path))
		wc = WordCloud(
			font_path=font_path,
			mask=mask,
			background_color="white",
			width=1000,
			height=1000,
			max_words=700,
			max_font_size=300)
	else:
		wc = WordCloud(
			font_path=font_path,
			background_color="white",
			width=1000,
			height=1000,
			max_words=700,
			max_font_size=300)

	wc.generate_from_frequencies(dict(noun_list))
	wc.to_file('wordcloud.png')


if __name__ == '__main__':
	readConfig()
	refine_msg_list = refine_message()
	noun_list = extract_noun(refine_msg_list)
	visualize(noun_list)