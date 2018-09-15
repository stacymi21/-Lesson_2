first = input ('Введите первое число: ')
second = input ('Введите второе число: ')

def get_summ (num_one, num_two):
	try:
		summ = int(first) + int(second)
		return (summ)
	except ValueError:
		return ('Попробуйте ещё раз')

print (get_summ(first, second))