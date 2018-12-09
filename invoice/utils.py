#! /usr/bin/python3.2
# -*- coding: utf-8 -*-

from decimal import Decimal


def transform(trnsfstr):
	trnsfstr = ' '.join(trnsfstr.split())
	trnsfstr = trnsfstr.capitalize()
	return trnsfstr


def triad(number, mass, sort):
	tens = number % Decimal('100')
	tens = int(tens // Decimal('10'))
	ed = number % Decimal('10')
	word = mass[0]
	if tens == 1:
		if ed == 0:
			third_number = 'десять'
		elif ed == 1:
			third_number = 'одиннадцать'
		elif ed == 2:
			third_number = 'двенадцать'
		elif ed == 3:
			third_number = 'тринадцать'
		elif ed == 4:
			third_number = 'четырнадцать'
		elif ed == 5:
			third_number = 'пятнадцать'
		elif ed == 6:
			third_number = 'шестнадцать'
		elif ed == 7:
			third_number = 'семнадцать'
		elif ed == 8:
			third_number = 'восемьнадцать'
		elif ed == 9:
			third_number = 'девятнадцать'
		else:
			third_number = ''
	else:
		if ed == 1:
			if sort == 'w':
				third_number = 'одна'
				word = mass[1]
			else:
				third_number = 'один'
				word = mass[1]
		elif ed == 2:
			if sort == 'w':
				third_number = 'две'
				word = mass[2]
			else:
				third_number = 'два'
		elif ed == 3:
			third_number = 'три'
			word = mass[2]
		elif ed == 4:
			third_number = 'четыре'
			word = mass[2]
		elif ed == 5:
			third_number = 'пять'
		elif ed == 6:
			third_number = 'шесть'
		elif ed == 7:
			third_number = 'семь'
		elif ed == 8:
			third_number = 'восемь'
		elif ed == 9:
			third_number = 'девять'
		else:
			third_number = ''
	hundred = int(number // Decimal('100'))
	if hundred == 1:
		first_number = 'сто'
	elif hundred == 2:
		first_number = 'двести'
	elif hundred == 3:
		first_number = 'триста'
	elif hundred == 4:
		first_number = 'четыреста'
	elif hundred == 5:
		first_number = 'пятьсот'
	elif hundred == 6:
		first_number = 'шестьсот'
	elif hundred == 7:
		first_number = 'семьсот'
	elif hundred == 8:
		first_number = 'восемьсот'
	elif hundred == 9:
		first_number = 'девятьсот'
	else:
		first_number = ''
	if tens == 2:
		second_number = 'двадцать'
	elif tens == 3:
		second_number = 'тридцать'
	elif tens == 4:
		second_number = 'сорок'
	elif tens == 5:
		second_number = 'пятьдесят'
	elif tens == 6:
		second_number = 'шестьдесят'
	elif tens == 7:
		second_number = 'семьдесят'
	elif tens == 8:
		second_number = 'восемьдесят'
	elif tens == 9:
		second_number = 'девяносто'
	else:
		second_number = ''
	return first_number + ' ' + second_number + ' ' + third_number + ' ' + word


def summ(sum):
	hundred = ['', '', '', '']
	thousand = ['тысяч', 'тысяча', 'тысячи']
	million = ['миллионов', 'миллион', 'миллиона']
	billion = ['миллиардов', 'миллиард', 'миллиарда']
	sort1 = ['m']
	sum, kop = divmod(sum, 1)
	sum = int(sum)
	kop = int(round(kop, 2) * 100)
	number1 = sum // Decimal('1000000')
	part1 = int(number1)
	number2 = part1
	number2 = sum - number2 * Decimal('1000000')
	part2 = int(number2)
	billionpart = int(part1 // Decimal('1000'))
	if billionpart == 0:
		billion_word = ''
	else:
		billion_word = triad(billionpart, billion, sort1)
	mill = part1 % Decimal('1000')
	if mill == 0:
		mill_word = ''
	else:
		mill_word = triad(mill, million, sort1)
	thous = int(part2 // Decimal('1000'))
	sort1 = 'w'
	if thous == 0:
		thous_word = ''
	else:
		thous_word = triad(thous, thousand, sort1)

	hundredpart = part2 % 1000
	if hundredpart == 0:
		hundred_word = ''
	else:
		sort1 = 'm'
		hundred_word = triad(hundredpart, hundred, sort1)

	if sum < 1:
		null_word = 'ноль рублей'
	else:
		null_word = ''
	copeck_word = sum % Decimal('1')
	copeck_word = int(copeck_word * 100)
	copeck_word = str(kop)*2 if kop == 0 else str(kop)
	trnsfstr = billion_word + ' ' + mill_word + ' ' + thous_word + ' ' + hundred_word + ' ' + null_word + 'рублей' + ' ' + copeck_word + ' ' + 'копеек'
	trnsfstr = transform(trnsfstr)

	return trnsfstr