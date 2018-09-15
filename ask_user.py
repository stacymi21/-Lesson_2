ask ={'как дела?':'хорошо','что делаешь?':'программирую','как успехи?':'лучше, чем у тебя'}

def what_ask_you (question, answers):
	return ask.get(question)



def ask_user (answers):
	while True:
		try:
			user_questions = input ('Поговорим? ')	
			answer = what_ask_you (user_questions, answers)
			print (answer)
		
			if user_questions == 'пока':
				return ('Хорошего дня!')
				break
		except KeyboardInterrupt: 
			return ('Ну и ладно')
			break

print (ask_user (ask))

