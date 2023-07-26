import pandas as pd

file_path = "Species.txt"

# Read the tab-separated data from the text file into a DataFrame.
df = pd.read_csv(file_path, sep='\t')

#print(df.to_string())

print(df)

# Filter the DataFrame to only include rows with 'X' in the 'compartment' column.
Nucleus_df = df.loc[df['compartment'] == 'Nucleus']

Mitochondrion_df = df.loc[df['compartment'] == 'Mitochondrion']

Cytoplasm_df = df.loc[df['compartment'] == 'Cytoplasm']

Extracellular_df = df.loc[df['compartment'] == 'Extracellular']



# Print the filtered DataFrame.
print("Nucleus_df\n", Nucleus_df)
print("Mitochondrion_df\n", Mitochondrion_df)
print("Cytoplasm_df\n", Cytoplasm_df)
print("Extracellular_df\n", Extracellular_df)
#print(nucleus_df.to_string())