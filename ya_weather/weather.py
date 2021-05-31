from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from ya_weather.auth import login_required
from ya_weather.db import get_db

bp = Blueprint('weather', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT w.id, created, condition, temperature, city, author_id, username'
        ' FROM weather w JOIN user u ON w.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('index.html', posts=posts)


