normD=1
fireD=1
fightD=1
watD=1
flyD=1
grassD=1
poiD=1
electricD=1
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

type1= input("What pokemon type do you want to know about?: ").lower()
type2= input("What is the secondary type? (If none, say none, or press enter to skip): ").lower()

def norm(vals):
  print("normal")
  vals["fightD"] = vals["fightD"]*2
  vals["ghostD"]=vals["ghostD"]*0
  return vals
def fire(vals):
  print("fire")
  vals["bugD"] = vals["bugD"] * .5
  vals["fireD"] = vals["fireD"]* .5
  vals["grassD"] = vals["grassD"]* .5
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
  vals["darkD"] = vals["darkD"]* 2
  return vals
def wat(vals):
  print("wat")
  vals["electricD"] = vals["electricD"]* 2
  vals["grass"] = vals["grassD"]* 2
  vals["fireD"] = vals["fireD"]* .5
  vals["iceD"] = vals["iceD"]* .5
  vals["steelD"] = vals["steelD"]* .5
  vals["watD"] = vals["watD"]* .5
  return vals
def fly(vals):
  print("flying")
  vals["bugD"] = vals["bugD"]* .5
  vals["fightD"] = vals["fightD"]* .5
  vals["grassD"] = vals["grassD"]* .5
  vals["electricD"] = vals["electricD"]* 2
  vals["iceD"] = vals["iceD"]* 2
  vals["rockD"] = vals["rockD"]* 2
  vals["groundD"] = vals["groundD"]* 0
  return vals
def grass(vals):
  print("grass")
  vals["electricD"] = vals["electricD"]* .5
  vals["grassD"] = vals["grassD"]* .5
  vals["groundD"] = vals["groundD"]* .5
  vals["watD"] = vals["watD"]* .5
  vals["bugD"] = vals["bugD"]* 2
  vals["flyD"] = vals["flyD"]* 2
  vals["fireD"] = vals["fireD"]* 2
  vals["iceD"] = vals["iceD"]* 2
  vals["poiD"] = vals["poiD"]* 2
  return vals
def poi(vals):
  print("poison")
  vals["groundD"] = vals["groundD"]* 2
  vals["psyD"] = vals["psyD"]* 2
  vals["fightD"] = vals["fightD"]* .5
  vals["poiD"] = vals["poiD"]* .5
  vals["bugD"] = vals["bugD"]* .5
  vals["grassD"] = vals["grassD"]* .5
  return vals
def electric(vals):
  print("electric")
  vals["groundD"] = vals["groundD"]* 2
  vals["electricD"] = vals["electricD"]* .5
  vals["flyD"] = vals["flyD"]* .5
  vals["steelD"] = vals["steelD"]* .5
  return vals
def ground(vals):
  print("ground")
  vals["grassD"] = vals["grassD"]* 2
  vals["iceD"] = vals["iceD"]* 2
  vals["watD"] = vals["watD"]* 2
  vals["poiD"] = vals["poiD"]* .5
  vals["rockD"] = vals["rockD"]* .5
  vals["electricD"] = vals["electricD"]* 0
  return vals
def psy(vals):
  print("psychic")
  vals["bugD"] = vals["bugD"]* 2
  vals["darkD"] = vals["darkD"]* 2
  vals["ghostD"] = vals["ghostD"]* 2
  vals["fightD"] = vals["fightD"]* .5
  vals["psyD"] = vals["psyD"]* .5
  return vals
def rock(vals):
  print("rock")
  vals["fightD"] = vals["fightD"]* 2
  vals["grassD"] = vals["grassD"]* 2
  vals["groundD"] = vals["groundD"]* 2
  vals["steelD"] = vals["steelD"]* 2
  vals["watD"] = vals["watD"]* 2
  vals["fireD"] = vals["fireD"]* .5
  vals["flyD"] = vals["flyD"]* .5
  vals["normD"] = vals["normD"]* .5
  vals["poiD"] = vals["poiD"]* .5
  return vals
