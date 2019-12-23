
global bugD 
global fireD
global graD
global iceD
global steelD
global fightD
global ghostD

normD=1
fireD=1
fightD=1
watD=1
flyD=1
graD=1
poiD=1
eleD=1
groundD=1
psyD=1
rockD=1
iceD=1
bugD=1
draD=1
ghostD=1
darkD=1
steelD=1
fairyD=1

type1= input("what pokemon type do you want to know about?").lower()
type2= input("what is the secondary type? If none, say none").lower()

def norm(vals):
  print("normal")
  vals["fightD"] = vals["fightD"]*2
  vals["ghostD"]=vals["ghostD"]*0
  return vals

def fire(vals):
  print("fire")
  vals["bugD"] = vals["bugD"] * .5
  vals["fireD"] = vals["fireD"]* .5
  vals["graD"] = vals["graD"]* .5
  vals["iceD"] = vals["iceD"]* .5
  vals["steelD"] = vals["steelD"]* .5
  vals["watD"] = vals["watD"]* 2
  vals["groundD"] = vals["groundD"]* 2
  vals["rockD"] = vals["rockD"]* 2
  return vals
def fight(vals):
  print("fighting")
  vals["bugD"] = vals["bugD"]*.5
  vals["rockD"] = vals["rockD"]*.5
  vals["psyD"] = vals["psyD"]* 2 
  vals["flyD"] = vals["flyD"]* 2
  return vals
def wat():
  print("water")
def fly():
  print("flying")
def gra():
  print("grass")
def poi():
  print("poison")
def ele():
  print("electric")
def ground():
  print("ground")
def psy():
  print("psychic")
def rock():
  print("rock")
def ice():
  print("ice")
def bug():
  print("bug")
def dra():
  print("dragon")
def ghost():
  print("ghost")
def dark():
  print("dark")
def steel():
  print("steel")
def fairy():
  print("fairy")
def none(vals):
  return vals
typedefense={
"normal": norm,
"fire": fire,
"fighting": fight,
"fight": fight,
"water": wat,
"fly": fly,
"flying": fly,
"grass": gra,
"poison": poi,
"electric": ele,
"ground": ground,
"psychic": psy,
"psy": psy,
"rock": rock,
"ice": ice,
"bug": bug,
"dragon": dra,
"dra": dra,
"ghost": ghost,
"dark": dark,
"steel": steel,
"faerie": fairy,
"fairy": fairy,
"none": none,
"": none
}
vals = {
  "bugD": 1,
  "fireD": 1,
  "graD": 1,
  "iceD": 1,
  "steelD": 1,
  "rockD": 1,
  "fightD": 1,
  "groundD": 1,
  "watD": 1,
  "ghostD": 1,
  "flyD": 1,
  "psyD": 1,
}
vals = typedefense[type1](vals)
vals = typedefense[type2](vals)
print(vals)
print(fireD)