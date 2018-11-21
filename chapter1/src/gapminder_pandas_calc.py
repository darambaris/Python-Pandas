import pandas as pd 
import matplotlib.pyplot as plot

def groupMean(df):
	#what is the average life expectancy for each year? 
	print(df.groupby('year')['lifeExp'].mean().head(n=5))

	#type DataFrameGroupBy
	print(type(df.groupby('year')))

	#type SeriesGroupBy
	print(type(df.groupby('year')['lifeExp']))

	#what is the average life expectancy and avg the income per capita, 
	#for each year and continent?
	mult_group_var = df.groupby(['year','continent'])\
					 [['lifeExp','gdpPercap']]\
					 .mean()

	#year and continent in other structure 
	print(mult_group_var.head(n=20))

	#the same index (structure)
	print(mult_group_var.reset_index().head(n=20))

def calcFreq(df):
	#count num of countries for each continent
	print(df.groupby('continent')['country'].nunique()) 

	#count number of times that each country appears 
	print(df.groupby('continent')['country'].value_counts())

if __name__ == '__main__':
	df = pd.read_csv('../data/gapminder.tsv', sep='\t')
	groupMean(df)	

	print('\n\n Pandas methods to calculate frequency \n' )
	calcFreq(df)

