import json
import matplotlib.pyplot as plt

engineData = {'state':'Stopped','throttlemode':'Internal','throttle':70,'enginespeed':{'NL':1400,'NI':8000,'NH':15000},'temperatures':{'T0':23,'T1':180,'T3':180,'T45':180},'pressures':{'P0':23,'P1':180,'P3':180},'thrust':1,'fuelflow':600}

print(json.dumps(engineData, sort_keys=True, indent=4, separators=(',',':')))

print(engineData['state'])
print(engineData['enginespeed'])
print(engineData['enginespeed']['NI'])

jsonData = json.dumps(engineData)

print(jsonData)

receivedData = json.loads(jsonData)

print(receivedData['state'])
print(receivedData['enginespeed'])
print(receivedData['temperatures']['T1'])

temp0 = [10,10,10]
print(temp0)
temp0.append(receivedData['temperatures']['T0'])
print(temp0)

plt.plot(temp0)
plt.show()
