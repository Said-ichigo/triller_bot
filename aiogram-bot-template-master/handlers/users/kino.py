
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.kino_a import moves_menu
from keyboards.inline.kino_b import kinolar_inline
from aiogram.dispatcher.filters import Command
from loader import dp 



@dp.message_handler(Text(equals="🎥kinolar"))
async def kin_po(message: types.Message, state: FSMContext):
    await message.answer("Bizde tomende kinolar bar:", reply_markup=kinolar_inline)

@dp.callback_query_handler(text='speder')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgIAAxkBAAEVS9ZkaJ06E2fUh6xWJCu62S338koBdwAC5TEAAoJdiUkZ5-MSUHnW_C8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2024-jildin bahar ayina shigadi!")

@dp.callback_query_handler(text='fast')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTChkaLnvYB0eTNKUmmHoKHIrB1p_dQACq-oAAgVISVNWTW8cIYPwBi8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2024-jilga shigadi!")

@dp.callback_query_handler(text='fast X')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTDJkaLvdCtaEtYSNDnwxQ6rg_peKNAACisgAAgVISVPglY24JyR8LC8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2023-jildin Jaz ayina shigadi!")

@dp.callback_query_handler(text='GXK')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTCZkaLmKjZ7aDg-FRbnrvHkQPgzH2AACye4AAgVISVOwdYopWT1Yoy8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2023-jilga shigadi!")

@dp.callback_query_handler(text='trans')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTDBkaLthiTmgtI9_pjHwqW2KlIv6kQACxPcAAgVISVOq-ZcciIxvhC8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2023-jilga Guz shigadiguz ayina shigadi!")

@dp.callback_query_handler(text='blue')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTCpkaLoilYBnSN8ymzdKHoa2Cw_QHwACH-oAAgVISVM4gb__Vj8h2C8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2024-jilga shigadi!")

@dp.callback_query_handler(text='moana')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTCxkaLpgCraX0JKfYie927pzB38hjQACp-kAAgVISVO-v6EwxZREUC8E')
    await call.message.answer("Eger kinoni korajaq bolsaniniz 2023-jilga shigadi qis ayinda shigadi!")


@dp.callback_query_handler(text='kill')
async def kin_pp(call: types.CallbackQuery):
    await call.message.answer_video('BAACAgQAAxkBAAEVTC5kaLrBeAjScNW2-nGHBK5eXuILywACOekAAgVISVPRcWAiOiJCUC8E')
    await call.message.answer(f"Egerkinoni korajaq bolsaninz bul saitqa otip kor👇")
    await call.message.answer(f'http://uzmovi.com/tarjima-kinolari/'
                              f'4526-uddalab-bolmas-topshiriq-7premeyra-uzbek-ozbek-tilida.html')

@dp.message_handler(Text(equals="🕹Oyin"))
async def game_lonj(message: types.Message):
    await message.answer(f"AWMET SIZGE {message.from_user.full_name} :)")
    await message.answer_dice('🎰')
    
@dp.message_handler(Command('locatcitya'))
async def kin_po(message: types.Message, state: FSMContext):
    await message.answer(f"{message.from_user.full_name} sizdin konta",reply_markup=moves_menu)