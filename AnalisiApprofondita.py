print("\nMatrice di correlazione:")
print(df.corr(numeric_only=True))

print("\nMedia per specie:")
print(df.groupby("species").mean(numeric_only=True))

print("\nValori massimi per specie:")
print(df.groupby("species").max(numeric_only=True))
