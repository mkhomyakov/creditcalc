import math as mt #для округления значений
import argparse as arg #для работы с аргументами в cmd
import sys

#работаем с аргументами из командной строки
parser = arg.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = sys.argv
args_dict = {}
arguments = []
for i in range(1, len(args)):
	sprt = args[i].find('=')
	argument = args[i][2:sprt]
	value = args[i][sprt+1:]
	args_dict[argument] = value
	if argument != 'type':
		arguments.append(argument)
arguments.sort()

#преобразуем типы данных в словаре аргументов
for i in arguments:
	if i in ['interest', 'payment']:
		args_dict[i] = float(args_dict[i])
	elif i in ['principal', 'periods']:
		args_dict[i] = int(args_dict[i])

#функция подсчета дифференцированных платежей
def diffpay(principal, periods, interest):
	interest_rate = interest / 100 / 12
	all_pays = 0
	for i in range(1, periods + 1):
		payment = mt.ceil((principal / periods) + interest_rate * (principal - ((principal * (i - 1)) / periods)))
		all_pays += payment
		print('Month {}: payment is {}'.format(i, payment))
	overpay = all_pays - principal
	print()
	print('Overpayment =  {}'.format(overpay))

#подсчет тела для аннуитетных платежей
def ann_principal(interest, payment, periods):
	interest_rate = interest / 100 / 12
	all_payments = periods * payment
	principal = round(payment / ((interest_rate * ((1 + interest_rate)**periods)) / (((1 + interest_rate)**periods) - 1)))
	overpay = all_payments - principal
	print('Your loan principal = {}!'.format(principal))
	print('')
	print('Overpayment = {}'.format(overpay))

#подсчет периодов для аннуитетных платежей
def ann_months(interest, payment, principal):
		interest_rate = interest / 100 / 12
		months = mt.ceil(mt.log((payment / (payment - interest_rate * principal)) , 1 + interest_rate))
		all_payments = payment * months
		overpay = all_payments - principal
		years = months // 12
		rest_months = months % 12
		if years == 1:
			if rest_months == 0:
				print('It will take {} year to repay this loan!'.format(years))
			elif rest_months == 1:
				print('It will take {} year and {} month to repay this loan!'.format(years, rest_months))
			else:
				print('It will take {} year and {} months to repay this loan!'.format(years, rest_months))
		elif years == 0:
			if rest_months == 1:
				print('It will take {} month to repay this loan!'.format(rest_months))
			else:
				print('It will take {} months to repay this loan!'.format(rest_months))
		else:
			if rest_months == 0:
				print('It will take {} years to repay this loan!'.format(years))
			elif rest_months == 1:
				print('It will take {} years and {} month to repay this loan!'.format(years, rest_months))
			else:
				print('It will take {} years and {} months to repay this loan!'.format(years, rest_months))
		print()
		print('Overpayment = {}'.format(overpay))

#подсчет аннуитетного платежа
def ann_payment(interest, periods, principal):
	interest_rate = interest / 100 / 12
	annuity_pay = mt.ceil(principal * ((interest_rate * (1 + interest_rate)**periods) / ((1 + interest_rate)**periods - 1)))
	all_payments = annuity_pay * periods
	overpay = all_payments - principal
	print('Your monthly payment = {}!'.format(annuity_pay))
	print()
	print('Overpayment = {}'.format(overpay))

#ветвление для всех возможных вариантов
if len(args_dict) == 4:
	if args_dict['type'] == 'diff':
		if arguments == ['interest', 'periods', 'principal']:
			diffpay(args_dict['principal'], args_dict['periods'], args_dict['interest'])
		else:
			print('Incorrect parameters.')
	elif args_dict['type'] == 'annuity':
		if arguments == ['interest', 'payment', 'periods']:
			ann_principal(args_dict['interest'], args_dict['payment'], args_dict['periods'])
		elif arguments == ['interest', 'payment', 'principal']:
			ann_months(args_dict['interest'], args_dict['payment'], args_dict['principal'])
		elif arguments == ['interest', 'periods', 'principal']:
			ann_payment(args_dict['interest'], args_dict['periods'], args_dict['principal'])
		else:
			print('Incorrect parameters.')
	else:
		print('Incorrect parameters.')
else:
	print('Incorrect parameters.')