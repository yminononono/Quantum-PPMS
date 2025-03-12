import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml, os
from InquirerPy import prompt
from InquirerPy.separator import Separator

# xlim = [8, 10]
xlim = False
scale_y = 1.1

with open('yaml/data.yaml', 'r') as yml:
    data_info = yaml.safe_load(yml)

questions = [
    {
        "type": "list",
        "message": "Select data:",
        "choices": data_info.keys(),
        "default": None,
    },
]

key = prompt(questions=questions)[0]

questions = [
    {
        "type": "list",
        "message": "Select file:",
        "choices": data_info[key]["file_path"],
        "default": None,
    },
]

file_path = os.path.join('data', prompt(questions=questions)[0])
label = data_info[key]["label"]
ncol = len(label)

XValue = data_info[key]["xvalue"]
YValue = data_info[key]["yvalue"]

with open('yaml/column.yaml', 'r') as yml:
    data_info = yaml.safe_load(yml)
columns = data_info['columns']

# Need to specify number of columns in usecols since number of columns in the header and data rows differ !!
# There are two additional columns in the data rows and the first two columns will be ignored without specifying the number of columns
# Two ways to fix this

# Store column info in data.yaml and get the number of columns
# data = pd.read_csv(file_path, sep='\t', skiprows=3, usecols=range( len(columns) )) 
# Get number of columns in the header and reread the data using the number of columns
data = pd.read_csv(file_path, sep='\t', skiprows=3)
data = pd.read_csv(file_path, sep='\t', skiprows=3, usecols=range( len(data.columns) )) 

# Set Seaborn style
# sns.set(style="whitegrid")
sns.set(style="darkgrid")
pd.set_option('display.max_columns', 1000)


color = [
    'purple',
    'brown',
    'blue'
]


# Preview data in the first row
print(data.head(1).iloc[0])

# Plot multiple channels
fig, axs = plt.subplots(1, ncol, figsize=(4 * ncol, 4), sharex=True)

for i in range( ncol ):
    # Plot Resistance vs Temperature
    sns.lineplot(x=XValue, y=YValue[i], data=data, ax=axs[i], label=label[i], color=color[i])
    # axs[i].plot(data[XValue], data[YValue[i]], label= f"ch{i+1}", color=color[i])

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
plt.savefig('plots/' + key + '.png')
plt.show()
