from bot.resources import messages
def hello_habit(update, result):
    update.message.reply_text(messages.ANALYTICS_HELLO_HABIT.format(
        str(result['users']),
        str(result['new_users']),
        str(result['outflow']),
        str(result['bot_using_day']),
        str(result['users_without_habits']),
        str(result['active_habits']),
        str(result['fulfillments']),
        str(result['omissions']),
        str(result['payments']),
        str(result['profit']),
        str(result['buddy_pair']),
        str(result['invites']),
        str(result['approval']),
        str(result['kicks']),
        str(result['reposts'])))
