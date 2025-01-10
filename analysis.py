import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml

xlim = [8, 10]
scale_y = 1.1
key = '2024-12-26'

with open('data.yaml', 'r') as yml:
    data_info = yaml.safe_load(yml)

file_path = data_info[key]["file_path"]
label = data_info[key]["label"]
ncol = len(label)

columns = [
    "SMU-V(+)", "SMU-V(-)",
    "SMU-V(+-)/ABS", "SMU-I(+)", "SMU-I(-)", "SMU-I(+-)/ABS",
    "temp-ch1 (K)", "EX. temp-ch1(K)", "magnetic Field-ch1 (Oe)", "2700-CH1(+)", "2700-CH1(-)", "2700-CH1(+-)",
    "R(+-)-2700-CH1", "Unused1", "Unused2", "Unused3", "DMM-2182-CH1(+)", "DMM-2182-CH1(-)", "DMM-2182-CH1(+-)/ABS",
    "R(+-)-2182-CH1", "temp-ch3 (K)", "EX. temp-ch3(K)", "magnetic Field-ch3 (Oe)", "2700-CH3(+)", "2700-CH3(-)", 
    "2700-CH3(+-)", "R(+-)-2700-CH3", "Unused4", "Unused5", "Unused6", "DMM-2182-CH4(+)", "DMM-2182-CH4(-)", 
    "DMM-2182-CH4(+-)/ABS", "R(+-)-2182-CH4", "temp-ch5 (K)", "EX. temp-ch5(K)", "magnetic Field-ch5 (Oe)", 
    "DMM-CH5(+)", "DMM-CH5(-)", "DMM-CH5(+-)", "R(+-)-CH5", "temp-ch6 (K)", "EX. temp-ch6(K)", "magnetic Field-ch6 (Oe)",
    "DMM-CH6(+)", "DMM-CH6(-)", "DMM-CH6(+-)", "R(+-)-CH6", "Time(sec)",
]

# Need to specify number of columns in usecols since number of columns in the header and data rows differ !!
# There are two additional columns in the data rows and the first two columns will be ignored without specifying the number of columns
data = pd.read_csv(file_path, sep='\t', skiprows=3, usecols=range( len(columns) )) 

# Set Seaborn style
# sns.set(style="whitegrid")
sns.set(style="darkgrid")
pd.set_option('display.max_columns', 1000)


color = [
    'purple',
    'brown',
    'blue'
]

Temperature = 'temp-ch1 (K)'
Resist = [
    'R(+-)-2700-CH1',
    'R(+-)-2182-CH1',
    'R(+-)-2700-CH3'
]

## Values are not stored in the correct keys...
## The first two columns are ignored
# print(data.columns)
# data.columns = columns[:len(data.columns)]

# Temperature = 'SMU-I(-)'
# Resist = [
#     '2700-CH1(-)',
#     'DMM-2182-CH1(-)',
#     '2700-CH3(-)'
# ]

# Preview the first few rows of the data
print(data.head(1).iloc[0])

# Plot multiple channels
fig, axs = plt.subplots(1, ncol, figsize=(4 * ncol, 4), sharex=True)

for i in range( ncol ):
    # Plot Resistance vs Temperature
    sns.lineplot(x=Temperature, y=Resist[i], data=data, ax=axs[i], label=label[i], color=color[i])
    # axs[i].plot(data[Temperature], data[Resist[i]], label= f"ch{i+1}", color=color[i])

    ymin, ymax = axs[i].get_ylim()
    axs[i].set_ylim([ymin, scale_y * ymax])
    axs[i].get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
    axs[i].get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
    axs[i].grid(which='major', color='w', linewidth=1.0)
    axs[i].grid(which='minor', color='w', linewidth=0.5)
    if xlim:
        axs[i].set_xlim(xlim[0], xlim[1])
    axs[i].set_xlabel('Temperature (K)')
    axs[i].set_ylabel('Resistance (Ohm)')
    axs[i].legend(fontsize = 10)
    axs[i].set_title('Resistance vs Temperature')

plt.tight_layout()
plt.show()
