#Merge CSV file
import os
import pandas as pd

# You need to set the path where you have put all your archives! 
path = "/home/joao/Z-Tecs/Modelo/talisma_0/"

#Here you list the files in the directory
os.listdir(path)

# creates list with files to merge based on name convention
#choose the initial name of all the files and put in startswith('xxx')
#keep in mind that all the archives needs to start with the same name or word
file_list = [path + f for f in os.listdir(path) if f.startswith('peso')] 

# To see all the archives you're importing
print(file_list) 

# creates empty list to include the content of each file converted to pandas DF
csv_list = []
 
# reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file).assign(File_Name = os.path.basename(file)))

# merges single pandas DFs into a single DF, index is refreshed 
csv_merged = pd.concat(csv_list, ignore_index=True)

# Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv(path + 'peso_full.csv', index=False)

