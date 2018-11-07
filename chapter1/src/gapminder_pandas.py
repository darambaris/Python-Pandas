import pandas as pd

#read .csv and print its structure
def readCSV():

	#read file and define separator
	df = pd.read_csv('../data/gapminder.tsv', sep='\t')

	#print first 5 rows
	print(df.head())

	#print type dataFrame
	print(type(df))

	#print number of rows and columns
	print(df.shape)

	#columns name
	print(df.columns)

	#uses dtypes to get dtype columns
	print(df.dtypes)

	#gets more informations about data
	print(df.info())

	return df

if __name__ == '__main__':
	df = readCSV()