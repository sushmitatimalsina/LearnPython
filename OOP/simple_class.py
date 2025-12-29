import pandas as pd

# class DataProcessor:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.df = None

#     def load_data(self):
#         self.df = pd.read_csv(self.file_path)
#         print("data loaded successfully")
#         return self.df 

#     def clean_data(self):
#         # Example: Drop missing values
#         self.df = self.df.dropna()
#         print("Missing values dropped")
#         return self.df  
        
#     def show_head(self, n=5):
#         print(self.df.head(n))   
# processor = DataProcessor("users.csv")
# processor.load_data()
# processor.clean_data()
# processor.show_head()   
# 
# 
class User:
    def __init__(self, name, email):
        self.name = name       # attribute
        self.email = email

    def greet(self):           # method
        print(f"Hello, my name is {self.name}")

# Create object
user1 = User("Ram", "ram@gmail.com")
user1.greet()  

user2 = User("Sita", "sita@gmail.com")
user3 = User("Hari", "hari@gmail.com")

users = [user1, user2, user3]

for u in users:
    u.greet()

class ETL:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.data = None

    def extract(self):
        self.data = pd.read_csv(self.input_file)
        print("Data extracted")

    def transform(self):
        # Remove duplicates and fill nulls
        self.data = self.data.drop_duplicates()
        self.data["name"] = self.data["name"].fillna("Unknown")
        self.data["city"] = self.data["city"].fillna("Unknown")
        print("Data transformed")

    def load(self):
        self.data.to_csv(self.output_file, index=False)
        print("Data loaded")

# Using the ETL pipeline
etl = ETL("users_clean.csv", "users_final.csv")
etl.extract()
etl.transform()
etl.load()    