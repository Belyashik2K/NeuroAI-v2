from aiogram.fsm.state import State, StatesGroup

class NeuroRequest(StatesGroup):
    request = State()
    image_request = State()
    bender = State()
    whisper = State()
    tencentmaker = State()
    chating = State()

class AdminPanel(StatesGroup):
    find_user = State()