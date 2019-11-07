from collections import defaultdict
from typing import Dict

from telegram.ext import Handler

from extensions.state import State


class StatesHandler(Handler):
    BACK = '_back'

    # noinspection PyMissingConstructor
    def __init__(self, entry_point: Handler, states: Dict[str, State]):
        self.entry_point = entry_point
        self.states = states

        self.chats_states = defaultdict(list)

    def check_update(self, update):
        chat_id, chat_state = self._get_chat_state(update)

        if not chat_state:
            check = self.entry_point.check_update(update)
            return check
        else:
            return True

    def handle_update(self, update, dispatcher, check_result, context=None):
        chat_id, chat_state = self._get_chat_state(update)

        if not chat_state:
            new_state_key = self.entry_point.handle_update(update, dispatcher, check_result, context)

        else:
            new_state_key = chat_state.handle(update, dispatcher, context)

        if new_state_key:
            if new_state_key == self.BACK:
                self.chats_states[chat_id].pop()
                new_state_key = self.chats_states[chat_id].pop()

            self._activate_state(chat_id, new_state_key, update, context)

    def _get_chat_state(self, update):
        chat = update.effective_chat
        chat_states = self.chats_states.get(chat.id, None)

        if chat_states:
            chat_state_key = chat_states[-1]
            chat_state = self.states.get(chat_state_key, None)

            return chat.id, chat_state

        return chat.id, None

    def _activate_state(self, chat_id, state_key, update, context):
        state = self.states.get(state_key, None)

        if state:
            self.chats_states[chat_id].append(state_key)
            result_state_key = state.activate(update, context)

            if result_state_key:
                self._activate_state(chat_id, result_state_key, update, context)
