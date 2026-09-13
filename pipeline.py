import pandas as pd

# TO CONVERT FROM CSV TO PANDAS 

data=pd.read_csv("sales.csv")

#MISSING VAULES 
print("missing values: ",data.isnull().sum())

# Remove duplicates

res=data.drop_duplicates()

#Convert data type

res["order_date"]=pd.to_datetime(res["order_date"])

#Clean strings
res["customer"]=res["customer"].str.strip()

#Calculate total_amount
res["total"]=res["quantity"]*res["price"]

#save 
res.to_csv("fianl.csv",index=False)

