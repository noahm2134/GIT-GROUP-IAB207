from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    events = Events.query.all()
    return render_template('index.html', events=events)

@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        events = Events.query.filter(Events.name.like(dest)).all()
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))
