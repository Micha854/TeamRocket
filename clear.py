import telebot

class Clear():
  def clear(self,token,chatID,singlechatID,cfg):
    bot = telebot.TeleBot(token)
    try:
      f = open(cfg.areaName+cfg.areaNumber+"/lists.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(chatID,message_id=messageID)
      except:
        print("Alte LISTE konnte nicht entfernt werden")
    try:
      f = open(cfg.areaName+cfg.areaNumber+"/output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("Alte BOSS Nachricht konnte nicht entfernt werden")
    try:
      f = open(cfg.areaName+cfg.areaNumber+"/boss-output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("Alte Lockmodul Nachricht konnte nicht entfernt werden")
    try:
      f = open(cfg.areaName+cfg.areaNumber+"/lockmodul-output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("Alte Rüpel Nachricht konnte nicht entfernt werden")
