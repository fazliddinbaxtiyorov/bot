from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from loader import dp
from keyboards.default.muloqot import malumot, eng, kun, vaqt, soat, soat2, telefon, IT, toplam, foydalanuvchi, haqimiz, \
    ustozlar

from keyboards.inline.malumot import tel


@dp.message_handler(text='Assalomu Aleykum')
async def hello(msg: types.message):
    await msg.answer("Xush kelibsiz o'zingiz qiziqqan kursga tegishli ma'lumotni tanlang!", reply_markup=haqimiz)


users = {}


# @dp.message_handler(text="Bizning kurslar haqida ma'lumot📚")
# async def kursla(msg: types.message):
#     await msg.answer("Qaysi kurs haqida ma'lumot kerak:", reply_markup=tanla)
#
#


@dp.message_handler(text="👨🏻‍💼O'qituvchilarimiz")
async def ustoz(msg: types.message):
    await msg.answer("Ustozlarimiz haqida ma'lumotlar: ", reply_markup=ustozlar)


@dp.message_handler(text="👨🏻‍💼Matematika")
async def usma(msg: types.message):
    await msg.answer_photo("https://media.hswstatic.com"
                           "/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL3BsYXlcL2FjZTllZjk2LTc4MDUtNDY5OS1iYjU3LWUwMWJhNTg4NjJkZS0xOTIwLTEwODAuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjoiMTIwMCJ9fX0=",
                           "Matematika haqidagi fikringizni o'zgartirib yuboramiz!🧮 Matematika haqida gap boshlansa "
                           "ufff, obbo,"
                           "men uchun emas deymiz. Shoshilmang, bizning ustozlarimiz sizni xecham zeriktirmaydi!📌 "
                           "Respublika Olimpiada"
                           "g'olibidan:- 0 dan fundamentalgacha (DTM) kurslari"
                           "- SAT (math) 700+ sertifikati uchun tayyorlov kurslari 📍  21 - maktab yoni | 9 - damas yo'li (67)☎️ 70-204-04-88")


@dp.message_handler(text="💻Dasturlash")
async def das(msg: types.message):
    await msg.answer_photo("https://kartinkin.net/uploads/posts/2022-02/1645236094_42-kartinkin-net-p-programmist"
                           "-kartinki-45.jpg", "Hamma dasturchi bo'la oladi(mi?)📚 Biz sizni dasturchi qilamiz. " \
                                               "Buning uchun sizda kuchli xohish bo'lsa bas! 🖇 O'quvchilarini " \
                                               "hayotga tayyorlaydigan, jamoaviy ishlashni, ta'lim va tarbiyani " \
                                               "beruvchi 80% amaliy darslarga marhamat.📌 O'zbekiston va dunyo " \
                                               "kompaniyalari uchun tayyorlanasiz:"
                                               " Frontend  "
                                               "Backend  "
                                               "Interview cracking " 
                                               "📍 21-maktab yoni | (67)☎️ 70-204-04-88")


@dp.message_handler(text="👨🏻‍💼Ingliz tili")
async def engus(msg: types.message):
    await msg.answer_photo("https://rskrf.ru/upload/iblock/138/138a580edb1881a819d33a7adda5f9e9.jpg", "IELTS olish "
                                                                                                      "sizga nima "
                                                                                                      "beradi? 📃 "
                                                                                                      "IELTS bo'lsa, "
                                                                                                      "demak SAT-Math "
                                                                                                      "sertifikatini "
                                                                                                      "olish ham "
                                                                                                      "sizga проблема "
                                                                                                      "bo'lmaydi. 🗝 "
                                                                                                      "Bu esa TOP "
                                                                                                      "universitetlarda bemalol grantda o'qish mumkin degani. Qolaversa dunyo eshiklari siz uchun tekinga ochiladi.🔖 Bizda IELTS guruhlariga qabul boshlandi. Guruhlar Pre-Intermediate darajadan 4 oyda natijaga olib chiqiladi.📌 Sababi 4 kishilik mini guruhlarda har bir talaba bilan individual ishlanadi.✅ Bilim darajangizni aniqlang va IELTS'ga tayyorlaning. Biz siz uchun barcha imkoniyatlarni yaratib beramiz")


@dp.message_handler(text="📚O'quv kursimiz")
async def kurs(msg: types.message):
    await msg.answer("Kurslardan birini tanlang: ", reply_markup=malumot)


@dp.message_handler(text="📞Biz bilan aloqa")
async def biz(msg: types.message):
    await msg.answer("Shu raqamga murojaat qilishingiz mumkin: +998 94 407 77 88")

@dp.message_handler(text='📤Biz haqimizda')
async def haqida(msg: types.message):
    await msg.answer("Kutib oling, ixtisoslashgan o'quv markaz!🤩 Olmaliq shahrida ilk bora "
                     "ixtisoslashgan o'quv markaz Elite Modern School📍 21-maktab yonida | 9-damas "
                     "yo'li (67)")


@dp.message_handler(text='🌍Ingliz Tili')
async def english(msg: types.message):
    await msg.answer("Ingliz tili kursini turini tanlang: ", reply_markup=eng)


@dp.message_handler(text="📘Beginner")
async def begin(msg: types.message):
    await msg.answer("Qaysi Kunlarini tanaysiz: ", reply_markup=kun)


@dp.message_handler(text="🔝Elementary")
async def begin(msg: types.message):
    await msg.answer("Qaysi Kunlarini tanaysiz: ", reply_markup=kun)


