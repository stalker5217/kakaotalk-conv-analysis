from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image
import numpy as np

def extract_noun():
	with open("refine.txt", "r", encoding='utf-8') as f:
		msg_list = f.read()


	nlpy = Okt()
	nouns = nlpy.nouns(msg_list)
	
	count = Counter(nouns)
	noun_list = count.most_common(700)
	
	return noun_list


def visualize(noun_list):
	mask = np.array(Image.open('aa.png'))
	
	wc = WordCloud(
		font_path="./font/malgunbd.ttf",
		mask=mask,
		background_color="white",
		width=1000,
		height=1000,
		max_words=700,
		max_font_size=300)

	wc.generate_from_frequencies(dict(noun_list))
	wc.to_file('wordcloud.png')

if __name__ == '__main__':
	noun_list = extract_noun()
	visualize(noun_list)
	