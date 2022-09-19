import os
import pandas as pd

# should read path from environment variables
dataPath = r"C:\Users\maxim\Work\financials\data"

file_names = os.listdir(dataPath)

acc_map = {}


for file_name in file_names:
    split_tup = os.path.splitext(file_name)
    pretext = split_tup[0]
    posttest = split_tup[1]
    if ".CSV" == posttest or ".csv" == posttest:
        id = pretext.split("_")[0]
        if id in acc_map:
            acc_map[id].append(file_name)
        else:
            acc_map[id] = [file_name]

# checkings and savings accounts are seperated by the "id" in the filename

for k, file_names in acc_map.items():
    df = pd.read_csv(os.path.join(dataPath, file_names[0]))
    print(df)

    # merge other data from that id
    for i in range(1, len(file_names)):
        temp = pd.read_csv(file_names[i])

        # line of code that merges

