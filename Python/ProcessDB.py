import pandas as pd
import numpy as np
import json
import re

path = "../DB/"
filename = "Medicinal Data CURR.csv"

data = pd.read_csv(path + filename)

data = data.drop(["Timestamp"], axis=1)

def extractCompounds(filepath="Compounds/compounds_list.json"):
	compSet = set()

	compounds = np.array(data['Compounds (salts)'])
	
	for block in compounds:
		for sent in block.split("\n"):
			comp = sent.split('-')[0].strip()
			if (comp):
				compSet.add(comp.lower())

	print(compSet)
	with open(path + filepath, 'w+') as f:
		json.dump(list(compSet), f)

if __name__ == '__main__':
	extractCompounds()
