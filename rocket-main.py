import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear

cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("rocket-config.ini")

Sql = sql.Sql()
result = Sql.myGeo(cfg)

fence_file = open(cfg.areaName+cfg.areaNumber+"geofence.txt", "w")
write_cords = fence_file.write(result[cfg.areaName])
fence_file.close()

fence_file = open(cfg.areaName+cfg.areaNumber+"geofence.txt", "r")
geofence = fence_file.read()
fence_file.close()

clear = clear.Clear()
clear.clear(cfg.token,cfg.singlechatId,cfg)
send = sendMessage.sendMessage()
send.setConfig(cfg.token,cfg.singlechatId,cfg.chatId,cfg.areaName,cfg.areaNumber)

sys.stdout.write("\x1b]2;%s\x07" % cfg.areaName+cfg.areaNumber)

newMessageAfter = float(cfg.newMessageAfter) * 60
sleep_time = int(cfg.sleep_time)
timer = 0

while 1 == 1:
  if timer > newMessageAfter:
    timer = sleep_time
  else:
    timer +=sleep_time
    
  Sql.lockmodulSQL(cfg,"SELECT name,latitude,longitude,active_fort_modifier,lure_expiration FROM pokestop where timestampdiff(SECOND,lure_expiration,NOW())<3600 AND ST_CONTAINS(st_geomfromtext('POLYGON(( " + geofence + " ))') , point(pokestop.latitude,pokestop.longitude)) ORDER BY lure_expiration,name")
  Sql.rocketSQL(cfg,"SELECT name,latitude,longitude,incident_grunt_type,incident_expiration FROM pokestop where timestampdiff(SECOND,incident_expiration,NOW())<3600 AND ST_CONTAINS(st_geomfromtext('POLYGON(( " + geofence + " ))') , point(pokestop.latitude,pokestop.longitude)) ORDER BY incident_expiration,name")
  send.clearOutputList(Sql.name,Sql.Lname)
  create = createMessage.createMessage()
  create.create(send,Sql,cfg,timer,newMessageAfter)
  time.sleep(sleep_time)
  #send.send(create.message)