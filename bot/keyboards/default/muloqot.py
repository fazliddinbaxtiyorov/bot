from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

hello = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Assalomu Aleykum')]
    ], resize_keyboard=True
)

ustozlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨🏻‍💼Matematika")], [KeyboardButton(text="👨🏻‍💼Ingliz tili")],
        [KeyboardButton(text="💻Dasturlash")], [KeyboardButton(text="◀️Ortga")]
    ], resize_keyboard=True
)

haqimiz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📤Biz haqimizda"), KeyboardButton(text="📚O'quv kursimiz"),
            KeyboardButton(text="👨🏻‍💼O'qituvchilarimiz")], [KeyboardButton(text="📞Biz bilan aloqa")
                                                            ],
    ], resize_keyboard=True
)

malumot = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🌍Ingliz Tili')],
        [KeyboardButton(text='🧮Matematika')], [KeyboardButton(text='👨🏻‍💻Dasturlash')],
        [KeyboardButton(text="◀️Ortga")]
    ]
)

eng = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘Beginner")], [KeyboardButton(text="🔝Elementary")],
        [KeyboardButton(text="📒Pre-Intermadite")], [KeyboardButton(text="📚Intermadite")],
        [KeyboardButton(text='◀️Ortga')]
    ]
)

kun = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌔Toq kunlari")], [KeyboardButton(text="🌒Juft kunlari")], [KeyboardButton(text='◀️Ortga')]
    ], resize_keyboard=True
)

vaqt = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌕Ertalab")], [KeyboardButton(text="🌑Kechki")]
    ], resize_keyboard=True
)

soat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⏳14:00dan 16:00gacha")], [KeyboardButton(text="⏳16:00dan 18:00gacha")],
        [KeyboardButton(text='⏳18:00dan 20:00gacha')]

    ], resize_keyboard=True
)

soat2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⏳10:00dan 12:00gacha")], [KeyboardButton(text="⏳12:00dan 14:00gacha")],
        [KeyboardButton(text='⏳14:00dan 16:00gacha')]

    ], resize_keyboard=True
)

telefon = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞Telefon raqam", request_contact=True)]
    ], resize_keyboard=True
)

foydalanuvchi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='')]
    ], resize_keyboard=True
)

IT = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⌨️Fronted")], [KeyboardButton(text="💻Backend")]
    ], resize_keyboard=True
)
toplam = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📃Oq to'plam")], [KeyboardButton(text="📗Yashil to'plam")]
    ], resize_keyboard=True
)
