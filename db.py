from flask_redis import FlaskRedis
redis_client = FlaskRedis(charset="utf-8", decode_responses=True)