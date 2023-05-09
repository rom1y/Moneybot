from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import config as cfg


################################################
keyboard1 = InlineKeyboardMarkup(row_width=1)

btnZarabotat = InlineKeyboardButton(text = "Заработать💰", callback_data='showmenu')
keyboard1.insert(btnZarabotat)

################################################
MainKeyboard = InlineKeyboardMarkup(row_width=2)

btnChat = InlineKeyboardButton(text="Наш чат", url=cfg.CPA_CHAT)
btnChannel = InlineKeyboardButton(text="Наш канал", url=cfg.CPA_CHANNEL)
btnSkhemy = InlineKeyboardButton(text="Темки💵", callback_data='menutemki')
btnSoft = InlineKeyboardButton(text="Софт⚙️", url=cfg.CPA_CHAT)   #поменять ссылку
btnPrivateSub = InlineKeyboardButton(text="Подписка🔑", url=cfg.CPA_CHAT)   #поменять ссылку
btnSupport = InlineKeyboardButton(text="Поддержка❔", url="https://t.me/pax_manager")

MainKeyboard.insert(btnChat)
MainKeyboard.insert(btnChannel)
MainKeyboard.insert(btnSkhemy)
MainKeyboard.insert(btnSoft)
MainKeyboard.insert(btnPrivateSub)
MainKeyboard.insert(btnSupport)

################################################
TemkiKeyboard = InlineKeyboardMarkup(row_width=1)

btnFree = InlineKeyboardButton(text="Бесплатные", callback_data='free')
btnPlatno = InlineKeyboardButton(text="Платные", callback_data='platno')
btnBack1 = InlineKeyboardButton(text="Назад🔙", callback_data='showmenu')

TemkiKeyboard.insert(btnFree)
TemkiKeyboard.insert(btnPlatno)
TemkiKeyboard.insert(btnBack1)

################################################
FreeTemkiKeyboard = InlineKeyboardMarkup(row_width=2)

btnTemka1 = InlineKeyboardButton(text="Буксы", callback_data='buksi')
btnBack2 = InlineKeyboardButton(text="Назад🔙", callback_data='menutemki')

FreeTemkiKeyboard.insert(btnTemka1)
FreeTemkiKeyboard.insert(btnBack2)

################################################
PlatnoTemkiKeyboard = InlineKeyboardMarkup(row_width=2)

btnInstagram = InlineKeyboardButton(text="Прокачка аккаунтов инстаграм", callback_data='instagram')

PlatnoTemkiKeyboard.insert(btnInstagram)
PlatnoTemkiKeyboard.insert(btnBack2)

#temka insagram
InstagamKeyboard = InlineKeyboardMarkup(row_width=1)

btnBuyInstagram = InlineKeyboardButton(text="Купиь за 100 р.", callback_data='buyinsta')

InstagamKeyboard.insert(btnBuyInstagram)
InstagamKeyboard.insert(btnBack2)