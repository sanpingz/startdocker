from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host="db", port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	return 'Hello buddy! I have been seen {0} times'.format(redis.get('hits'))


if __name__ == '__main__':
	app.run()
