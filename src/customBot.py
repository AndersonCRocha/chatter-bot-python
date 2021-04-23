from src.constants import *
from chatterbot import ChatBot
from difflib import SequenceMatcher

class CustomBot:
  def __init__(self, name, debug=False):
    self.bot = ChatBot(
      name,
      read_only=True,
      statement_comparison_function=self.__compareMessages,
      response_selection_method=self.__selectAnswer,
      logic_adapters=[
        {
          "import_path":"chatterbot.logic.BestMatch",
        }
      ]
    )
    self.isDebug = debug
  
  def __compareMessages(self, question, answer):
    if question.text and answer.text:
      questionText = question.text
      answerText = answer.text

      similarity = SequenceMatcher(
        None,
        questionText,
        answerText
      )
      
      similarity = round(similarity.ratio(), 2)
      if self.isDebug:
        print(f'Question: {questionText}')
        print(f'Possible answer: {answerText}')
        print(f'Similarity: {similarity}')
        
      if similarity >= ACCEPTANCE:
        return similarity
  
    return 0.0
  
  def __selectAnswer(self, message, answers, storage=None):
    if self.isDebug:
      print(f'Selected answer: {answers[0]}')
    
    return answers.pop(0)

  def getChatterBot(self):
    return self.bot
    
  def getAnswer(self, question):
    answer = self.bot.get_response(question)
    
    if answer.confidence > MINIMAL_CONFIDENCE:
      return answer.text
    
    return DEFAULT_UNKNOWN_RESPONSE
