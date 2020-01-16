# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt


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
		for c in self.text_list:
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
			if val != 0:
				ent += val * (math.log(val, 10))
		self.entropy = ent

	def get_value(self, value):
		if value == 'letters':
			return list(self.chars_num.keys())
		elif value == 'quantity':
			return list(self.chars_num.values())
		elif value == 'entropy':
			return round(self.entropy, 5)
		elif value == 'length':
			return self.text_len
		elif value == 'probability':
			return list(self.char_prob.values())
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


def form_output(rows_list):
	table_rows = []
	line2 = f'{"Кол-во":^10}|{"p":^10}|{"H":^10}|'*4
	header = f'''{"_"*144}
|{"Символ":^10}|{"Текст1":^32}|{"Текст2":^32}|{"Текст3":^32}|{"Текст4":^32}|
{"_"*144}
|{"":^10}|{line2}
{"_"*144}
'''
	for i in range(len(rows_list[0])):
		table_rows.append([])
		for j in range(len(rows_list)):
			if type(rows_list[j]) != list:
				table_rows[-1].append(f'{rows_list[j]:^10}')
			else:
				table_rows[-1].append(f'{rows_list[j][i]:^10}')
	rows = f'\n'.join([f'|{"|".join(row)}|' for row in table_rows])
	table = f'{header}{rows}'
	return table


def main():
	strings = get_strings(4)
	texts = [Text(string) for string in strings]
	rows = [[]]
	for text in texts:
		text.count_chars()
		text.calc_len()
		text.calc_prob()
		text.calc_ent()
		for v in ('quantity', 'probability', 'entropy'):
			rows.append(text.get_value(v))
	letters = texts[0].get_value('letters')
	rows[0] = letters
	table = form_output(rows)

	print(table)
	#plt.figure()
	for i in range(2, 12, 3):
		plt.figure()
		if i in (2, 5):
			x, y = rows[0][:-33], rows[i][:-33]
		else:
			x, y = rows[0][26:], rows[i][26:]
		plt.plot(x, y)
	plt.show()


if __name__ == "__main__":
	main()
