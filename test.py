import pandas as pd

# create a DataFrame with the variable and constants
df = pd.DataFrame({
    'variable': [1, 2, 3, 4, 5],
    'constant1': [20, 40, 40, 20, 10],
    'constant2': [100, 200, 300, 400, 500]
})

# compute the correlation coefficient between the variable and the constants
correlations = df[['variable', 'constant1', 'constant2']].corr()['variable'][1:]

print(correlations)
