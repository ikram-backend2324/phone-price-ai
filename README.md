# 📱 PhonePrice AI

A Django web application that uses **Claude AI (via OpenRouter)** to estimate the market price of a smartphone from a photo.

## Features
- Upload a phone photo → get an AI-powered price estimate in USD
- Identifies brand, model, and condition automatically
- Confidence score for each estimate
- Dashboard with stats (avg price, avg confidence)
- **4 languages**: English, Uzbek, Russian, Qaraqalpaq (toggle in navbar)
- **Dark / Light theme** toggle (saved to localStorage)
- **Jazzmin admin panel** with dark theme and language switcher
- User authentication (register / login)

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 3. Compile translations
```bash
python manage.py compilemessages
```

### 4. Run migrations & seed data
```bash
python manage.py migrate
python manage.py create_default_superuser
python manage.py seed_brands
```

### 5. Run the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

## Default admin credentials
- **Username:** admin
- **Password:** admin123

## Language files location
All translation files are in `locale/<lang>/LC_MESSAGES/django.po`
After editing any `.po` file, run: `python manage.py compilemessages`

## Supported languages
| Code | Language    | Admin support |
|------|-------------|---------------|
| en   | English     | Full          |
| uz   | Uzbek       | Full          |
| ru   | Russian     | Full          |
| kaa  | Qaraqalpaq  | Content only  |
