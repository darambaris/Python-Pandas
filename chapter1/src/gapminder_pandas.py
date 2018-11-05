import pandas as pd


def readCSV():

	#read file and define separator
	df = pd.read_csv('../data/gapminder.tsv', sep='\t')

	#print first 5 rows
	print(df.head())

	#print type dataFrame
	print(type(df))

	#print number of rows and columns
	print(df.shape)

if __name__ == '__main__':
	readCSV()