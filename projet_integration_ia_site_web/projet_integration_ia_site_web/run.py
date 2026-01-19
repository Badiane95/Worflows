from flask import Flask

from app_assistant_ia.views import app as app_bot
from app_analyse_sentiment.views import app as app_sentiment

if __name__ == '__main__':
	app_bot.run(debug=True)
	# app_sentiment.run(debug=True)
