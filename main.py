import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
import config as cfg
import markups as nav


logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_API)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Привет бро, если нужны какие то темки для поднятия денежек, жми на кнопку", reply_markup=nav.keyboard1)

################## ГЛАВНОЕ МЕНЮ ##################
@dp.callback_query_handler(text='showmenu')
async def show_main_menu(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    photo = open('MainMenu.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=nav.MainKeyboard)

################## МЕНЮ ДЛЯ ТЕМОК ##################
@dp.callback_query_handler(text='menutemki')
async def show_temki_menu(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    photo = open('TemkiMenu.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=nav.TemkiKeyboard)

################## ДОП РАЗДЕЛЫ ДЛЯ ТЕМОК (БЕСПЛАТНЫЕ) ##################
@dp.callback_query_handler(text='free')
async def show_temki_free(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    photo = open('TemkiMenu.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=nav.FreeTemkiKeyboard)

################## ДОП РАЗДЕЛЫ ДЛЯ ТЕМОК (ПЛАТНЫЕ) ##################
@dp.callback_query_handler(text='platno')
async def show_temki_free(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    photo = open('TemkiMenu.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=nav.PlatnoTemkiKeyboard)

#---------------- ИНСТАГРАММ ----------------#
@dp.callback_query_handler(text='instagram')
async def show_instagram(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Схема по прокачке и продаже аккаунтов инстаграм без вложений", reply_markup=nav.InstagamKeyboard)

@dp.callback_query_handler(text='buyinsta')
async def buyinsta(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Схема", description="Схема по заработку на инстаграме", payload="insta", provider_token=cfg.YOOKASSA_API, currency="RUB", start_parameter="test_bot", prices=[{"label":"rub", "amount":10000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):

    if message.successful_payment.invoice_payload == "insta":
      await bot.send_document(message.from_user.id, open("Прокачка и продажа аккаунтов Instagram без вложений.txt", "rb"))


#---------------- БУКСЫ -----------------#
@dp.callback_query_handler(text='buksi')
async def show_buksi(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    photo = open('Buksi.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, "   Буксы - это сайты, где исполнителям простых заданий в сети (лайки,просмотры,отзывы,подписки,регистрации и тд), платят реальные деньги. Количество заданий просто огромное, цены варьируются от 0.3 до 5000 за задание, если правильно подбирать задания, в день можно заработать ~ 300-500 рублей.  Прикреплю топ-3 буксов которыми пользуюсь сам.\n• SocPublic\n• Toloka\n• Seosprint\n   Первый, по моему мнению, самый удачный и простой.\n   А в платной группе выдам расширение и еще пару способов заработка на буксах, на полном пассиве\n   Так же, в телеграмме множество ботов, в которых за подписки реакции и просмотры платят реальные деньги, я пользуюсь этим : @TGSTAR (лучше не засорять личный аккаунт)")




if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
