import pandas as pd

#Large Data Sets
#read in chunks at a time---in this case we will do 5 rows at a time

for df in pd.read_csv('modified_pokemon.csv', chunksize=5):
    print(df)

#you can also create a new dataframe with same columns but empty---I really dont understand what he is doing here to be honest
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified_pokemon.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    #use concat function to append two dataframes together
    new_df = pd.concat([new_df, results])

print(new_df)