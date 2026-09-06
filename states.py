from aiogram.fsm.state import State, StatesGroup


class AdminStates(StatesGroup):
    broadcast_wait_message = State()
    addchannel_wait_id = State()
    addchannel_wait_title = State()
    addmodel_wait_name = State()
    addmodel_wait_text = State()
