import pandas as pd
data = pd.read_csv('Nato_.csv')
data.to_dict()



dict_for_nato = {row.letter : row.code  for (index,row) in data.iterrows()}



word = input("Enter a word: ").upper()
output= [dict_for_nato[letter] for letter in word]
print(output)
