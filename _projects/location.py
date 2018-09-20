import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

floodrisk = pd.read_csv("open_flood_risk_by_postcode.csv", header=None, names=[])
floodrisk.head()

elevation = pd.read_csv("open_postcode_elevation.csv", names=["Postcode", "Elevation/m"])
elevation.head()

houseprices = pd.read_csv("uk-housing-prices-paid.csv")
houseprices.head()

