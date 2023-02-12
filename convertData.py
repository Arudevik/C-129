import pandas as pd 

data = pd.read_csv("Pro-129/dwarfStars.csv")

data = data.dropna()

data["Radius"] = 0.102763*  data["Radius"]


data['Mass']=data['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

data['Mass'] = 0.000954588* data['Mass']

data.to_csv("Pro-129/convertedData.csv")






