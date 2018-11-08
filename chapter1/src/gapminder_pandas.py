import pandas as pd

#read .csv and print its structure
def readCSV():

	#read file and define separator
	df = pd.read_csv('../data/gapminder.tsv', sep='\t')

	#print first 5 rows
	print(df.head())

	#print last 5 rows
	print(df.tail())

	#print type dataFrame
	print(type(df))

	#print number of rows and columns
	print(df.shape)

	#columns name
	print(df.columns)

	#use dtypes to get dtype columns
	print(df.dtypes)

	#get more informations about data
	print(df.info())

	return df

def contentSpec(df):
	#subset with specific columns
	subset = df[['country', 'continent', 'year']]
	print (subset.head())
	print (subset.tail())

	#subset with specific rows
	print(subset.loc[0])
	print(subset.loc[subset.shape[0]-1])
	print(subset.loc[[0, 99, 999]]) #DataFrame
	#other syntax
	print (subset.tail(n=1))

	#types diff
	print (type(subset.tail(n=1))) #DataFrame
	print (type(subset.head(n=1))) #DataFrame
	print (type(subset.loc[[0,99,999]])) #DataFrame
	print (type(subset.loc[subset.shape[0]-1])) #Series
	

if __name__ == '__main__':
	df = readCSV()
	contentSpec(df)
