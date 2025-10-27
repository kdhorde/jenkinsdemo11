import pandas as pd
print('Extract data')

data ={
    'Id':[101,102,103],
    'Name':['ram','raj','raja'],
    'Age':[29,34,42]
    
}
df =pd.DataFrame(data)
print(df)