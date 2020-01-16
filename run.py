# -*- coding: utf-8 -*-
import math
import pylab


class Text:
	def __init__(self, text_list):
		self.text_list = text_list
		self.chars_num = {}
		self.char_prob = {}
		self.entropy = 0
		self.text_len = 0

	def count_chars(self):
		lat_chars = 'abcdefghijklmnopqrstuvwxyz'
		rus_chars = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
		all_chars = lat_chars + rus_chars
		chars_num = {c: 0 for c in all_chars}
		for c in self.txt:
			if c in chars_num:
				chars_num[c] += 1
		self.chars_num = chars_num

	def calc_len(self):
		text_len = 0
		for key, val in self.chars_num.items():
			text_len += val
		self.text_len = text_len

	def calc_prob(self):
		char_prob = {}
		for key, val in self.chars_num.items():
			prob = val / self.text_len
			char_prob[key] = round(prob, 2)
		self.char_prob = char_prob

	def calc_ent(self):
		ent = 0
		for key, val in self.char_prob.items():
			ent += val * (math.log(val, 10))
		self.entropy = ent

	def get_value(self, value):
		if value == 'letters':
			return list(self.chars_num.keys())
		elif value == 'quantity':
			return self.chars_num.values()
		elif value == 'entropy':
			return self.entropy
		elif value == 'length':
			return self.text_len
		else:
			raise Exception('Incorrect value')


def get_strings(n):
	texts = []
	for i in range(1, n+1):
		text = open(f'text{i}.txt').readlines()
		text = ''.join(text)
		text = text.lower()
		texts.append(text)
	return texts


def all_list(l1, l2, l3, l4):
	l = []
	l.extend(l1)
	l.extend(l2)
	l.extend(l3)
	l.extend(l4)
	return l


def serial_number(all_l, txt_evrchl):
	clist = []  # list of coinsiding values
	counter = 0
	for i in all_l:
		counter += 1
		for n in txt_evrchl:
			if n == i:
				clist.append(counter)
	return clist


def form_output():
	table_list = []
	row = f'{"Кол-во":10}|{"p":10}|{"H":10}|'*4
	header = f'''{"_"*140}
|Символ|{"Текст1":32}|{"Текст2":32}|{"Текст3":32}|{"Текст4":32}|
{"_"*140}
|{"":6}|{row}'''


def main():
	strings = get_strings(4)
	texts = [Text(string) for string in strings]
	letters = texts[0].get_value('letters')
	for text in texts:
		text.count_chars()
		text.calc_prob()
		text.calc_len()
		text.calc_ent()


	all_lst = all_list(text1_list, text2_list, text3_list, text4_list)
	sn1 = serial_number(all_l, text1_every_char_list)
	sn2 = serial_number(all_l, text2_every_char_list)
	sn3 = serial_number(all_l, text3_every_char_list)
	sn4 = serial_number(all_l, text4_every_char_list)
	graph = []
	graph2 = []
	graph3 = []
	graph4 = []
	numg1 = []
	numg2 = []
	numg3 = []
	numg4 = []
	pi12 = pi1
	pi22 = pi2
	pi32 = pi3
	pi42 = pi4
	# cpi1 =
	# cpi2 = chr(pi2)
	# cpi3 = chr(pi3)
	# cpi4 = chr(pi4)
	counter = 0
	elist = []
	for i in text1_every_char_list:
		elist.append(i)
	for i in text2_every_char_list:
		if elist.count(i) == 0:
			elist.insert(counter, i)
	for i in text3_every_char_list:
		if elist.count(i) == 0:
			elist.append(i)
	for i in text4_every_char_list:
		if elist.count(i) == 0:
			elist.append(i)
	for i in elist:
		if text1_every_char_list.count(i) == 0:
			pi12.insert(counter, 0)
		counter += 1
	counter = 0
	for i in elist:
		if text2_every_char_list.count(i) == 0:
			pi22.insert(counter, 0)
		counter += 1
	counter = 0
	for i in elist:
		if text3_every_char_list.count(i) == 0:
			pi32.insert(counter, 0)
		counter += 1
	counter = 0
	for i in elist:
		if text4_every_char_list.count(i) == 0:
			pi42.insert(counter, 0)
		counter += 1
	counter = 0

	for i in elist:
		graph.append(ord(i))
	for i in range(len(pi12)):
		numg1.append(i)
	for i in range(len(pi22)):
		numg2.append(i)
	for i in range(len(pi32)):
		numg3.append(i)
	for i in range(len(pi42)):
		numg4.append(i)

	# pylab.annotate(
	#   'message',
	#  xy=(6, 30),
	# xytext=(8, 31.5),
	# arrowprops={
	#   'facecolor': 'black',
	#  'shrink': 0.05
	# });

	###pylab.plot(221)
	##pylab.plot (numg1,pi1)
	##pylab.xticks(numg1,graph)
	##pylab.xlabel('Код символа')
	##pylab.ylabel('Вероятность')
	##pylab.title('Английский текст №1',fontsize=10)
	##
	###pylab.subplot(222)
	##pylab.plot (numg3, pi3)
	##pylab.xticks(numg3,graph)
	##pylab.xlabel('Код символа')
	##pylab.ylabel('Вероятность')
	##pylab.title('Русский текст №1',fontsize=10)
	##
	###pylab.subplot(223)
	##pylab.plot (numg2, pi2)
	##pylab.xticks(numg2,graph)
	##pylab.xlabel('Код символа')
	##pylab.ylabel('Вероятность')
	##pylab.title('Английский текст №2',fontsize=10)

	# pylab.subplot(224)
	pylab.plot(numg4, pi4)
	pylab.xticks(numg4, graph)
	pylab.xlabel('Код символа')
	pylab.ylabel('Вероятность')
	pylab.title('Русский текст №2', fontsize=10)

	pylab.show()


if __name__ == "__main__":
	main()
