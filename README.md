<!-- Banner Typing Animation -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=6C5CE7&center=true&vCenter=true&width=900&lines=🎓+MentorApprentice+Bot;🤝+Mentor+%26+Apprentice;💼+Job+%26+Partner+Search;📲+Telegram+Integration" alt="Typing SVG" />
</p>

---

# 🚀 MentorApprentice Bot

**MentorApprentice Bot** is a Telegram bot that helps users:  
- **Connect with mentors and apprentices**  
- **Find jobs or employees**  
- **Discover project partners**  

The bot is built using **Python** and **Aiogram v3**, and it uses **FSM (Finite State Machine)** to handle multi-step user interactions.

---

## 🧩 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Main bot file; runs the Dispatcher and manages all user interactions |
| `Register.py` | Defines FSM states (`StatesGroup`) for user registration (name, age, skills, phone, location, profession, etc.) |
| `Tugma.py` | Keyboard buttons and menus (`return_keyboards()` main menu, `confirmation_keyboard()` for confirmation) |
| `.env` | Stores bot TOKEN securely |

---

## 🎯 Key Features

- 👥 Connect mentors and apprentices  
- 💼 Match jobs and employees  
- 📝 Search for project partners  
- ✅ Multi-step form using FSM  
- 📞 Validate phone numbers  
- 🔄 Edit and confirm form submissions  
- 🌐 Specify location and skills  

---

## 🛠 Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-0088CC?style=for-the-badge&logo=python&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## ⚡ Core Concepts

- **FSM (Finite State Machine)** – handles multi-step user interactions  
- **Aiogram v3** – Telegram bot framework  
- **Environment Variables** – secure storage of bot TOKEN in `.env`  
- **Dynamic Keyboards** – main menu and confirmation buttons  
- **Data Formatting** – displays user input as clean messages  
- **Form Validation & Editing** – validates phone number, age, location, and skills  

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=BehruzMaxmudov1203&show_icons=true&theme=tokyonight" alt="GitHub Stats" /> 
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=BehruzMaxmudov1203&theme=tokyonight" alt="GitHub Streak" /> 
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=BehruzMaxmudov1203&theme=react-dark" alt="GitHub Activity Graph" /> 
</p>

---

## 🐙 GitHub

<p align="center"> ⭐️ Creator: <b>Behruz Maxmudov</b> — MentorApprentice Bot </p> 

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/username/MentorApprentice-Bot.git
cd MentorApprentice-Bot

# 2. Create and activate a virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and set your TOKEN
TOKEN="Your_Telegram_Bot_Token"

# 5. Run the bot
python main.py
