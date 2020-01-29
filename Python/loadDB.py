import pandas as pd
import json

path = '../DB/'

def loadJSON(filepath):
	with open(path + filepath, 'r') as f:
		return JSON.load(f)

def loadCompounds(filepath = "Compounds/standard_compounds.json"):
	return loadJSON(filepath)
