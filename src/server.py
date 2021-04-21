from src.constants import BOT_NAME, SETTINGS_FILE_PATHS, SERVER_VERSION
from src.trainer import Trainer
from src.customBot import CustomBot
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('./config.py')

bot = CustomBot(BOT_NAME, debug=True)
Trainer(bot, settingsFilePaths=SETTINGS_FILE_PATHS).train()

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/version")
def getVersion():
    return SERVER_VERSION

@app.route("/answer/<question>")
def getAnswer(question):
  return bot.getAnswer(question)

def run():
  app.run()