import csv
import pandas as pd

dataset_1=[]
dataset_2=[]

with open("final.csv", "r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("archive_dataset_sorted1.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1=dataset_1[0]
planet_data_1=dataset_1[1:]

headers_2=dataset_2[0]
planet_data_2=dataset_2[1:]

headers=headers_1+headers_2
planet_data=[]
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

with open("merged_dataset.csv") as input, open("merged.csv","w", newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row)

with open("merged.csv") as input, open("merged_updated.csv","w", newline='') as output:
    df=pd.read_csv("planet_data.csv")
    print(df.head())

    del df["luminousity"]
    del df["pl_orbperlim"]
    del df["pl_orbpererr2"]
    del df["pl_orbsmaxerr2"]
    del df["pl_orbsmaxlim"]
    del df["pl_orbeccenerr2"]
    del df["pl_radj"]
    del df["pl_radjerr1"]
    del df["pl_radjerr2"]
    del df["pl_radjlim"]
    del df["pl_dens"]
    del df["pl_denserr1"]
    del df["pl_denserr2"]
    del df["pl_denslim"]
    del df["pl_k2flag"]
    del df["st_disterr2"]
    del df["gaia_disterr2"]
    del df["gaia_gmagerr"]
    del df["rowupdate"]
    del df["st_raderr2"]
    del df["st_masserr2"]
    del df["st_tefferr2"]
