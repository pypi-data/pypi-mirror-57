import pandas as pd

def min_max():
    
    #local variable
    j = 0
    
    #Selecting the dataset
    dataset = input("Enter dataset name:")
    df = pd.read_csv(dataset)
    
    #Columns available in dataset
    print("Columns available in dataset:")
    c = 0
    for i in df:
        c = c + 1
        print(c,"-",i)
        
    #Select your appropriate column    
    saved_column = input('Enter Column Name:')
    saved_column = df[saved_column]

    #Take number of elements from a particular columm
    rows = int(input("Enter number of records:"))
    
    #Finding the minimum and maximun value
    minA = int(min(saved_column.head(rows)))
    maxA = int(max(saved_column.head(rows)))

    #Enter the range values
    new_maxA = int(input("Enter max range:"))
    new_minA = int(input("Enter min range:"))
    
    print ("Element# : min_max value")
    print ("------------------------")
    
    for v in saved_column[:rows]:
        a = (v-minA)*(new_maxA-new_minA)
        b = maxA - minA
        min_max = (a/b) + new_minA
        j = j+1
        print(j,"\t\t","%.2f" % min_max)
        

min_max()