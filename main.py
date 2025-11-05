import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Register import GeneralForm
from Tugma import return_keyboards,confirmation_keyboard

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()


# --- Yordamchi funksiyalar ---
async def start_registration(message: types.Message, state: FSMContext, form_type: str, first_prompt: str):
    await state.clear()
    await state.set_data({'form_type': form_type, 'chat_id': message.from_user.id})
    await message.answer(first_prompt)


async def next_step(message: types.Message, state: FSMContext, data_key: str, next_state: State, prompt: str):
    await state.update_data(**{data_key: message.text})
    await message.answer(prompt)
    await state.set_state(next_state)


def format_final_text(data: dict) -> str:
    form_type = data.get('form_type', 'Ma\'lumot')

    mapping = {
        'Sherik kerak': {
            'name': '🏅 Sherik', 'technology': '📚 Texnologiya', 'telegram': '🇺🇿 Telegram',
            'phone': '📞 Aloqa', 'region': '🌐 Hudud', 'price': '💰 Narxi',
            'job': '👨🏻‍💻 Kasbi', 'time': '🕰 Murojaat vaqti', 'goal': '🔎 Maqsad'
        },
        'Ish joyi kerak': {
            'name': '🏅 Ishchi', 'age': '🎂 Yosh', 'technology': '📚 Texnologiya',
            'phone': '📞 Aloqa', 'region': '🌐 Hudud', 'price': '💰 Narxi',
            'job': '👨🏻‍💻 Kasbi', 'time': '🕰 Murojaat vaqti', 'goal': '🔎 Maqsad'
        },
        'Xodim': {
            'company': '🏢 Idora nomi', 'technology': '📚 Texnologiya',
            'phone': '📞 Aloqa', 'region': '🌐 Hudud', 'manager': '✍️ Mas’ul',
            'time': '🕰 Murojaat vaqti', 'work_time': '⏳ Ish vaqti',
            'salary': '💰 Maosh', 'extra': '‼️ Qo‘shimcha ma’lumot'
        },
        'Ustoz kerak': {
            'name': '🎓 Shogird', 'age': '🕑 Yosh', 'technology': '📚 Texnologiya',
            'phone': '📞 Aloqa', 'region': '🌐 Hudud', 'job': '👨🏻‍💻 Kasbi',
            'time': '🕰 Murojaat vaqti', 'goal': '🔎 Maqsad'
        },
        'Shogird kerak': {
            'name': '🎓 Shogird', 'age': '🕑 Yosh', 'technology': '📚 Texnologiya',
            'telegram': '🇺🇿 Telegram', 'phone': '📞 Aloqa', 'region': '🌐 Hudud',
            'price': '💰 Narxi', 'job': '👨🏻‍💻 Kasbi', 'time': '🕰 Murojaat vaqti',
            'goal': '🔎 Maqsad'
        }
    }

    fields = mapping.get(form_type, {})
    text = f"--- {form_type} ---\n\n"
    for key, label in fields.items():
        value = data.get(key, 'Kiritilmagan')
        text += f"{label}: {value}\n"

    return text


# --- Handlers ---
@dp.message(Command('start'))
async def greeting(message: types.Message):
    await message.answer(
        text=f"Assalom alaykum {message.from_user.username} Birga O‘rganamiz kanalining rasmiy botiga xush kelibsiz!",
        reply_markup=return_keyboards()
    )


@dp.message(F.text == "Sherik kerak", StateFilter("*"))
async def start_sherik(message: types.Message, state: FSMContext):
    await start_registration(message, state, "Sherik kerak", "🏅 Ismingizni kiriting:")
    await state.set_state(GeneralForm.name)


@dp.message(F.text == "Ish joyi kerak", StateFilter("*"))
async def start_ish(message: types.Message, state: FSMContext):
    await start_registration(message, state, "Ish joyi kerak", "🏅 Ismingizni kiriting:")
    await state.set_state(GeneralForm.name)


@dp.message(F.text == "Xodim", StateFilter("*"))
async def start_hodim(message: types.Message, state: FSMContext):
    await start_registration(message, state, "Xodim", "🏢 Idora nomini kiriting:")
    await state.set_state(GeneralForm.company)


