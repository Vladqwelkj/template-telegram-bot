from typing import Callable, List

from telegram.ext import Handler


class State:
    def __init__(self, on_activate: Callable, handlers: List[Handler]):
        self.on_activate = on_activate
        self.handlers = handlers

    def activate(self, update, context):
        return self.on_activate(update, context)

    def handle(self, update, dispatcher, context=None):
        for candidate_helper in self.handlers:
            check = candidate_helper.check_update(update)
            if check:
                return candidate_helper.handle_update(update, dispatcher, check, context)
