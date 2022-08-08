import subprocess

from natsort import natsorted

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import glob
import time
import os

laptop = "new"      # "old" or "new"

# read data
datapath = "data.csv"
print(f"reading {datapath}")
if os.path.isfile(datapath):
    print("existing data found and used")
    df = pd.read_csv(datapath)
else:
    print("no file found, new one created")
    df = pd.DataFrame(columns=["name", "day", "task", "time", "laptop"])

# run and time the tasks
print("start timing")
paths = natsorted(glob.glob("week2/day8_task2.py"))
for path in paths:
    print(path)
    name = path.split("\\")[-1][:-3]
    day, task = name.split("_")
    for rep in range(2):
        start = time.perf_counter()
        subprocess.run(f"python {path}")
        rep_time = time.perf_counter() - start
        df.loc[len(df.index)] = [name, day, task, rep_time, laptop]

# write data
print("writing data")
df.to_csv("data.csv", index=False)
print(df)

# create graph
print("creating graph")
sns.barplot(x="day", y="time", hue="laptop", data=df, ci="sd", capsize=.2)
plt.yscale("log")


fig, axes = plt.subplots(ncols=3)
sns.barplot(x="day", y="time", hue="laptop", data=df, ci="sd", capsize=.2, ax=axes[0])
# sns.barplot(x="day", y="time", data=df, ci="sd", capsize=.2, ax=axes[0])
sns.barplot(x="laptop", y="time", data=df, capsize=.2, ax=axes[1])
sns.barplot(x="task", y="time", hue="laptop", data=df, capsize=.2, ax=axes[2])
plt.show()