@dp.message(F.text == "Ustoz kerak", StateFilter("*"))
async def start_ustoz(message: types.Message, state: FSMContext):
    await start_registration(message, state, "Ustoz kerak", "👤 Ism, familiyangizni kiriting:")
    await state.set_state(GeneralForm.name)


@dp.message(F.text == "Shogird kerak", StateFilter("*"))
async def start_shogird(message: types.Message, state: FSMContext):
    await start_registration(message, state, "Shogird kerak", "👤 Ism, familiyangizni kiriting:")
    await state.set_state(GeneralForm.name)


# --- Universal Bosqichlar ---
@dp.message(GeneralForm.name)
async def process_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('form_type') in ["Sherik kerak", "Ish joyi kerak"]:
        await next_step(message, state, 'name', GeneralForm.technology, "📚 Qaysi texnologiyalarni bilasiz?")
    else:  # Ustoz kerak, Shogird kerak
        await next_step(message, state, 'name', GeneralForm.age, "🕑 Yoshingizni kiriting?\nMasalan: 19")


@dp.message(GeneralForm.age)
async def process_age(message: types.Message, state: FSMContext):
    await next_step(message, state, 'age', GeneralForm.technology,
                    "📚 Talab qilinadigan texnologiyalarni kiriting:\nTexnologiya nomlarini vergul bilan ajrating. Masalan:\nJava, C++, C#")


