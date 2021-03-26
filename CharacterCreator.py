import tkinter as tk
import random

window = tk.Tk()
window.title('D&D 5E Character Roller')



#Character Stats
class Character:

	def __init__(self,Str,Dex,Con,Int,Wis,Cha):
		self.Str = Str
		self.Dex = Dex
		self.Con = Con
		self.Int = Int
		self.Wis = Wis
		self.Cha = Cha


def characterRoll():
	abilityTag = [1,1,1,1,1,1]
	finalMod = [0,1,2,3,4,5]

	for j in range(0,6):
		roll = [random.randrange(1,7), random.randrange(1,7), random.randrange(1,7), random.randrange(1,7)];
		roll.sort();
		abilityTag[j] = roll[1] + roll[2] + roll[3];
	C1=Character(abilityTag[0], abilityTag[1], abilityTag[2], abilityTag[3], abilityTag[4], abilityTag[5])
	
	stat1['text'] = C1.Str
	stat2['text'] = C1.Dex
	stat3['text'] = C1.Con
	stat4['text'] = C1.Int
	stat5['text'] = C1.Wis
	stat6['text'] = C1.Cha

def increaseStr():
	value = int(stat1['text'])
	stat1['text'] =  f"{value + 1}"
def decreaseStr():
	value = int(stat1['text'])
	stat1['text'] =  f"{value - 1}"

def increaseDex():
	value = int(stat2['text'])
	stat2['text'] =  f"{value + 1}"
def decreaseDex():
	value = int(stat2['text'])
	stat2['text'] =  f"{value - 1}"

def increaseCon():
	value = int(stat3['text'])
	stat3['text'] =  f"{value + 1}"
def decreaseCon():
	value = int(stat3['text'])
	stat3['text'] =  f"{value - 1}"

def increaseInt():
	value = int(stat4['text'])
	stat4['text'] =  f"{value + 1}"
def decreaseInt():
	value = int(stat4['text'])
	stat4['text'] =  f"{value - 1}"

def increaseWis():
	value = int(stat5['text'])
	stat5['text'] =  f"{value + 1}"
def decreaseWis():
	value = int(stat5['text'])
	stat5['text'] =  f"{value - 1}"

def increaseCha():
	value = int(stat6['text'])
	stat6['text'] =  f"{value + 1}"
def decreaseCha():
	value = int(stat6['text'])
	stat6['text'] =  f"{value - 1}"

def modCalculator():
	finalMod = [0,1,2,3,4,5]
	abilityTag = [int(stat1['text']),int(stat2['text']),int(stat3['text']),int(stat4['text']),int(stat5['text']),int(stat6['text'])]
	for j in range(0,6):
		if abilityTag[j] in range(2,4):
			finalMod[j] = '-4'
		elif abilityTag[j] in range(4,6):
			finalMod[j] = '-3'
		elif abilityTag[j] in range(6,8):
			finalMod[j] = '-2'
		elif abilityTag[j] in range(8,10):
			finalMod[j] = '-1'
		elif abilityTag[j] in range(10,12):
			finalMod[j] = '+0'
		elif abilityTag[j] in range(12,14):
			finalMod[j] = '+1'
		elif abilityTag[j] in range(14,16):
			finalMod[j] = '+2'
		elif abilityTag[j] in range(16,18):
			finalMod[j] = '+3'
		elif abilityTag[j] in range(18,20):
			finalMod[j] = '+4'
		else:
			finalMod[j] = '+5'
	mod1['text'] = finalMod[0]
	mod2['text'] = finalMod[1]
	mod3['text'] = finalMod[2]
	mod4['text'] = finalMod[3]
	mod5['text'] = finalMod[4]
	mod6['text'] = finalMod[5]



window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=5, weight=1)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=10, weight=1)


