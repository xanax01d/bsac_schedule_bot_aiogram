from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from configs.groups import level_vo,level_sso,courses_vo,courses_sso,days,gr_list_1course_vo,gr_list_1course_sso,gr_list_2course_vo,gr_list_2course_sso,gr_list_3course_vo,gr_list_3course_sso,gr_list_4course_vo,gr_list_4course_sso


def vo_or_sso() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = level_vo)
    kb.button(text = level_sso)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)


def sday() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(days)):
        kb.button(text = days[i])
    kb.button(text = 'Назад')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard = True)