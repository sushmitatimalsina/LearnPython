import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("data loaded successfully")
        return self.df 

    def clean_data(self):
        # Example: Drop missing values
        self.df = self.df.dropna()
        print("Missing values dropped")
        return self.df  
        
    def show_head(self, n=5):
        print(self.df.head(n))   
processor = DataProcessor("users.csv")
processor.load_data()
processor.clean_data()
processor.show_head()        