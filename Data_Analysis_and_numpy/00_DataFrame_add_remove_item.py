import pandas as pd
import numpy as np
from datetime import datetime
# Creating a DataFrame
grocery_items = {'Items': ['Milk', 'Bread', 'Cheese', 'Butter', 'Egg'],
                 'Price': [2.5, 1.5, 3.5, 2.0, 0.5],
                 'Origin': ['Cow', 'Wheat', 'Moon', 'Oil', 'Chicken']
}
grocery_df = pd.DataFrame(grocery_items)
# Adding items to DataFrame
new_items = pd.DataFrame({
    'Items': ['Cucumber', 'Radish'],
    'Price': [0.5, 0.3]
})
print("\n -------- Initial DataFrame ---------- \n")
print(grocery_df)



# We can set the index
print("\n -------- Setting an ID ---------- \n")
grocery_df['ID'] = [501, 502, 503, 504, 6]
grocery_df.set_index('ID', inplace=True) # We can use  inplace to modify the grocery_df and not to copy the variable.
print(grocery_df)



# We can reset the index
print("\n -------- Resetting the ID and Adding items ---------- \n")
grocery_df = pd.concat([grocery_df, new_items]).reset_index(drop=True)
print(grocery_df)



# Selecting and dropping Rows
print("\n -------- Dropping Rows ---------- \n")
index_to_drop = []
index_to_drop.append(grocery_df[grocery_df['Items'] == 'Cheese'].index)
index_to_drop.append(grocery_df[grocery_df['Items'] == 'Butter'].index)
for i in index_to_drop:
    grocery_df = grocery_df.drop(i)
print(grocery_df)



# Printing an specific id 
print("\n -------- Selecting an specific ID and specifying a column ---------- \n")
print(grocery_df.loc[[1]])
print(f'The items names: {grocery_df.loc[:,"Items"]}')
# The function grocery_df.iloc[2] returns the value in the position 2 (starting from 0)
print(f'Getting the position of the column "Price": {grocery_df.columns.get_loc("Price")}')
print(f'Getting the positions of the columns "Items" and "Price": {grocery_df.columns.get_indexer(["Items","Price"])}')
print(f'Getting the price of the milk using the ID: {grocery_df.iloc[grocery_df.index.get_loc(0), 1]}')
print(f'Getting the price of the milk using comparations: {grocery_df.loc[grocery_df["Items"]=='Milk', 'Price'].values[0]}')
print(f'Sampling the population of the grocery store: {grocery_df.sample(3, random_state=5)}') # extracts 3 samples over the row amounts
print(f'Sampling the columns grocery store: {grocery_df.sample(2, random_state=5, axis=1)}') # extracts 3 samples over the row amounts
print(f'Samplin a percentage of the DataFrame: {grocery_df.sample(frac = 0.6, random_state = 18)}') # Random state is used as a seed

# Printing the data of a DataFrame
print("\n -------- Describing the DataFrame & Info ---------- \n")
print(grocery_df.describe())
print(grocery_df.info())
# Also we can sort by value


'''
Practical use of DataFrames.


'''
# Setup
np.random.seed(42)
names = ["Ana", "Juan", "Marta", "Pedro", "Isabel", "Jorge", "Luisa", "Carlos", "Esther", "David"]
lastNames = ["García", "López", "Martínez", "Rodríguez", "González", "Fernández", "Ruiz", "Ramirez", "Morales", "Torres"]
hire_dates = pd.date_range(start="2015-01-01", end="2022-09-01", freq='M')
employees = {
    'Name': [f"{np.random.choice(names)} {np.random.choice(lastNames)}" for _ in range(100)],
    'Age': np.random.randint(20, 60, 100),
    'Salary ($)': np.random.randint(25000, 75000, 100),
    'Hire Date': np.random.choice(hire_dates, 100),
    'Job': np.random.choice(["Desarrollador", "Diseñador", "Gerente", "Analista"], 100)
}
df = pd.DataFrame(employees)
df.to_csv("employees.csv", index=False)

# Reading csv
dtypes = {'Age': 'float32', 'Salary': 'float32'} # Specifying which column has other type of value, this case is float
df = pd.read_csv('employees.csv', index_col=0, dtype=dtypes, parse_dates=["Hire Date"])
print(f'\n\n\n\n{df.head(5)}')
print(f'\nLooking for NaN values:\n {df.isna().sum()}')
print(f'\nEmployees hired after January 1 of 2020: \n{df[df["Hire Date"] > '2020-01-1'].head()}')
print(f'\nMean Salary of each Job: {df.groupby(by = "Job")["Salary ($)"].mean()}')
#Creating a Seniority Column
current_year = datetime.now().year
df["Seniority"] = current_year - df["Hire Date"].dt.year
print(f'\nAdding Seniority column:\n {df.head(10)}')
df_most_seniority = df[df["Seniority"] > 3]
best_paid = df_most_seniority.loc[df_most_seniority["Salary ($)"].idxmax(),["Age", "Salary ($)", "Job"]]
print('The most paid employee is:\n',best_paid)



print("\n -------- Cleaning Data ---------- \n")


data = {'A':[2, 4, None, 8],
        'B':[5, None, 7, 9],
        'C':[12, 13, None, None]}
df = pd.DataFrame(data)
print(df.isnull(), '\n')  # isnull() return a DataFrame with Boolean Values
df.dropna(inplace=True)  # erease all the rows that has None or Null values
print(df,'\n')

df = pd.DataFrame(data)
df['A'].fillna(0, inplace=True)  # Fulfill the None fields with some value.
df['B'].fillna(np.mean(df['B']), inplace=True)
df.fillna(100, inplace=True)
print(df)


print("\n\n -------- Handling Duplicates & Outliers ---------- ")

data = {'Name': ['John', 'Anna', 'Peter', 'John', 'Anna', 'Jose'],
        'Age': [16, 15, 13, 16, 15, 14],
        'Grade': [9, 10, 7, 9, 10, 98]}
df = pd.DataFrame(data)
print(df.duplicated())
df = df.drop_duplicates() # Drop the duplicated rows.
print(df)

# Calculating IQR for Grade
Q1 = df['Grade'].quantile(0.25)
Q3 = df['Grade'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR
print("Deleting outliers (Jose)")
df_without_outliers = df[(df['Grade'] > lower_bound) & (df['Grade'] < upper_bound)]
print(df_without_outliers)
print("Or just changing with the median")
median = df['Grade'].median()
df['Grade'] = np.where((df['Grade'] < lower_bound) | (df['Grade'] > upper_bound), median, df['Grade'])
print(df)

