#!/usr/bin/python

#	Joey Allen Python Weather Reader
#	Dr. Andrew Pounds CSC330
import urllib
import string
import operator

#will hold all values associated with a state
class State:
 def __init__(self, name):
   self.stationCount = 0
   self.name = name
   self.sumTemp = 0.0
   self.avgTemp = 0.0

#will keep track of each station's corresponding state
class Station:
 def __init__(self, stationID, stateName, temperature):
   self.stationID = stationID
   self.stateName = stateName
   self.temperature = temperature


# Define lists
stationid = []
state = []
# Define dictionaries
myStations = {}
myStates = {}

#attach and read online txt file
stationfile = urllib.urlopen("http://theochem.mercer.edu/csc330/data/station.txt")
data = stationfile.read()

#split each line
lines = data.split('\n')

count = 0
for line in lines:
  if count == 0:	#skip first line
   count = 1
   continue
  count = count+1
  fields = line.split('|')
  CURRENT_ID = fields[0]
  CURRENT_STATE = fields[7]
  #put into array of stationids
  stationid.append(CURRENT_ID)
  #if unique state name, put into array of state names,
  # initialize dictionary with statename as key and state object of same name as item
  if not any(x ==(CURRENT_STATE) for x in state):
    state.append(CURRENT_STATE)
    myStates[CURRENT_STATE]=State(CURRENT_STATE)
  #create stationobject connecting stationID and state name
  myStations[CURRENT_ID]=CURRENT_STATE

#big loop to process all daily data
counter = 0
iterationlength = line in lines

for line in lines:
  #skip first one
  if counter == 0:
    counter = 1
    continue

  #skip last one
  if counter == len(lines)-1:
     continue

  #increment
  counter = counter + 1

  #skip missing readings
  if line.split(',')[6] == 'M':
     continue

  #examine current station
  currstationid = line.split(',')[0]

  #examine current float value of reading
  currtemp = float(line.split(',')[6])

  #if this id is in myStations keys list, examine its corresponding state name
  if currstationid in myStations.keys():
     currstate = myStations[currstationid]

     #if that state name is in myStates.keys, examine that state object and increment sumTemp and stationCount
     if currstate in myStates.keys():
        myStates[currstate].sumTemp = myStates[currstate].sumTemp + currtemp
        myStates[currstate].stationCount = myStates[currstate].stationCount + 1

#remove states with no readings
for item in myStates:
    if myStates[item].stationCount > 0:
      myStates[item].avgTemp = myStates[item].sumTemp / myStates[item].stationCount

#print header for data
print "State:\t#of Stations\tAvg Temp"


#print a version of myStates sorted by avgTemp of each state
for item in (sorted(myStates.values(), key=operator.attrgetter('avgTemp'))):
  if item.stationCount > 0:
    print item.name + "\t" + str(item.stationCount) + "\t\t" + str(item.avgTemp)
