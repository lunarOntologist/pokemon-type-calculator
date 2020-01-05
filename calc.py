#!/usr/bin/env python3 
"""
Type advantage calculator
"""

def get_inputs():
  """Prompts the user for one or more types to check.

  Returns: 
    the names of the two types given
  """
  type1= input("What pokemon type do you want to know about?: ").lower()
  type2= input("What is the secondary type? (If none, say none, or press enter to skip): ").lower()
  return type1, type2

def norm(vals):
  print("normal")
  vals["fightD"] = vals["fightD"]*2
  vals["ghostD"]=vals["ghostD"]*0
  if "steel" in vals:
    vals["steel"] = vals["steel"] + "resists normal, "
  else:
    vals["steel"] = "resists normal, "
  if "rock" in vals:
    vals["rock"] = vals["rock"] + "resists normal, "
  else:
    vals["rock"] = "resists normal, "
  if "ghost" in vals:
    vals["ghost"] = vals["ghost"] + "immune normal, "
  else:
    vals["ghost"] = "immune to normal, "
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
  vals["fairyD"] = vals["fairyD"] * .5
  if "bug" in vals:
    vals["bug"] = vals["bug"] + "weak to fire, "
  else:
    vals["bug"] = "weak to fire, "
  if "grass" in vals:
    vals["grass"] = vals["grass"] + "weak to fire, "
  else:
    vals["grass"] = "weak to fire, "
  if "ice" in vals:
    vals["ice"] = vals["ice"] + "weak to fire, "
  else:
    vals["ice"] = "weak to fire, "
  if "steel" in vals:
    vals["steel"] = vals["steel"] + "weak to fire, "
  else:
    vals["steel"] = "weak to fire, "
  if "rock" in vals:
    vals["rock"] = vals["rock"] + "resists fire, "
  else:
    vals["rock"] = "resists fire, "
  if "dragon" in vals:
    vals["dragon"] = vals["dragon"] + "resists fire, "
  else:
    vals["dragon"] = "resists fire, "
  if "water" in vals:
    vals["water"] = vals["water"] + "resists fire, "
  else:
    vals["water"] = "resists fire, "
  if "fire" in vals:
    vals["fire"] = vals["fire"] + "resists fire, "
  else:
    vals["fire"] = "resists fire, "
  return vals
def fight(vals):
  print("fighting")
  vals["bugD"] = vals["bugD"]*.5
  vals["rockD"] = vals["rockD"]*.5
  vals["psyD"] = vals["psyD"]* 2 
  vals["flyD"] = vals["flyD"]* 2
  vals["darkD"] = vals["darkD"]* 2
  vals["fairyD"] = vals["fairyD"] * 2
  if "poison" in vals:
    vals["poison"] = vals["poison"] + "resists fighting, "
  else:
    vals["poison"] = "resists fighting, "
  if "flying" in vals:
    vals["flying"] = vals["flying"] + "resists fighting, "
  else:
    vals["flying"] = "resists fighting, "
  if "bug" in vals:
    vals["bug"] = vals["bug"] + "resists fighting, "
  else:
    vals["bug"] = "resists fighting, "
  if "psychic" in vals:
    vals["psychic"] = vals["psychic"] + "resists fighting, "
  else:
    vals["psychic"] = "resists fighting, "
  if "fairy" in vals:
    vals["fairy"] = vals["fairy"] + "weak to fighting, "
  else:
    vals["fairy"] = "resists fighting, "
  if "ghost" in vals:
    vals["ghost"] = vals["ghost"] + "immune to fighting, "
  else:
    vals["ghost"] = "immune to fighting, "
  if "normal" in vals:
    vals["normal"] = vals["normal"] + "weak to fighting, "
  else:
    vals["normal"] = "weak to fighting, "
  if "steel" in vals:
    vals["steel"] = vals["steel"] + "weak to fighting, "
  else:
    vals["steel"] = "weak to fighting, "
  if "rock" in vals:
    vals["rock"] = vals["rock"] + "weak to fighting, "
  else:
    vals["rock"] = "weak to fighting, "
  if "ice" in vals:
    vals["ice"] = vals["ice"] + "weak to fighting, "
  else:
    vals["ice"] = "weak to fighting, "
  if "dark" in vals:
    vals["dark"] = vals["dark"] + "weak to fighting, "
  else:
    vals["dark"] = "weak to fighting, "
  return vals
