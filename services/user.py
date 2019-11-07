from datetime import datetime, timedelta, date

from sqlalchemy import cast, Date
from telegram import Update

from hellohabit.bot.states import names
from hellohabit.extensions.db import db
from hellohabit.models import User, HabitReport


def get_all():
    return User.query.all()


def find_by_id(user_id) -> User:
    return User.query.filter(User.chat_id == user_id).first()


def create_from_update(update: Update) -> User:
    user = find_by_id(update.effective_user.id)

    if not user:
        user = User(
            id=update.effective_user.id,
            chat_id=update.effective_chat.id,
            username=update.effective_user.username,
            first_name=update.effective_user.first_name,
            last_name=update.effective_user.last_name,
        )

        db.session.add(user)
        db.session.commit()

    return user


def set_phone_number(user_id, phone_number):
    user = find_by_id(user_id)

    if user:
        user.phone_number = phone_number

        db.session.add(user)
        db.session.commit()

    return user


def set_state(user_id, state):
    user = find_by_id(user_id)

    if user:
        if not user.states:
            user.states = []

        user.states.append(state)
        user.last_state = state

        db.session.add(user)
        db.session.commit()

    return user


def get_states(user_id):
    user = find_by_id(user_id)

    if user:
        return user.states


def pop_state(user_id):
    user = find_by_id(user_id)

    if user:
        state = user.states.pop()
        user.last_state = user.states[-1] if user.states else ''

        db.session.add(user)
        db.session.commit()

        return state


def clear_states(user_id):
    user = find_by_id(user_id)

    if user:
        user.states = []
        user.last_state = ''

        db.session.add(user)
        db.session.commit()

    return user


def set_last_message_time(user_id, last_message_time):
    user = find_by_id(user_id)

    if user:
        user.last_message_time = last_message_time

        db.session.add(user)
        db.session.commit()

    return user


def get_with_not_finished_creation():
    from_time = datetime.now() - timedelta(minutes=15)

    return User.query.filter(
        User.last_state.in_(names.CREATION_STATES),
        User.last_message_time <= from_time
    ).all()


def get_with_do_for_today():
    query = User.query.outerjoin(
        HabitReport, User.id == HabitReport.user_id
    ).filter(
        cast(HabitReport.creation_date, Date) == date.today(),
        HabitReport.type == 'do',
    )

    return query.all()


def get_context_data(user_id):
    user = find_by_id(user_id)

    if user:
        return user.context_data


def update_context_data(user_id, data):
    user = find_by_id(user_id)

    if user:
        user.context_data = data

        db.session.add(user)
        db.session.commit()
