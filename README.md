<!-- Banner Typing Animation -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=6C5CE7&center=true&vCenter=true&width=900&lines=🎓+UzToz+Shogirt+Bot;🤝+Ustoz+%26+Shogird;💼+Ish+%26+Sherik+Topish;📲+Telegram+Integratsiyasi" alt="Typing SVG" />
</p>

---

## 🚀 Loyiha haqida
**UzToz Shogirt Bot** – bu Telegram bot bo‘lib, foydalanuvchilarga **ustoz va shogirdlarni bog‘lash**, **ish joyi yoki xodim topish**, hamda **loyiha sheriklarini topish** imkoniyatini beradi.  

Foydalanuvchilar quyidagilarni qilishi mumkin:  
- 👨‍🏫 **Ustoz topish**  
- 🧑‍🎓 **Shogird topish**  
- 💼 **Ish yoki xodim topish**  
- 🤝 **Loyiha sherigi topish**  

Bot **Python** va **Aiogram v3** yordamida yozilgan, foydalanuvchi bosqichlarini boshqarish uchun **FSM (Finite State Machine)** ishlatilgan.

---

## 🧩 Loyiha tuzilishi

### 📘 1. `main.py`
- Botning asosiy fayli  
- Aiogram Dispatcher orqali botni ishga tushiradi  
- Foydalanuvchi bilan barcha interaktiv jarayonlarni boshqaradi  

### 📗 2. `Register.py`
- FSM holatlarini belgilaydi (`StatesGroup`)  
- Forma bosqichlari: ism, yosh, texnologiya, telefon, hudud, kasb va hokazo  

### 📙 3. `Tugma.py`
- Klaviatura tugmalari va menyular  
- `return_keyboards()` – asosiy menyu tugmalari  
- `confirmation_keyboard()` – tasdiqlash tugmalari  

### 📒 4. `.env`
- Bot TOKEN’ini xavfsiz saqlash uchun  
- Misol: `TOKEN="Sizning_Bot_Token"`

---

## 🎯 Asosiy funksiyalar

- 👥 Ustoz va shogirdlarni bog‘lash  
- 💼 Ish va xodimlarni bog‘lash  
- 📝 Loyiha sheriklarini qidirish  
- ✅ Ko‘p bosqichli forma (FSM)  
- 📞 Telefon raqamining tekshiruvi  
- 🔄 Forma qayta to‘ldirish va tasdiqlash  
- 🌐 Hudud va texnologiya kiriting  

---

## 🛠 Ishlatilgan texnologiyalar

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-0088CC?style=for-the-badge&logo=python&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## ⚡ Asosiy tushunchalar

- **FSM (Finite State Machine)** – foydalanuvchi bosqichlarini boshqaradi  
- **Aiogram v3** – Telegram bot yaratish uchun framework  
- **Environment Variables** – `.env` fayli orqali xavfsiz TOKEN saqlash  
- **Dinamik klaviaturalar** – asosiy menyu va tasdiqlash tugmalari  
- **Ma’lumotlarni formatlash** – foydalanuvchi kiritgan ma’lumotni chiroyli xabarga aylantiradi  
- **Forma qayta to‘ldirish va validatsiya** – telefon, yosh, hudud, texnologiya tekshiruvi  

---


<p align="center"> <img src="https://github-readme-stats.vercel.app/api?username=BehruzMaxmudov1203&show_icons=true&theme=tokyonight" alt="Behruz's GitHub stats" /> <img src="https://github-readme-streak-stats.herokuapp.com/?user=BehruzMaxmudov1203&theme=tokyonight" alt="GitHub Streak" /> </p> <p align="center"> <img src="https://github-readme-activity-graph.vercel.app/graph?username=BehruzMaxmudov1203&theme=react-dark" alt="GitHub Activity Graph" /> </p>


👨‍💻 Muallif

Behruz Maxmudov
📍 Uzbekistan
📧 behruzmaxmudov263@gmail.com

🐙 GitHub

<p align="center"> ⭐️ Yaratuvchi: <b>Behruz Maxmudov</b> — UzToz Shogirt Bot </p> ```

## 📦 O‘rnatish

```bash
# 1. Repozitoriyani klonlash
git clone https://github.com/username/UzToz-Shogirt-Bot.git
cd UzToz-Shogirt-Bot

# 2. Virtual muhit yaratish va faollashtirish
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. .env faylini yaratish va TOKEN qo‘yish
TOKEN="Sizning_Telegram_Bot_Token"

# 5. Botni ishga tushirish
python main.py




