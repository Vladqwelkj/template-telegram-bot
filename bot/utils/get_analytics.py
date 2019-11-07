
# Нужно связать с бд

def hello_habit(user_id, date_start=None, date_end=None, total=False): # или username вместо id, чтобы можно было найти в БД

	###Здесь должна быть связь с БД.
	#Получить данные с date_start по date_end, где user_id=user_id

	results = {
		'users': None,
		'new_users': None,
		'outflow': None,
		'bot_using_day': None,
		'users_without_habits': None,
		'active_habits': None,
		'fulfillments': None,
		'omissions': None,
		'payments': None,
		'profit': None,
		'buddy_pair': None,
		'invites': None,
		'approval': None,
		'kicks': None,
		'reposts':None
	}
	return results


def organisator(date_start, date_end, user_id, total=False): # или username вместо id, чтобы можно было найти в БД

	###Здесь должна быть связь с БД.
	#Получить данные с date_start по date_end

	results = {
		'marathons': None,
		'free': None,
		'participants': None,
		'organisators': None,
		'tasks': None,
		'habits': None,
		'lessons': None,
		'lessons_marks': None,
		'payments': None,
		'revenue': None,
		'profit': None,
	}
	return results