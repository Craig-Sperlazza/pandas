import pandas as pd

df = pd.read_csv('modified_pokemon.csv')

# for index, value in df.iterrows():
#     print(index, value)

#print(df.head(10))
#print(df.tail(10))


# Example: Average of all the pokemon stats for a certain type, grouped by type
print(df.groupby(['Type 1']).mean())

#Example 2: Do the same thing but sort by highest defense
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

#Example 2: Do the same thing but sort by highest attack
print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# .mean(), .sum(), .count() are the most common aggregate statistics----sum makes no sense here just an fyi
print(df.groupby(['Type 1']).sum().sort_values('Attack', ascending=False))

#.count()
#print(df.groupby(['Type 1']).count())
#The above looks sloppy. But you can add a count column and then total it and then bring back only the count column grouped by Type
#You can also use subtypes to group them further
df['Count'] = 1
df_sort = df.groupby(['Type 1', 'Type 2']).count()['Count']
print(df_sort)


