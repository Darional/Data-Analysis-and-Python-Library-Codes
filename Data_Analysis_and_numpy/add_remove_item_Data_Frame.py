import pandas as pd

# Creating a DataFrame
grocery_items = {'Items': ['Milk', 'Bread', 'Cheese', 'Butter'], 'Price': [2.5, 1.5, 3.5, 2.0]}
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
grocery_df['ID'] = [501, 502, 503, 504]
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
print("\n -------- Selecting an specific ID ---------- \n")
print(grocery_df.loc[[1]])