def ice(vals):
  print("ice")
  vals["fireD"] = vals["fireD"]* 2
  vals["fightD"] = vals["fightD"]* 2
  vals["rockD"] = vals["rockD"]* 2
  vals["iceD"] = vals["iceD"]* .5
  return vals
def bug(vals):
  print("bug")
  vals["fireD"] = vals["fireD"]* 2
  vals["flyD"] = vals["flyD"]* 2
  vals["rockD"] = vals["rockD"]* 2
  vals["grassD"] = vals["grassD"]* .5
  vals["groundD"] = vals["groundD"]* .5
  vals["fightD"] = vals["fightD"]* .5
  return vals
def dra(vals):
  print("dragon")
  vals["draD"] = vals["draD"]* 2
  vals["fairyD"] = vals["fairyD"]* 2
  vals["iceD"] = vals["iceD"]* 2
  vals["electricD"] = vals["electricD"]* .5
  vals["fireD"] = vals["fireD"]* .5
  vals["grassD"] = vals["grassD"]* .5
  vals["watD"] = vals["watD"]* .5
  return vals
def ghost(vals):
  print("ghost")
  vals["darkD"] = vals["darkD"]* 2
  vals["ghostD"] = vals["ghostD"]* 2
  vals["poiD"] = vals["poiD"]* .5
  vals["bugD"] = vals["bugD"]* .5
  vals["fightD"] = vals["fightD"]* 0
  vals["normD"] = vals["normD"]* 0
  return vals
def dark(vals):
  print("dark")
  vals["bugD"] = vals["bugD"]* 2
  vals["fightD"] = vals["fightD"]* 2
  vals["darkD"] = vals["darkD"]* .5
  vals["ghostD"] = vals["ghostD"]* .5
  vals["psyD"] = vals["psyD"]* 0
  return vals
def steel(vals):
  print("steel")
  vals["fireD"] = vals["fireD"]* 2
  vals["fightD"] = vals["fightD"]* 2
  vals["groundD"] = vals["groundD"]* 2
  vals["poiD"] = vals["poiD"]* 0
  vals["bugD"] = vals["bugD"]* .5
  vals["draD"] = vals["draD"]* .5
  vals["fairyD"] = vals["fairyD"]* .5
  vals["flyD"] = vals["flyD"]* .5
  vals["grassD"] = vals["grassD"]* .5
  vals["iceD"] = vals["iceD"]* .5
  vals["normD"] = vals["normD"]* .5
  vals["psyD"] = vals["psyD"]* .5
  vals["rockD"] = vals["rockD"]* .5
  vals["steelD"] = vals["steelD"]* .5
  return vals
def fairy(vals):
  print("fairy")
  vals["steelD"] = vals["steelD"]* 2
  vals["poiD"] = vals["poiD"]* 2
  vals["bugD"] = vals["bugD"]* .5
  vals["darkD"] = vals["darkD"]* .5
  vals["fightD"] = vals["fightD"]* .5
  vals["draD"] = vals["draD"]* 0
  return vals
def none(vals):
  return vals
typedefense={
"normal": norm, "fire": fire, "fighting": fight, "fight": fight, "water": wat, "fly": fly, "flying": fly, "grass": grass, "poison": poi, "electric": electric, "ground": ground, "psychic": psy, "psy": psy, "rock": rock, "ice": ice, "bug": bug, "dragon": dra, "dra": dra, "ghost": ghost, "dark": dark, "steel": steel, "faerie": fairy, "fairy": fairy, "none": none, "": none
}
vals = {
  "bugD": 1,
  "fireD": 1,
  "grassD": 1,
  "iceD": 1,
  "steelD": 1,
  "rockD": 1,
  "fightD": 1,
  "groundD": 1,
  "watD": 1,
  "ghostD": 1,
  "flyD": 1,
  "psyD": 1,
  "darkD": 1,
  "electricD": 1,
  "poiD": 1,
  "darkD": 1,
  "draD": 1,
  "fairyD": 1,
  "normD": 1,
  
}
vals = typedefense[type1](vals)
vals = typedefense[type2](vals)
print("these are the multipliers on damage to this type")
print(vals)