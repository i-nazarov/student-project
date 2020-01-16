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


def output(c1, c2, c3, c4, s1, s2, s3, s4, p1, p2, p3, p4, h1, h2, h3, h4, all_l, sn1, sn2, sn3,
		   sn4):  # counts, strings probability, entropy
	counter1 = 1
	cp1 = 0
	cp2 = 0
	cp3 = 0
	cp4 = 0
	ch1 = str(h1)
	ch2 = str(h2)
	ch3 = str(h3)
	ch4 = str(h4)
	for a in all_l:
		for i1 in c1:
			for i2 in c2:
				for i3 in c3:
					for i4 in c4:
						temp = ord(all_l[counter1 - 1])
						if sn1.count(counter1) == 1 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[cp1]) + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[cp2]) + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(p3[cp3]) + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(
								p3[cp3]) + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(p3[cp3]) + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[
																 cp2]) + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0'  '  	|' + '0.00' + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[
																 cp2]) + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[cp2]) + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(
								p3[cp3]) + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 0 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(
								temp) + ')' + ' 	|' + '0' + '  	|' + '0.00' + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[cp2]) + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(p3[cp3]) + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 1 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[
																 cp1]) + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 1 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[
																 cp1]) + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 1 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[
																 cp1]) + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(
								p3[cp3]) + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 1 and sn2.count(counter1) == 0 and sn3.count(
								counter1) == 1 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[
																 cp1]) + '  	|' + ch1 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(p3[cp3]) + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 1 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 0:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[cp1]) + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[
																 cp2]) + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						elif sn1.count(counter1) == 1 and sn2.count(counter1) == 1 and sn3.count(
								counter1) == 0 and sn4.count(counter1) == 1:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[cp1]) + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[
																 cp2]) + '  	|' + ch2 + '|' + '0' + '  	|' + '0.00' + '  	|' + ch3 + '|' + str(
								c4.pop(0)) + '  	|' + str(p4[cp4]) + '  	|' + ch4 + '	|')
							counter1 += 1
						else:
							if counter1 <= 25:
								cp1 = counter1 - 1
							if counter1 <= 21:
								cp2 = counter1 - 1
							if counter1 <= 28:
								cp3 = counter1 - 1
							if counter1 <= 36:
								cp4 = counter1 - 1
							print('| ' + all_l[counter1 - 1] + ' (' + str(temp) + ')' + ' 	|' + str(
								c1.pop(0)) + '  	|' + str(p1[cp1]) + '  	|' + ch1 + '|' + str(
								c2.pop(0)) + '  	|' + str(p2[cp2]) + '  	|' + ch2 + '|' + str(
								c3.pop(0)) + '  	|' + str(
								p3[cp3]) + '  	|' + ch3 + '|' + '0' + '  	|' + '0.00  	|' + ch4 + '	|')
							counter1 += 1
						print(
							' ________________________________________________________________________________________________________________')


def main():
	strings = get_strings(4)
	texts = [Text(string) for string in strings]
	for text in texts:
		text.count_chars()
		text.calc_prob()
		text.calc_len()
		text.calc_ent()

	text_len1 = len(text1)  # count of all characters
	text_len2 = len(text2)
	text_len3 = len(text3)
	text_len4 = len(text4)
	text1_list = list(text1)  # lists of all characters
	text2_list = list(text2)
	text3_list = list(text3)
	text4_list = list(text4)
	text1_every_char_count, text1_every_char_list = count_chars(text1)  # lists of every char count and list
	text2_every_char_count, text2_every_char_list = count_chars(text2)
	text3_every_char_count, text3_every_char_list = count_chars(text3)
	text4_every_char_count, text4_every_char_list = count_chars(text4)
	pi1 = probability(text1_every_char_count, text_len1)  # lists of probabilities
	pi2 = probability(text2_every_char_count, text_len2)
	pi3 = probability(text3_every_char_count, text_len3)
	pi4 = probability(text4_every_char_count, text_len4)
	h1 = entropy(text1_every_char_count)
	h2 = entropy(text2_every_char_count)
	h3 = entropy(text3_every_char_count)
	h4 = entropy(text4_every_char_count)
	all_lst = all_list(text1_list, text2_list, text3_list, text4_list)
	all_c, all_l = count_chars(all_lst)  # count and list of characters from all texts
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

	print(
		' ________________________________________________________________________________________________________________')
	print(
		'|Символы (код)	|' + 'Текст №1		|' + 'Текст №2		|' + 'Текст №3		|' + 'Текст №4			|')
	print(
		' ________________________________________________________________________________________________________________')
	print(
		'|		|Кол	|' + 'p	|' + 'H	|Кол	|' + 'p	|' + 'H	|Кол	|' + 'p	|' + 'H	|Кол	|' + 'p	|' + 'H	|')
	print(
		'|________________________________________________________________________________________________________________')
	output(text1_every_char_count, text2_every_char_count, text3_every_char_count, text4_every_char_count,
		   text1_every_char_list, text2_every_char_list, text3_every_char_list, text4_every_char_list, pi1, pi2, pi3,
		   pi4, h1, h2, h3, h4, all_l, sn1, sn2, sn3, sn4)

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
