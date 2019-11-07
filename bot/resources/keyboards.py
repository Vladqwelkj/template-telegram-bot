
# Общие
CONTINUE_BUTTON = 'Продолжить'
BACK_BUTTON = '↩ Назад'
DONE_BUTTON = 'Готово'
CANCEL_BUTTON = 'Отмена'

# аналитика  - общее 
TODAY_BUTTON = 'Сегодня'
YESTERDAY_BUTTON = 'Вчера'
WEEK_BUTTON = 'Неделя'
MONTH_BUTTON = 'Месяц'
TOTAL_BUTTON  = 'За всё время'
PERIOD_BUTTON = 'Период'
YES_BUTTON = 'Да'
NO_BUTTON = 'Нет'

CALENDAR_BUTTON = '📆 Календарь'
CLOSE_CALENDAR_BUTTON = '✗ Закрыть календарь'

#  аналитика
COMPARE_BUTTON = 'Сравнить'
SELECT_BUTTON = 'Выбрать'

# стартовая
HELLO_HABIT_BUTTON = 'Hello Habit'
ORGANISATOR_BUTTON = 'Организатор'

#hh
ANALYTICS_BUTTON = 'Аналитика'
REVIEWS_BUTTON = 'Отзывы'
CONTACTS_BUTTON = 'Контакты'
MESSAGE_BUTTON = 'Сообщение'

# only in 'organisator'
MARATHONS_BUTTON = 'Марафоны'
MODERATION_BUTTON = 'Модерация'

# отзывы
NEW_BUTTON = 'Новые'
RESPONSED_BUTTON = 'Отвеченные'
REPLY_BUTTON = 'Ответить'

# сообщения
LOG_BUTTON = 'Лог'

#контакты
USERS_BUTTON = 'Пользователи'

# марафоны
NEXT_BUTTON = 'Следующий ➜'
PREV_BUTTON = '← Предыдущий'


# moderation
REJECT_BUTTON = 'Отклонить ✖'
APPROVE_BUTTON = 'Одобрить ☑'


REJECT_APPROVE = [[REJECT_BUTTON], [BACK_BUTTON], [APPROVE_BUTTON]]

BACK_KEYBOARD = [[BACK_BUTTON]]
MAIN_MENU = [[HELLO_HABIT_BUTTON, ORGANISATOR_BUTTON]]

HELLO_HABIT_MENU = [[b] for b in [ANALYTICS_BUTTON, REVIEWS_BUTTON, CONTACTS_BUTTON, MESSAGE_BUTTON, BACK_BUTTON]]
ANALYTICS_CUSTOM_PERIOD = [[b] for b in [SELECT_BUTTON,
                                         COMPARE_BUTTON,
                                         DONE_BUTTON,
                                         BACK_BUTTON]]
ANALYTICS_SELECT_PERIOD  = [[b] for b in [TODAY_BUTTON,
                                          YESTERDAY_BUTTON,
                                          WEEK_BUTTON,
                                          MONTH_BUTTON,
                                          TOTAL_BUTTON,
                                          PERIOD_BUTTON,
                                          BACK_BUTTON]]

SELECT_OR_CANCEL = [[SELECT_BUTTON], [CANCEL_BUTTON]]

REVIEWS_MENU = [[b] for b in [NEW_BUTTON, RESPONSED_BUTTON, BACK_BUTTON]]
ORGANISATOR_MENU = [[b] for b in [ANALYTICS_BUTTON,
                                  MODERATION_BUTTON,
                                  MARATHONS_BUTTON,
                                  REVIEWS_BUTTON,
                                  CONTACTS_BUTTON,
                                  MESSAGE_BUTTON,
                                  BACK_BUTTON]]
YES_NO = [[YES_BUTTON], [NO_BUTTON], [BACK_BUTTON]]
USERS = [[USERS_BUTTON], [BACK_BUTTON]]
LOG = [[LOG_BUTTON], [BACK_BUTTON]]