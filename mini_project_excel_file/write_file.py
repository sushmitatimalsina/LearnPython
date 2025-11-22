import pandas as pd

data = {
    "Name": ["john", "sita", "Ram", "hari", "maya"],
    "Age": [33, 44, 55, 56 ,59],
    "City": ["kathmandu", "pokhara", "banepa", "chapur", "rautahat"],
    "Salary": [ 20000, 400000,500000,40000,200000]
}
df = pd.DataFrame(data)
df.to_excel("customer.xlsx",index= False)