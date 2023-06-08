from aiogram import Router,F
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
#импорты клавиатур
from keyboards.keyboards import *
from keyboards.keyboards_sso import *
from keyboards.keyboards_vo import *
#импорт групп
from configs.groups import courses_sso,courses_vo,levels,gr_list

from bot import BotDB

router = Router()

class user_level_course_group(StatesGroup):
    level = State()
    course = State()
    group = State()
    day = State()

@router.message(Text(text = ("Назад"),ignore_case=True))
async def back(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите ступень образования:</b> ",
        parse_mode="HTML",
        reply_markup=vo_or_sso()
    )
    await state.set_state(user_level_course_group.level)
@router.message(Command("start"))
async def cmd_start(message: Message,state:FSMContext):
    BotDB.create_bases()
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите ступень образования:</b> ",
        parse_mode="HTML",
        reply_markup=vo_or_sso()
    )
    await state.set_state(user_level_course_group.level)
#вышка
@router.message(
        user_level_course_group.level,
        F.text.in_(levels[0])
)
async def vo(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите курс:</b> ",
        parse_mode="HTML",
        reply_markup=course_vo()
    )
    await state.set_state(user_level_course_group.course)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_vo[0])
)
async def vo(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgvo1()
    )
    await state.set_state(user_level_course_group.group)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_vo[1])
)
async def vo(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgvo2()
    )
    await state.set_state(user_level_course_group.group)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_vo[2])
)
async def vo(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgvo3()
    )
    await state.set_state(user_level_course_group.group)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_vo[3])
)
async def vo(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgvo4()
    )
    await state.set_state(user_level_course_group.group)

@router.message(
        user_level_course_group.group,
        F.text.in_(gr_list)
)
async def vo(message: Message,state:FSMContext):
    BotDB.add_user((message.from_user.id),(message.text),(message.from_user.username),(message.from_user.first_name))
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите день:</b> ",
        parse_mode="HTML",
        reply_markup=sday()
    )
    await state.set_state(user_level_course_group.day)

#ССО

@router.message(
        user_level_course_group.level,
        F.text.in_(levels[1])
)
async def sso(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите курс:</b> ",
        parse_mode="HTML",
        reply_markup=course_sso()
    )
    await state.set_state(user_level_course_group.course)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_sso[0])
)
async def sso(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgsso1()
    )
    await state.set_state(user_level_course_group.group)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_sso[1])
)
async def sso(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgsso2()
    )
    await state.set_state(user_level_course_group.group)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_sso[2])
)
async def sso(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgsso3()
    )
    await state.set_state(user_level_course_group.group)
@router.message(
        user_level_course_group.course,
        F.text.in_(courses_sso[3])
)
async def sso(message: Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите группу:</b> ",
        parse_mode="HTML",
        reply_markup=sgsso4()
    )
    await state.set_state(user_level_course_group.group)

@router.message(
        user_level_course_group.group,
        F.text.in_(gr_list)
)
async def sso(message: Message,state:FSMContext):
    BotDB.add_user((message.from_user.id),(message.text),(message.from_user.username),(message.from_user.first_name))
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите день:</b> ",
        parse_mode="HTML",
        reply_markup=sday()
    )
    await state.set_state(user_level_course_group.day)

@router.message(
        user_level_course_group.day,
        F.text.in_(days)
)
async def SCHEDULE(message: Message,state:FSMContext):
    await message.reply(BotDB.get_schedule(message.from_user.id,message.text))
    await state.set_state(user_level_course_group.day)
