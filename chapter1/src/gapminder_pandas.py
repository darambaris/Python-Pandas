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

def subSetsColumns(df):
	#column subset with loc
	# : means all the rows
	subset = df.loc[:,['year','pop']]
	print (subset.head())

	#column subset with iloc
	subset = df.iloc[:,[2,4,-1]]
	print(subset.head())

	#convert range to list 
	list_range = list(range(5))
	list_interval = list(range(3,6))

	#column subset (0,1,2,3,4) with iloc and range
	subset_range = df.iloc[:,list_range]
	subset_interval_range = df.iloc[:,list_interval]
	
	print ('Subset range(5):\n {}'.format(subset_range.head()))
	print ('Subset range(3,6):\n {}'.format(subset_interval_range.head()))

	#column subset with iloc and slicing values
	subset = df.iloc[:,:5] # = list(range(5))
	subset_interval = df.iloc[:,3:6]

	print ('Subset slicing values (:5):\n {}'.format(subset.head()))
	print ('Subset slicing values (3:6): \n {}'.format(subset_interval.head()))

	#slicing and range with step 
	# range(3,6,2) step 2
	# slicing [3:6:2] step 2


if __name__ == '__main__':
	df = readCSV()
	contentSpec(df)
	subSetsColumns(df)
