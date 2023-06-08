from flask import Blueprint, render_template
from .models import Events
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    events = Events.query.all()
    return render_template('index.html', events=events)
