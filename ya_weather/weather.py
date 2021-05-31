from flask import (Blueprint, g, render_template, Response, redirect)

from ya_weather.auth import login_required
from ya_weather.csv_maker import csv_maker
from ya_weather.db import get_db
from ya_weather.req_forecast import dump_request

bp = Blueprint('weather', __name__)


def all_posts():
    db = get_db()
    posts = db.execute(
        'SELECT w.id, created, cit_1, cit_2, cit_3, cit_4, cit_5, temp_1, temp_2, temp_3, temp_4, temp_5, f_l_1, f_l_2, f_l_3, f_l_4, f_l_5, con_1, con_2, con_3, con_4, con_5, author_id, username'
        ' FROM weather w JOIN user u ON w.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return posts


@bp.route('/')
def index():
    return render_template('index.html', posts=all_posts(), actual=all_posts()[0])


@bp.route('/refresh', methods=('GET', 'POST'))
def refresh():
    return redirect('/')


@bp.route('/<int:id>/download', methods=('GET', 'POST'))
def download_csv(id):
    len_posts = len(all_posts())
    post = all_posts()[len_posts - id]

    csv = csv_maker(post)
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename=ya_weather_data.csv"})


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    dump = dump_request()

    cit_1 = dump[0]['city']
    cit_2 = dump[1]['city']
    cit_3 = dump[2]['city']
    cit_4 = dump[3]['city']
    cit_5 = dump[4]['city']
    temp_1 = dump[0]['temp']
    temp_2 = dump[1]['temp']
    temp_3 = dump[2]['temp']
    temp_4 = dump[3]['temp']
    temp_5 = dump[4]['temp']
    f_l_1 = dump[0]['feels_like']
    f_l_2 = dump[1]['feels_like']
    f_l_3 = dump[2]['feels_like']
    f_l_4 = dump[3]['feels_like']
    f_l_5 = dump[4]['feels_like']
    con_1 = dump[0]['condition']
    con_2 = dump[1]['condition']
    con_3 = dump[2]['condition']
    con_4 = dump[3]['condition']
    con_5 = dump[4]['condition']

    db = get_db()
    db.execute(
        'INSERT INTO weather (cit_1, cit_2, cit_3, cit_4, cit_5, temp_1, temp_2, temp_3, temp_4, temp_5, f_l_1, f_l_2, f_l_3, f_l_4, f_l_5, con_1, con_2, con_3, con_4, con_5, author_id)'
        ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (cit_1, cit_2, cit_3, cit_4, cit_5, temp_1, temp_2, temp_3, temp_4, temp_5, f_l_1, f_l_2, f_l_3, f_l_4, f_l_5,
         con_1, con_2, con_3, con_4, con_5, g.user['id'])
    )
    db.commit()

    post = all_posts()[0]

    csv = csv_maker(post)

    # return redirect('/test_down')
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename=ya_weather_data.csv"})
