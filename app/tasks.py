import celery
import pickle
from datetime import timedelta
from app import app
from phue import Bridge

#Queries the lights and returns the status for each room in the apartment
#Return: {"RoomName":True, "RoomName":False}, etc
def getRoomLightStatus(b):
	roomStatus = {}
	for group in b.groups:
		roomStatus[group.name] = any([light.on for light in group.lights])
	return roomStatus

def whosHome():
	pass

@celery.task(name='toggleLightsTask')
def checkApartment():
	try:
		apartmentHistory = pickle.load(open( "apartmentHistory.pkl", "rb" ))
	except:
		apartmentHistory = {}
		apartmentHistory = {"roomHistory":{}}


	b = Bridge('192.168.1.103')
	b.connect()
	roomStatus = getRoomLightStatus(b)
	print roomStatus
	roomHistory = apartmentHistory["roomHistory"]
	newRoomHistory = {}
	#Update the room stats for the history
	for room in roomStatus:
		if room not in roomHistory.keys():
			roomHistory[room] = []
		if len(roomHistory[room]) < 33600:
			newRoomHist = roomHistory[room] + [roomStatus[room]]
		else:
			newRoomHist = roomHistory[room][1:] + [roomStatus[room]]
		print room, len([val for val in newRoomHist if val==True])*1.0/len(newRoomHist)
		newRoomHistory[room] = newRoomHist
	apartmentHistory["roomHistory"] = newRoomHistory
	#print newRoomHistory

	pickle.dump(apartmentHistory,open( "apartmentHistory.pkl", "wb" ))
