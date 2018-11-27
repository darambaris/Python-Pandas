import pandas as pd
from collections import OrderedDict

def createSeries():
	#All the elements of the Series must have the same type
	s = pd.Series(['banana',3])
	print(s) #type is a object

	#index name 
	s_name=pd.Series(['Wes McKinney', 'Creator of Pandas'],
					  index=['Person','Who'])
	print(s_name)

def createDataFrame():
	#"Dataframe is like a dict of Series"
	scientists = pd.DataFrame({
			'Name': ['Rosaline Franklin','William Gosset'],
			'Born': ['1920-07-25','1876-06-13'],
			'Died': ['1958-04-16','1937-10-16'],
			'Occupation': ['Chemist','Statistician'],
			'Age': [37,61]},

			#use a column like index
			index=['Rosaline Franklin','William Gosset'],
			columns=['Occupation','Born','Died','Age'])

	print (scientists)

#create an ordered dataframe
def createOrderedDataFrame():
	scientists = pd.DataFrame(OrderedDict([
			('Name',['Rosaline Franklin','William Gosset']),
			('Born', ['1920-07-25','1876-06-13']),
			('Died', ['1958-04-16','1937-10-16']),
			('Occupation',['Chemist','Statistician']),
			('Age', [37,61])]))

	print(scientists)

if __name__ == '__main__':
	createSeries()
	createDataFrame()
	createOrderedDataFrame()