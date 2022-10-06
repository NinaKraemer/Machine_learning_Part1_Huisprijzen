
# data inlezen en beschrijven
import numpy as np
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd

#%matplotlib inline

#De gedownloade data is lokaal opgeslagen en deze laden we met pandas in in een DataFrame
df = pd.read_json("nl_for_sale_all_anon.json")

#eerst gaan we bekijken hoe de data in elkaar zit en welke attributen we allemaal hebben over de huizen in de dataset
df.info()

#ook bekijken we een aantal elementen van de dataset

# omzetten van data types
print(set(df.get("item_type")))

df["vraagprijs"] = df["vraagprijs"].str.replace(".", "")
df["vraagprijs"] = pd.to_numeric(df["vraagprijs"])
df["perceel"] = pd.to_numeric(df["perceel"])

#histogram maken bouwjaar
bouwjaar_all = []
bouwjaar_unique = []
for entry in df["bouwjaar"]:
    if entry:
        bouwjaar_all.append(entry)
        if entry not in bouwjaar_unique:
            bouwjaar_unique.append(entry)

print(bouwjaar_unique)
bouwjaar_all.sort()
plt.hist(bouwjaar_all, bins=len(bouwjaar_unique))
plt.xticks(range(len(bouwjaar_unique)))
plt.show()

#histogram kamers
plt.hist(df["kamers"])
plt.show()

#correlatiegrafiek woonoppervlakte en vraagprijs
plt.scatter(df["woonoppervlakte"], df["vraagprijs"])
plt.show()

#Eerst laden we een kaart van Nederland in
nl = gpd.read_file("https://stacks.stanford.edu/file/druid:st293bj4601/data.zip")
nlmap = nl.plot()


#Nu plotten we de huizen op basis van hun coordinaten op de kaart
houses = gpd.GeoDataFrame(geometry=gpd.points_from_xy(df['longitude'], df['latitude']))
houses.plot(ax=nlmap, color='red', markersize=0.5)
plt.show()

df.info()
