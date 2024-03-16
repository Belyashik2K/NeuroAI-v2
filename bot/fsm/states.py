from aiogram.fsm.state import State, StatesGroup


class NeuroRequest(StatesGroup):
    request = State()
    image_request = State()
    bender = State()
    whisper = State()
    tencentmaker = State()
    midjourneyv6 = State()
    enchance_image = State()
    chating = State()
    t2g = State()
    i2i = State()


class AdminPanel(StatesGroup):
    find_user = State()
