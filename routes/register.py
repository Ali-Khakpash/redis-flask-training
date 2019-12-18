from flask import Blueprint, render_template, abort
from flask import request
from db import redis_client
import ray
import time
ray.init()
from jinja2 import TemplateNotFound

user_register = Blueprint("user_register", __name__, template_folder='../')


@user_register.route('/register', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        name = str(request.values.get('name'))
        age = str(request.values.get('age'))

        now = str(time.time())
        user_id = str(redis_client.incrby('Users:'))
        redis_client.hset('Users:' + user_id,'name',name)
        redis_client.hset('Users:' + user_id, 'age', age)
        redis_client.sadd('time:Users:' + user_id, now)
        return render_template('templates/index.html')
    else:
        return render_template('templates/index.html')
