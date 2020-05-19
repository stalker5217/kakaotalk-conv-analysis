# 전처리 과정
# date line (--------------- 2019년 8월 14일 수요일 ---------------) >> 삭제
# user date ([사람] [오전 8:41]) >> 삭제

import re

# PreProcess
def refine_message():
	# read file
	
	msg_list = []
	with open("log.txt", "r", encoding='utf-8') as f:
		msg_list = f.readlines()
	
	user_date_pattern = re.compile("\[([\S\s]+)\] \[(오전|오후) ([0-9:\s]+)\] ")
	date_line_pattern = re.compile("--------------- ([0-9]+년 [0-9]+월 [0-9]+일)")

	# refine
	with open("refine.txt", "w", encoding="utf-8") as f:
		for msg in msg_list:
			if re.match(date_line_pattern, str(msg)) is None:
				msg = re.sub(user_date_pattern, '', str(msg))
				if not ('사진' in msg or '이모티콘' in msg):
					f.write(msg)

if __name__ == '__main__':
    refine_message()