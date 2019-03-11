import pandas as pd
import sys
import glob
# from settings import *


def getReplace(org, key, before, after):
	org[key] = org[key].str.replace(before, after)
	return org

def replacePrice(org, key, down, up, a, b):
	org.loc[(org[key]<up)&(org[key]>=down), key] = org.loc[(org[key]<up)&(org[key]>=down),key] * a + b
	return org

def readReplace(init, path_replce, key, orgData, replaced_csv_path):


	with open(path_replce, 'r', encoding='Shift-JIS') as f:
		for line in f:
			## remove 'Newline character'
			line = line.strip().split(',')
			print(len(line), line)
			if(key != "price"):
				if( len(line) == 2):
					## Before conversion and After conversion
					before = line[0]
					#after = '{0}({1})'.format(line[0], line[1])
					after = line[1]

					newData = getReplace(orgData, key, before, after)
					## Overwrite mode
					newData.to_csv(replaced_csv_path, encoding='Shift-JIS', index=False)
			else:
				if( len(line) == 4):
					## down, up, a, b
					newData = replacePrice(orgData, key, int(line[0]), int(line[1]), int(line[2]), int(line[3]))
					## Overwrite mode
					newData.to_csv(replaced_csv_path, encoding='Shift-JIS', index=False)

def runHeader(init, pathReplceList, headers):
	# test
	# replaced_csv_path = '../{0}_csv/replaced_{1}'.format(init['folder'], init['csv_name'])
	# org_csv_path = '../{0}_csv/{1}'.format(init['folder'], init['csv_name'])

	replaced_csv_path = '{0}_csv/replaced_{1}'.format(init['folder'], init['csv_name'])
	org_csv_path = '{0}_csv/{1}'.format(init['folder'], init['csv_name'])
	orgData = pd.read_csv(org_csv_path, encoding='Shift-JIS')

	for head, path_replce in zip(headers, pathReplceList):
		readReplace(init, path_replce, head, orgData, replaced_csv_path)

def runCsvList(init, pathReplceList, headers):
	if( len(pathReplceList) == len(headers) ):
			runHeader(init, pathReplceList, headers)
	else:
		sys.exit()


if __name__ == '__main__':
	init = setConst()
	headers = ['name', 'Material']
	pathReplceList = ['../replace_csv/name.csv', '../replace_csv/Material.csv']
	runCsvList(init, pathReplceList, headers)
