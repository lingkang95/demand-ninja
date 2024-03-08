


import demand_ninja
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# %%



df=pd.read_csv('open-meteo-51.44N5.48E23m.csv',parse_dates=True,index_col=[0] )


# %%

inputs =df

# `result`` will be a pandas.DataFrame
# setting raw=True includes the input data and intermediate results
# in the final DataFrame
result = demand_ninja.demand(inputs, raw=True)


# result[result.index.date==result.index.date[0]][['total_demand', 'heating_demand', 'cooling_demand']].plot()
result[result.index.date == result.index.date[0]].iloc[:, 3:].plot(subplots=True)


plt.show()

result.to_csv('heat_demand_ninja.csv')
