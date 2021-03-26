#5E character creator

import random

#Pool of classes to be chosen based on highest stat number
StrPool = ['Monk', 'Paladin', 'Barbarian']
DexPool = ['Monk','Rogue', 'Ranger']
ConPool = ['Fighter', 'Barbarian', 'Scorcerer']
IntPool = ['Wizard', 'Druid', 'Rogue']
WisPool = ['Warlock', 'Ranger', 'Cleric']
ChaPool	= ['Cleric', 'Bard', 'Scorcerer']

STATS = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma']
statArray = [0,1,2,3,4,5]


def BaseStats(x,y):

	for i in range(0,int(x)):
		finalStats = [0,1,2,3,4,5]
		finalMod = [0,1,2,3,4,5]
		y=int(y);
		print('\nCharacter '+str(i+1)+'\n');
		print('Level: '+str(y));


		#Stat Roller
		for j in statArray:
			Stat1 = [random.randrange(1,7), random.randrange(1,7), random.randrange(1,7), random.randrange(1,7)];
			Stat1.sort();
			StatScore = Stat1[1] + Stat1[2] + Stat1[3];
			finalStats[j]= StatScore;
			if StatScore in range(2,4):
				mod = -4
			elif StatScore in range(4,6):
				mod = -3
			elif StatScore in range(6,8):
				mod = -2
			elif StatScore in range(8,10):
				mod = -1
			elif StatScore in range(10,12):
				mod = +0
			elif StatScore in range(12,14):
				mod = +1
			elif StatScore in range(14,16):
				mod = +2
			elif StatScore in range(16,18):
				mod = +3
			elif StatScore in range(18,20):
				mod = +4
			finalMod[j] = mod;
			print(STATS[j]+':', str(StatScore), str(mod));

		#Class Selector
		max = finalStats[0]
		classStat = STATS[0];
		for n in range(0,6):
			if finalStats[n] > max:
				max = finalStats[n]
				classStat = STATS[n]
		if classStat == STATS[0]:
			classString = StrPool[random.randrange(0,3)]
		elif classStat == STATS[1]:
			classString = DexPool[random.randrange(0,3)]
		elif classStat == STATS[2]:
			classString = ConPool[random.randrange(0,3)]
		elif classStat == STATS[3]:
			classString = IntPool[random.randrange(0,3)]
		elif classStat == STATS[4]:
			classString = WisPool[random.randrange(0,3)]
		elif classStat == STATS[5]:
			classString = ChaPool[random.randrange(0,3)]

		#HP calculator
		if classString == 'Scorcerer' or 'Wizard':
			hitDie = 6
		elif classString == 'Warlock' or 'Rogue' or 'Druid' or 'Monk' or 'Bard' or 'Cleric':
			hitDie = 8
		elif classString == 'Fighter' or 'Paladin' or 'Ranger':
			hitDie = 10
		elif classString == 'Barbarian':
			hitDie = 12
		totalHealth=0;
		for z in range(0,y):
			totalHealth = random.randrange(1,hitDie+1) + totalHealth + finalMod[2] 

		HitPoints = totalHealth + hitDie;

		print("\nClass: "+ classString)
		print('HP: '+str(HitPoints))

		print("\n*--------------------------------------*");	

BaseStats(input("Number of Characters: "),input("Level of Characters: "))


