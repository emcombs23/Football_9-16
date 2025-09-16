import pandas as pd

# Read both CSV files
pass_df = pd.read_csv('pass_plays.csv')
rush_df = pd.read_csv('Rush_plays.csv')

# Combine the dataframes
plays_df = pd.concat([pass_df, rush_df], ignore_index=True)

# Save to plays.csv
plays_df.to_csv('plays.csv', index=False)

print('Combined CSV saved as plays.csv')
