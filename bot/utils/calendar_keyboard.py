from calendar import Calendar, isleap
from datetime import datetime, date

from telegram.ext import CallbackContext

from bot.utils.utils import build_keyboard, remove_emoji

February = 2

# Number of days per month (except for February in leap years)
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

next_button = '▶️'
prev_button = '◀️'

def monthlen(year, month):
    return mdays[month] + (month == February and isleap(year))


def prevmonth(year, month):
    if month == 1:
        return year - 1, 12
    else:
        return year, month - 1


def nextmonth(year, month):
    if month == 12:
        return year + 1, 1
    else:
        return year, month + 1


class CalendarKeyboard:
    MONTHS = {
        1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
        7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь',
    }

    def __init__(self, context: CallbackContext, month=None, year=None, allow_past=False):
        self.context = context
        self.allow_past = allow_past
        self.current_month = context.user_data.get('__calendar_month', None)
        self.current_year = context.user_data.get('__calendar_year', None)

        if not self.current_month:
            self.current_month = month or datetime.now().month
            context.user_data['__calendar_month'] = self.current_month

        if not self.current_year:
            self.current_year = year or datetime.now().year
            context.user_data['__calendar_year'] = self.current_year

    def get_keyboard(self, header=None, footer=None):
        if not header:
            header = []
        if not footer:
            footer = []

        monthday_keyboard = self.__get_monthdays_keyboard()
        months_keyboard = self.__get_months_keyboard()

        return header + monthday_keyboard + months_keyboard + footer

    def get_current_month_name(self):
        return self.MONTHS[self.current_month]

    def get_current_year(self):
        return self.current_year

    def get_monthday_date(self, monthday):
        return date(self.current_year, self.current_month, int(monthday))

    def change_month(self, month_name):
        if next_button in month_name:
            new_year, new_month = nextmonth(self.current_year, self.current_month)

        elif prev_button in month_name:
            new_year, new_month = prevmonth(self.current_year, self.current_month)

        else:
            raise ValueError('Its not calendar month button')

        self.context.user_data['__calendar_month'] = new_month
        self.context.user_data['__calendar_year'] = new_year

    def is_valid_monthday(self, monthday):
        try:
            is_valid = monthlen(self.current_year, self.current_month) >= int(monthday) > 0
        except ValueError:
            is_valid = False

        return is_valid

    def is_valid_month_name(self, month_name):
        if next_button not in month_name and prev_button not in month_name:
            return False

        month_name = remove_emoji(month_name).strip()

        _, next_month = nextmonth(self.current_year, self.current_month)
        _, prev_month = prevmonth(self.current_year, self.current_month)

        return month_name == self.MONTHS[next_month] or month_name == self.MONTHS[prev_month]

    def clear_context_data(self):
        self.context.user_data.pop('__calendar_month', None)
        self.context.user_data.pop('__calendar_year', None)

    def __get_monthdays_keyboard(self):
        monthdays = Calendar().itermonthdays(self.current_year, self.current_month)

        if not self.allow_past and self.__is_present_month():
            today = datetime.now().day
            monthdays_buttons = [str(monthday) if monthday >= today else ' ' for monthday in monthdays]

            while monthdays_buttons[:7] == [' '] * 7:
                monthdays_buttons = monthdays_buttons[7:]

        else:
            monthdays_buttons = [str(monthday) if monthday != 0 else ' ' for monthday in monthdays]

        return build_keyboard(monthdays_buttons, 7)

    def __get_months_keyboard(self):
        _, next_month = nextmonth(self.current_year, self.current_month)
        _, prev_month = prevmonth(self.current_year, self.current_month)

        next_month_button = '{month} {button}'.format(month=self.MONTHS[next_month], button=next_button)
        prev_month_button = '{button} {month}'.format(button=prev_button, month=self.MONTHS[prev_month])

        if not self.allow_past and self.__is_present_month():
            return [[next_month_button]]
        else:
            return [[prev_month_button, next_month_button]]

    def __is_present_month(self):
        return self.current_month == datetime.now().month and self.current_year == datetime.now().year