stat1 = tk.Label(text='0',bg='#F36C4F')
stat2 = tk.Label(text='0',bg='#F36C4F')
stat3 = tk.Label(text='0',bg='#F36C4F')
stat4 = tk.Label(text='0',bg='#F36C4F')
stat5 = tk.Label(text='0',bg='#F36C4F')
stat6 = tk.Label(text='0',bg='#F36C4F')

abil1 = tk.Label(text='Str:',bg='grey')
abil2 = tk.Label(text='Dex:',bg='grey')
abil3 = tk.Label(text='Con:',bg='grey')
abil4 = tk.Label(text='Int:',bg='grey')
abil5 = tk.Label(text='Wis:',bg='grey')
abil6 = tk.Label(text='Cha:',bg='grey')

mod1 = tk.Label(text='0',bg='#F36C4F')
mod2 = tk.Label(text='0',bg='#F36C4F')
mod3 = tk.Label(text='0',bg='#F36C4F')
mod4 = tk.Label(text='0',bg='#F36C4F')
mod5 = tk.Label(text='0',bg='#F36C4F')
mod6 = tk.Label(text='0',bg='#F36C4F')

btn_roll = tk.Button(text="Roll", command=characterRoll)
btn_mod = tk.Button(text="mod", command=modCalculator)
btn_incStr = tk.Button(text="+", command=increaseStr)
btn_decStr = tk.Button(text="-", command=decreaseStr)
btn_incDex = tk.Button(text="+", command=increaseDex)
btn_decDex = tk.Button(text="-", command=decreaseDex)
btn_incCon = tk.Button(text="+", command=increaseCon)
btn_decCon = tk.Button(text="-", command=decreaseCon)
btn_incInt = tk.Button(text="+", command=increaseInt)
btn_decInt = tk.Button(text="-", command=decreaseInt)
btn_incWis = tk.Button(text="+", command=increaseWis)
btn_decWis = tk.Button(text="-", command=decreaseWis)
btn_incCha = tk.Button(text="+", command=increaseCha)
btn_decCha = tk.Button(text="-", command=decreaseCha)

abil1.grid(row=1,column=1, sticky="ew")
abil2.grid(row=2,column=1, sticky="ew")
abil3.grid(row=3,column=1, sticky="ew")
abil4.grid(row=4,column=1, sticky="ew")
abil5.grid(row=5,column=1, sticky="ew")
abil6.grid(row=6,column=1, sticky="ew")

stat1.grid(row=1,column=4, sticky="ew")
stat2.grid(row=2,column=4, sticky="ew")
stat3.grid(row=3,column=4, sticky="ew")
stat4.grid(row=4,column=4, sticky="ew")
stat5.grid(row=5,column=4, sticky="ew")
stat6.grid(row=6,column=4, sticky="ew")

mod1.grid(row=1,column=5, sticky="ew")
mod2.grid(row=2,column=5, sticky="ew")
mod3.grid(row=3,column=5, sticky="ew")
mod4.grid(row=4,column=5, sticky="ew")
mod5.grid(row=5,column=5, sticky="ew")
mod6.grid(row=6,column=5, sticky="ew")


btn_roll.grid(row=0, column=4, sticky="ew")
btn_mod.grid(row=0, column=5, sticky="ew")
btn_incStr.grid(row=1, column=2, sticky="ew")
btn_decStr.grid(row=1, column=0, sticky="ew")
btn_incDex.grid(row=2, column=2, sticky="ew")
btn_decDex.grid(row=2, column=0, sticky="ew")
btn_incCon.grid(row=3, column=2, sticky="ew")
btn_decCon.grid(row=3, column=0, sticky="ew")
btn_incInt.grid(row=4, column=2, sticky="ew")
btn_decInt.grid(row=4, column=0, sticky="ew")
btn_incWis.grid(row=5, column=2, sticky="ew")
btn_decWis.grid(row=5, column=0, sticky="ew")
btn_incCha.grid(row=6, column=2, sticky="ew")
btn_decCha.grid(row=6, column=0, sticky="ew")


window.mainloop()