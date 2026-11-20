# Zubair Tahir — Django Portfolio

A personal portfolio built with **Django 6.1**, served with **Gunicorn** and **WhiteNoise**, ready to deploy on **Railway**.

Pages: Home · About · Projects · Contact (plus downloadable CV).

## Run locally

```bash
python -m venv venv
venv\Scripts\activate          # Windows   (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py runserver
```

Open http://127.0.0.1:8000 (requires **Python 3.12+**).

## Deploy on Railway

1. Push this folder's contents to a GitHub repo (`manage.py` must be at the repo root).
2. Railway → **New Project → Deploy from GitHub repo** → select the repo.
3. Open the service → **Variables** → add:

   | Variable | Value |
   |---|---|
   | `SECRET_KEY` | a long random string (see below) |

   `DEBUG` is automatically **off** on Railway. Optional: `CUSTOM_DOMAIN` = your own domain.
4. **Settings → Networking → Generate Domain**. Done.

Generate a secret key:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## Project layout

```
manage.py
requirements.txt     # dependencies
.python-version      # Python 3.12 (Django 6.1 needs >= 3.12)
Procfile             # start command (migrate + gunicorn)
railway.json         # build (collectstatic) + deploy config
portfolio/           # project settings & URLs
pages/               # app: views, templates, static (CSS, photo, CV)
```

## Author

Zubair Tahir — [GitHub](https://github.com/zubairtahir17-ops) · [LinkedIn](https://www.linkedin.com/in/zubair-tahir-95b393318)
