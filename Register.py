from aiogram.fsm.state import State, StatesGroup

class GeneralForm(StatesGroup):
    name = State()
    age = State()
    technology = State()
    phone = State()
    region = State()
    price = State()
    job = State()
    time = State()
    goal = State()
    telegram = State()
    company = State()
    manager = State()
    work_time = State()
    salary = State()
    extra = State()

    confirmation = State()