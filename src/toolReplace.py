import pandas as pd
import sys
import glob
from src.settings import *


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
	#test
	replaced_csv_path = '../{0}_csv/replaced_{1}'.format(init['folder'], init['csv_name'])
	org_csv_path = '../{0}_csv/{1}'.format(init['folder'], init['csv_name'])

	# replaced_csv_path = '{0}_csv/replaced_{1}'.format(init['folder'], init['csv_name'])
	# org_csv_path = '{0}_csv/{1}'.format(init['folder'], init['csv_name'])
	# orgData = pd.read_csv(org_csv_path, encoding='Shift-JIS')

	for head, path_replce in zip(headers, pathReplceList):
		readReplace(init, path_replce, head, orgData, replaced_csv_path)

def replaceName(org_data, df_replace):
	copy_data = org_data.copy()
	for i, d in enumerate(org_data['name']):
		add_str = ''
		for a, b in zip(df_replace['name_after'], df_replace['name_before']):
			if(str(b) in str(d)):
				add_str += str(a) + ' '
				add_str = add_str.rstrip()
		copy_data['name'][i] = '[{}]'.format(add_str) + str(org_data['name'][i])

	return copy_data

def replaceMaterial(org_data, df_replace):
	for i, d in enumerate(org_data['Material']):
		add_str = ''
		for a, b in zip(df_replace['Material_after'], df_replace['Material_before']):
			if(str(b) in str(d)):
				org_data['Material'] = a
				break

	return org_data

def runCsvList(init, pathReplceList, headers):
	#df_replace = pd.read_csv('replace_list.csv', encoding='Shift-JIS')
	df_replace = pd.read_csv('replace_csv/replace_list.csv', encoding='Shift-JIS')

	replaced_csv_path = '{0}_csv/replaced_{1}'.format(init['folder'], init['csv_name'])
	org_csv_path = '{0}_csv/{1}'.format(init['folder'], init['csv_name'])
	org_data = pd.read_csv(org_csv_path, encoding='Shift-JIS', dtype = 'object')

	for i in headers:
		if(i == 'name'):
			org_data = replaceName(org_data, df_replace)
		if(i == 'Material'):
			org_data = replaceMaterial(org_data, df_replace)

	org_data.to_csv(replaced_csv_path, encoding='Shift-JIS', index=False)

if __name__ == '__main__':
	init = setConst()
	headers = ['name', 'Material']
	pathReplceList = 0
	runCsvList(init, pathReplceList, headers)