def wat(vals):
  print("wat")
  vals["electricD"] = vals["electricD"]* 2
  vals["grassD"] = vals["grassD"]* 2
  vals["fireD"] = vals["fireD"]* .5
  vals["iceD"] = vals["iceD"]* .5
  vals["steelD"] = vals["steelD"]* .5
  vals["watD"] = vals["watD"]* .5
  if "fire" in vals:
    vals["fire"] = vals["fire"] + "weak to water, "
  else:
    vals["fire"] = "weak to water, "
  if "ground" in vals:
    vals["ground"] = vals["ground"] + "weak to water, "
  else:
    vals["ground"] = "weak to water, "
  if "rock" in vals:
    vals["rock"] = vals["rock"] + "weak to water, "
  else:
    vals["rock"] = "weak to water, "
  '''if "grass" in vals:
    vals["grass"] = vals["grass"] + "resists water, "
  else:
    vals["grass"] = "resists water, "'''
  if "dragon" in vals:
    vals["dragon"] = vals["dragon"] + "resists water, "
  else:
    vals["dragon"] = "resists water, "
  if "water" in vals:
    vals["water"] = vals["water"] + "resists water, "
  else:
    vals["water"] = "resists water, "
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
  if "electric" in vals:
    vals["electric"] = vals["electric"] + "resists flying, "
  else:
    vals["electric"] = "resists flying, "
  if "steel" in vals:
    vals["steel"] = vals["steel"] + "resists flying, "
  else:
    vals["steel"] = "resists flying, "
  if "rock" in vals:
    vals["rock"] = vals["rock"] + "resists flying, "
  else:
    vals["rock"] = "resists flying, "
  if "bug" in vals:
    vals["bug"] = vals["bug"] + "weak to flying, "
  else:
    vals["bug"] = "weak to flying, "
  if "fighting" in vals:
    vals["fighting"] = vals["fighting"] + "weak to flying, "
  else:
    vals["fighting"] = "weak to flying, "
  if "grass" in vals:
    vals["grass"] = vals["grass"] + "weak to flying, "
  else:
    vals["grass"] = "weak to flying, "
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
  if "water" in vals:
    vals["water"] = vals["water"] + "weak to grass, "
  else:
    vals["water"] = "weak to grass, "
  if "ground" in vals:
    vals["ground"] = vals["ground"] + "weak to grass, "
  else:
    vals["ground"] = "weak to grass, "
  if "rock" in vals:
    vals["rock"] = vals["rock"] + "weak to grass, "
  else:
    vals["rock"] = "weak to grass, "
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
  if "ghost" in vals:
    vals["ghost"] = vals["ghost"] + "resists"
  else:
    vals["ghost"] = "resists, "
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

def get_starting_vals():
  """Get a default array of attack and defense scaling

  Returns:
    A dict of default defense values (no types applied)
  """
  return {
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
    "draD": 1,
    "fairyD": 1,
    "normD": 1,
  }

def compute_defense(type1, type2, vals):
  """Compute the defense scaling values for the given types

  Returns: 
    a mutated version of vals
  """
  vals = typedefense[type1](vals)
  vals = typedefense[type2](vals)
  return vals

def print_output(vals):
  """Prints the result of the check to the terminal
  """
  print("these are the multipliers on damage to this type")
  vals = [print(x) for x in vals.items() if x[1] != 1]

def main():
  """Main command line function
  """
  type1, type2 = get_inputs()
  vals = get_starting_vals()
  vals = compute_defense(type1, type2, vals)
  print_output(vals)

if __name__ == "__main__":
  main()