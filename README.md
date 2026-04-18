# 🐦 TweetSite - Django Microblogging Web App

TweetSite is a microblogging web application built using Django.  
It allows users to create, manage, and share short posts (tweets) with optional image uploads, along with authentication and personalized user feeds.

This project was built to gain hands-on experience with Django’s core features including authentication, CRUD operations, media handling, and template rendering.

---

## ✨ Features

- 🔐 **User Authentication**
  - Sign up, login, logout functionality
  - Secure session handling

- 📝 **Tweet Management (CRUD)**
  - Create, edit, and delete tweets
  - Only authors can modify their own tweets

- 🖼️ **Media Upload**
  - Attach images to tweets
  - File handling using Django media system

- 📱 **Responsive UI**
  - Clean interface using Tailwind CSS

- 🧠 **Dynamic Templates**
  - Personalized dashboard
  - User-specific tweet feed

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Tailwind CSS  
- **Database:** SQLite (development)

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rudrah001/TweetSite.git
cd TweetSite
```

### Step 2: Create Virtual Environment
 
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### Step 3: Install Dependencies
 
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
 
```bash
python manage.py migrate
```

### Step 5: Start Server
 
```bash
python manage.py runserver
```

## ⚠️ Limitations
 
- No pagination for tweets
- Basic UI (can be enhanced further)
- SQLite used (not production-ready)

## 🔮 Future Improvements

- Add likes and comments system
- Implement pagination/infinite scroll
- Deploy with PostgreSQL
- Improve UI/UX
- Add user profiles

## 📌 Author 

**Author**: Tushar
**Email**: rudrahpratap@gmail.com
**GitHub**: https://github.com/Rudrah001