@dp.message_handler(text="📒Pre-Intermadite")
async def begin(msg: types.message):
    await msg.answer("Qaysi Kunlarini tanaysiz: ", reply_markup=kun)


@dp.message_handler(text="📚Intermadite")
async def begin(msg: types.message):
    await msg.answer("Qaysi Kunlarini tanaysiz: ", reply_markup=kun)


@dp.message_handler(text="◀️Ortga")
async def back(msg: types.message):
    await msg.answer('🏠Bosh Menu', reply_markup=haqimiz)


@dp.message_handler(text='🌔Toq kunlari')
async def toq(msg: types.message):
    await msg.answer("Ertalab yoki Kechki: ", reply_markup=vaqt)


@dp.message_handler(text='🌒Juft kunlari')
async def toq(msg: types.message):
    await msg.answer("Ertalab yoki Kechki: ", reply_markup=vaqt)


@dp.message_handler(text="🌕Ertalab")
async def erta(msg: types.message):
    await msg.answer("Vaqtini tanlang:", reply_markup=soat2)


@dp.message_handler(text="🌑Kechki")
async def kech(msg: types.message):
    await msg.answer("Vaqtini tanlang: ", reply_markup=soat)


@dp.message_handler(text="⏳14:00dan 16:00gacha")
async def ism0(msg: types.message):
    await msg.answer("Hop ismingizni kiriting: ", reply_markup=foydalanuvchi)


@dp.message_handler(text="⏳10:00dan 12:00gacha")
async def ism8(msg: types.message):
    await msg.answer("Hop ismingizni kiriting: ", reply_markup=foydalanuvchi)


@dp.message_handler(text="⏳12:00dan 14:00gacha")
async def ism4(msg: types.message):
    await msg.answer("Hop ismingizni kiriting: ", reply_markup=foydalanuvchi)


@dp.message_handler(text="⏳16:00dan 18:00gacha")
async def ism3(msg: types.message):
    await msg.answer("Hop ismingizni kiriting: ", reply_markup=foydalanuvchi)


@dp.message_handler(text="⏳18:00dan 20:00gacha")
async def vaqt2(msg: types.message):
    await msg.answer("Hop ismingizni kiriting: ", reply_markup=foydalanuvchi)


@dp.message_handler(text={telefon})
async def aloqa(msg: types.message):
    await msg.answer("Rahmat sog' bo'ling sizga tez orada aloqaga chiqamiz !")


@dp.message_handler(text="👨🏻‍💻Dasturlash")
async def choose(msg: types.message):
    await msg.answer("Dasturlash Levelingizni tanlang: ", reply_markup=IT)


@dp.message_handler(text="⌨️Fronted")
async def dastur(msg: types.message):
    await msg.answer("Hop qaysi kunlarni tanlaysiz: ", reply_markup=kun)


@dp.message_handler(text="💻Backend")
async def dastur(msg: types.message):
    await msg.answer("Hop qaysi kunlarni tanlaysiz: ", reply_markup=kun)


@dp.message_handler(text="🌔Toq kunlari")
async def darkun(msg: types.message):
    await msg.answer("Endi esa vaqtini tanlang: ", reply_markup=vaqt)


@dp.message_handler(text="🌒Juft kunlari")
async def dastujuf(msg: types.message):
    await msg.answer("Endi esa vaqtini tanlang: ", reply_markup=vaqt2)


@dp.message_handler(text="🌕Ertalab")
async def dasturku(msg: types.message):
    await msg.answer("Sizga qaysi soat maqul: ", reply_markup=soat2)


@dp.message_handler(text="🌑Kechki")
async def dasturku(msg: types.message):
    await msg.answer("Sizga qaysi soat maqul: ", reply_markup=soat)


@dp.message_handler(text="🧮Matematika")
async def matem(msg: types.message):
    await msg.answer("Matematika kitob turini tanlang: ", reply_markup=toplam)


@dp.message_handler(text="📃Oq to'plam")
async def matemoq(msg: types.message):
    await msg.answer("O'zingizga qulay kunlarni tanlang: ", reply_markup=kun)


@dp.message_handler(text="📗Yashil to'plam")
async def matemyashil(msg: types.message):
    await msg.answer("O'zingizga qulay kunlarni tanlang: ", reply_markup=kun)


@dp.message_handler(text="🌔Toq kunlari")
async def matemtoq(msg: types.message):
    await msg.answer("Endi esa vaqtini tanlang: ", reply_markup=vaqt)


@dp.message_handler(text="🌒Juft kunlari")
async def matemjut(msg: types.message):
    await msg.answer("Endi esa vaqtini tanlang: ", reply_markup=vaqt2)


@dp.message_handler(text="🌕Ertalab")
async def ertamate(msg: types.message):
    await msg.answer("Sizga qaysi soat maqul: ", reply_markup=soat2)


@dp.message_handler(text="🌑Kechki")
async def matemku(msg: types.message):
    await msg.answer("Sizga qaysi soat maqul: ", reply_markup=soat)


@dp.message_handler(text=None)
async def qir(msg: types.message):
    await msg.answer("Ismingiz saqlandi, endi Telefon raqamingizni yuboring!", reply_markup=telefon)


@dp.message_handler(text="📞Telefon raqam")
async def qabul(msg: types.message):
    await msg.answer("Sizning ma'lumotingiz saqlandi va o'zimiz sizga aloqaga chiqamiz !")
