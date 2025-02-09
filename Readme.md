# 🎮 Tic Tac Toe Web Application

[![Django](https://img.shields.io/badge/Django-5.0-brightgreen.svg)](https://docs.djangoproject.com/en/5.0/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-%2346e3b7)](https://render.com)


A modern web-based implementation of the classic Tic Tac Toe game with real-time gameplay, animated interface, and game history tracking.

## 🌟 Features

- 🕹️ Player vs Player gameplay
- 🎨 Dynamic background animations based on game state
- 📊 Persistent game history tracking
- 🔊 Sound effects and click animations
- 📱 Responsive design for all screen sizes
- 🏆 Win detection and draw handling
- 🕹️ Interactive game board with hover effects
- 🌈 Color transitions and visual feedback

## 🚀 Deployment
The application is live at:  
https://tic-tac-toe-bmwl.onrender.com

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/N2B6/tic-tac-toe.git
cd tic-tac-toe
```

2. Set up virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start development server:
```bash
python manage.py runserver
```

## 🛠️ Technical Highlights

- **Django** backend with SQLite database
- **Whitenoise** for static file serving
- **CSS Animations** for smooth transitions
- **Responsive Design** with CSS Grid
- **Security Best Practices** (CSRF protection, XSS filters)
- **Production-ready configuration** with Render.com

## 📂 Project Structure

```
tic-tac-toe/
├── game/               # Main application
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── models.py       # Game model and logic
│   └── views.py        # Application views
├── tic_tac_toe/        # Project configuration
│   ├── settings.py     # Django settings
│   └── urls.py         # URL routing
└── manage.py           # Django CLI
```

## 🙏 Credits
Developed with ❤️ by **Nipun Bakshi**  
**Special Thanks:** Django community, Render.com for hosting
