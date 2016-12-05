import numpy as np
import array as ar
import time
from HumanRandom import HumanRandom
#from PlotEnvironment import Plot
import matplotlib.pyplot as plt

nbrHuman = 10
fieldSize = 20
Agents = []
lifeTime = 100
HOME = 1
FOOD = 0
nestPosition = fieldSize/2  #general nest position

maxSugar = 100
carreiSize= 1
collectedSugar = 0
#===============================================================================
# GRID RESOURCES --> ANTS
#===============================================================================
gridInfo = np.zeros((fieldSize,fieldSize,3))
for i in range(fieldSize):
	for j in range(fieldSize):
		gridInfo[i][j] = [0,0,0] #[PheromeForaging, PheromoneRetHome, SugarAmount]
	#
#===========================================================================
# PLOT INFO 
#===========================================================================
plotInfo = np.zeros((fieldSize,fieldSize,3))
for i in range(fieldSize):
	for j in range(fieldSize):
		plotInfo[i][j] = [0,0,0] #[state, health, SugarAmount]
	#
	

for it in range(1000):
	#spawn new ant from nest
	xPos = np.random.random_integers(nestPosition-1,nestPosition+1)
	yPos = np.random.random_integers(nestPosition-1,nestPosition+1)
	Agents.append(HumanRandom(xPos, yPos, lifeTime))
	nbrHuman += 1
	#moves all agents once
	i = 0
	while i < nbrHuman:
		[pos,oldPos,health] = Agents[i].Move(gridInfo)
		plotInfo[oldPos[0]][oldPos[1]][1] = 0 #reset HP
		if gridInfo[pos[0]][pos[1]][2] > 0  and Agents[i].GetState() == FOOD : #to recognise sugar
			Agents[i].ChangeState(HOME)
			plotInfo[pos[0]][pos[1]][2] -= 1
			gridInfo[pos[0]][pos[1]][2] -= 1
		#
		if gridInfo[pos[0]][pos[1]][2] == -1 and Agents[i].GetState() == HOME : #to recognise nest
			Agents[i].ChangeState(FOOD)
			collectedSugar += 1
		#
		if health < 0: #ants drop sugar on death
			gridInfo[pos[0]][pos[1]][2] += sugar
			plotInfo[pos[0]][pos[1]][2] += sugar
			del Agents[i]
			nbrHuman -= 1
		#
	#
	#FIX plotinfo, add all agents to the plot
	#
	#plotInfo[pos[0]][pos[1]][0] = Agents[i].GetState() #state
	#plotInfo[pos[0]][pos[1]][1] = Agents[i].GetHealth() #state
	#
	
	#lowers pheromones and food
	#FIX add diffusion
	for i in range(fieldSize):
		for j in range(fieldSize):
			gridInfo[i][j][0] -= gridInfo[i][j][0]*0.1
			gridInfo[i][j][1] -= gridInfo[i][j][1]*1
			if (gridInfo[i][j][2] > 0):
				gridInfo[i][j][2] -= 1
			#
	#
	
	#===========================================================================
	#FIX Adding new Sugar?
	#===========================================================================
	#with diffusion like behaviour 
	
	#Plot.AllFields(Plot ,plotInfo , 5 , 5) 
	#The above line does not work, the same goes for the import at row 5
