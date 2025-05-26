import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
     #Filter countries that meet either condition
    big = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Select only the required columns
    result = big[['name', 'population', 'area']]
    
    return result