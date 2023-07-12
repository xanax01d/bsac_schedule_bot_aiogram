from aiogram import Router,F
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove, Update
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Filter
from aiogram.filters import MagicData
#импорты клавиатур
from keyboards.keyboards import *
from keyboards.keyboards_sso import *
from keyboards.keyboards_vo import *
#импорт групп
from configs.groups import courses_sso,courses_vo,levels,gr_list
from configs.admins import admin_ids,keyboard
from base.base_conn import BotDB

class user_level_course_group(StatesGroup):
    level = State()
    course = State()
    group = State()
    day = State()

router = Router()
#[хуйня,не трогать вообще нахуй)]
class BannedUsersFilter(Filter):
    def __init__(self, banned_users) -> None:
        self.banned_users = banned_users
    
    async def __call__(self, message:Message) -> bool:
        if message.from_user.id not in self.banned_users :
            return False
        return message.from_user.id in self.banned_users

banned_users = BotDB.get_banned_users()

@router.message(BannedUsersFilter(BotDB.get_banned_users()))
async def banned(message:Message):
    await message.reply(
        "<b>Вы заблокированы.</b>\nДля уточнения причины и возможности разблокировки,обратитесь к @xanax01d .",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Text(text = ("Назад"),ignore_case=True)) 
async def back(message: Message,state:FSMContext) -> None :
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
        "<b>Выберите ступень образования:</b> ",
        parse_mode="HTML",
        reply_markup=vo_or_sso(message.from_user.id)
    )
    await state.set_state(user_level_course_group.level)
@router.message(Command("start"))
async def cmd_start(message: Message,state:FSMContext) -> None:
    if BotDB.check_ban((message.from_user.id)) is None:
        BotDB.add_user_bans((message.from_user.id),(0),(message.from_user.first_name))
    if BotDB.check_chat_id((message.from_user.id)) is False:
        BotDB.add_user_chat_id((message.from_user.id),(message.chat.id))
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
    "<b>Выберите ступень образования:</b> ",
        parse_mode="HTML",
        reply_markup=vo_or_sso(message.from_user.id)
    )
    await state.set_state(user_level_course_group.level)
#вышка
@router.message(
        user_level_course_group.level,
        F.text.in_(levels[0])
)
async def vo(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def vo(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def vo(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def vo(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def vo(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def vo(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
    BotDB.add_user((message.from_user.id),(message.text),(message.from_user.username),(message.from_user.first_name),(message.chat.id))
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
async def sso(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def sso(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def sso(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def sso(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def sso(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def sso(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
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
async def SCHEDULE(message: Message,state:FSMContext) -> None:
    banned_users = BotDB.get_banned_users()
    await message.reply(BotDB.get_schedule(message.from_user.id,message.text))
    await state.set_state(user_level_course_group.day)

