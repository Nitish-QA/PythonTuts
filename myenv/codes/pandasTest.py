import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
    
# Accessing columns
print("\nColumn 'Name':")
print(df['Name'])

# Accessing rows by index
print("\nRow at index 2:")
print(df.loc[2])

# Filtering based on a condition
print("\nPeople above 25 years old:")
print(df[df['Age'] > 25])

# Adding a new column
df['Occupation'] = ['Engineer', 'Doctor', 'Student', 'Manager', 'Teacher']

# Sorting the DataFrame
df_sorted = df.sort_values(by='Age', ascending=False)

# Display the sorted DataFrame
print("\nSorted DataFrame:")
print(df_sorted)
