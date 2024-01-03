from aiogram.fsm.state import State, StatesGroup

class NeuroRequest(StatesGroup):
    request = State()
    chating = State()
    image_request = State()
    enchance_image = State()
    whisper = State()
    bender = State()

class AdminPanel(StatesGroup):
    find_user = State()