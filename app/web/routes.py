from flask import Blueprint, render_template, jsonify
from app.models import Parameter
from app import db
import datetime
import plotly.graph_objs as go
import plotly.io as pio

bp = Blueprint(
    'web',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/current_value')
def current_value():
    latest_parameter = Parameter.query.order_by(Parameter.timestamp.desc()).first()
    if latest_parameter:
        return jsonify(value=latest_parameter.value)
    return jsonify(value=None)


@bp.route('/last_hour_data')
def last_hour_data():
    one_hour_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    data = Parameter.query.filter(Parameter.timestamp >= one_hour_ago).all()
    timestamps = [param.timestamp for param in data]
    values = [param.value for param in data]

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=timestamps, y=values, mode='lines', name='Parameter Value'))
    graph_html = pio.to_html(figure, full_html=False)
    return graph_html
