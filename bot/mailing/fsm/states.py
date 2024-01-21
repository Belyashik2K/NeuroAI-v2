from aiogram.fsm.state import StatesGroup, State

class MailingState(StatesGroup):
    text = State()
    media = State()
    button_link = State()
    button_text = State()
    wb = State()