@dp.message(GeneralForm.technology)
async def process_technology(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('form_type') in ["Sherik kerak", "Ish joyi kerak"]:
        await next_step(message, state, 'technology', GeneralForm.telegram, "🇺🇿 Telegram username’ingizni kiriting:")
    elif data.get('form_type') == "Xodim":
        await next_step(message, state, 'technology', GeneralForm.phone,
                        "📞 Bog‘lanish uchun raqamingizni kiriting?\nMasalan: +998 90 123 45 67")
    else:  # Ustoz kerak, Shogird kerak
        await next_step(message, state, 'technology', GeneralForm.phone,
                        "📞 Bog‘lanish uchun raqamingizni kiriting?\nMasalan: +998 90 123 45 67")


@dp.message(GeneralForm.telegram)
async def process_telegram(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('form_type') == "Sherik kerak":
        await next_step(message, state, 'telegram', GeneralForm.phone, "📞 Telefon raqamingizni kiriting:")
    else:  # Shogird kerak
        await next_step(message, state, 'telegram', GeneralForm.phone,
                        "📞 Aloqa: \n\nBog‘lanish uchun raqamingizni kiriting?\nMasalan: +998 90 123 45 67")


@dp.message(GeneralForm.phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip().replace(" ", "")
    if not (phone.startswith('+') and phone[1:].isdigit() and 9 <= len(phone) <= 15):
        return await message.answer("❌ Telefon raqam noto‘g‘ri formatda. Masalan: +998901234567")

    data = await state.get_data()
    prompt = "🌐 Qaysi hududdansiz?"
    if data.get('form_type') == "Xodim":
        prompt = "🌐 Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting"

    await next_step(message, state, 'phone', GeneralForm.region, prompt)


@dp.message(GeneralForm.region)
async def process_region(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('form_type') in ["Sherik kerak", "Ish joyi kerak", "Shogird kerak"]:
        await next_step(message, state, 'region', GeneralForm.price,
                        "💰 Narxni kiriting (agar bepul bo‘lsa, 'Bepul' deb yozing):")
    elif data.get('form_type') == "Ustoz kerak":
        await next_step(message, state, 'region', GeneralForm.job,
                        "👨🏻‍💻 Kasbingizni yozing (Talaba, ishchi va h.k.):")
    else:  # Xodim
        await next_step(message, state, 'region', GeneralForm.manager, "✍️ Mas’ul ism sharifini kiriting:")


@dp.message(GeneralForm.price)
async def process_price(message: types.Message, state: FSMContext):
    await next_step(message, state, 'price', GeneralForm.job,
                    "👨🏻‍💻 Kasbingizni kiriting (Talaba, Dasturchi, va h.k.):")


@dp.message(GeneralForm.job)
async def process_job(message: types.Message, state: FSMContext):
    await next_step(message, state, 'job', GeneralForm.time, "🕰 Qaysi vaqtda murojaat qilish mumkin?")


@dp.message(GeneralForm.time)
async def process_time(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('form_type') == "Xodim":
        await next_step(message, state, 'time', GeneralForm.work_time, "⏳ Ish vaqtini kiriting:")
    else:
        await next_step(message, state, 'time', GeneralForm.goal, "🔎 Maqsadingizni yozing:")


@dp.message(GeneralForm.goal)
async def process_goal(message: types.Message, state: FSMContext):
    await state.update_data(goal=message.text)
    data = await state.get_data()

    final_text = format_final_text(data)
    await message.answer(
        f"Kiritilgan ma'lumotlar to'g'rimi? 👇\n\n{final_text}",
        reply_markup=confirmation_keyboard()
    )
    await state.set_state(GeneralForm.confirmation)


@dp.message(GeneralForm.company)
async def process_company(message: types.Message, state: FSMContext):
    await next_step(message, state, 'company', GeneralForm.technology,
                    "📚 Talab qilinadigan texnologiyalarni kiriting:\n\nTexnologiya nomlarini vergul bilan ajrating. Masalan:\nJava, C++, C#")


@dp.message(GeneralForm.manager)
async def process_manager(message: types.Message, state: FSMContext):
    await next_step(message, state, 'manager', GeneralForm.time,
                    "🕰 Qaysi vaqtda murojaat qilish mumkin?\nMasalan: 9:00 - 18:00")


@dp.message(GeneralForm.work_time)
async def process_work_time(message: types.Message, state: FSMContext):
    await next_step(message, state, 'work_time', GeneralForm.salary, "💰 Maoshni kiriting:")


@dp.message(GeneralForm.salary)
async def process_salary(message: types.Message, state: FSMContext):
    await next_step(message, state, 'salary', GeneralForm.extra, "‼️ Qo‘shimcha ma’lumotlarni kiriting:")


@dp.message(GeneralForm.extra)
async def process_extra(message: types.Message, state: FSMContext):
    await state.update_data(extra=message.text)
    data = await state.get_data()

    final_text = format_final_text(data)
    await message.answer(
        f"Kiritilgan ma'lumotlar to'g'rimi? 👇\n\n{final_text}",
        reply_markup=confirmation_keyboard()
    )
    await state.set_state(GeneralForm.confirmation)


# --- Tasdiqlash va Qayta To'ldirish Handler'lari ---
@dp.message(GeneralForm.confirmation, F.text == "✅ Ha, to'g'ri")
async def finish_registration(message: types.Message, state: FSMContext):
    data = await state.get_data()
    final_text = format_final_text(data)

    await message.answer("✅ Ma'lumotlaringiz muvaffaqiyatli qabul qilindi!", reply_markup=return_keyboards())
    await state.clear()


@dp.message(GeneralForm.confirmation, F.text == "🔄 Qayta to'ldirish")
async def restart_registration(message: types.Message, state: FSMContext):
    data = await state.get_data()
    form_type = data.get('form_type')

    # Har bir forma turiga qarab qayta boshlash uchun xabar
    restart_message_map = {
        'Sherik kerak': "📝 Qayta to'ldirish uchun ismingizni kiriting:",
        'Ish joyi kerak': "📝 Qayta to'ldirish uchun ismingizni kiriting:",
        'Xodim': "📝 Qayta to'ldirish uchun idora nomini kiriting:",
        'Ustoz kerak': "📝 Qayta to'ldirish uchun ism, familiyangizni kiriting:",
        'Shogird kerak': "📝 Qayta to'ldirish uchun ism, familiyangizni kiriting:",
    }

    await message.answer(
        restart_message_map.get(form_type, "📝 Ma'lumotlarni qayta kiritishingiz mumkin. Boshidan boshlaymiz."),
        reply_markup=types.ReplyKeyboardRemove()
    )
    # Tegishli holatga o'tkazish
    if form_type == "Xodim":
        await state.set_state(GeneralForm.company)
    else:
        await state.set_state(GeneralForm.name)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())