from chatterbot.trainers import ListTrainer
import json

class Trainer:
  def __init__(self, bot, settingsFilePaths=[]):
    self.trainer = ListTrainer(bot.getChatterBot())
    self.__loadSettingsFile(settingsFilePaths)
    
  def __loadSettingsFile(self, settingsFilePaths):
    self.settings = []
    
    for path in settingsFilePaths:
      with open(path, 'r', encoding='utf-8') as settingsFile:
        self.settings.extend(json.load(settingsFile))
        settingsFile.close()
    
  def train(self):
    for setting in self.settings:
      questions = setting['questions']
      answer = setting['answer']
      
      for question in questions:
        self.trainer.train([question, answer])
    
