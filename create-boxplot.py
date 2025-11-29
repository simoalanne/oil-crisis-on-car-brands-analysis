import matplotlib.pyplot as plt
from fetchalldata import fetchalldata
from measurable_keys import measurable_keys
from shared import set_and_save_plot


def create_boxplot(
    df, key: measurable_keys, title: str, xlabel: str, ylabel: str, savepath: str
):
    fig, ax = plt.subplots(figsize=(8, 5))
    df.boxplot(column=key, by="origin", ax=ax)
    set_and_save_plot(fig, ax, title, xlabel, ylabel, savepath)


# Adjust to create different boxplots as needed
create_boxplot(
    fetchalldata(),
    "fuel_ec",
    "Polttoainetehokkuus eri alueiden välillä",
    "Alue",
    "Polttoainetehokkuus (l/100km)",
    "fuel_efficiency_between_origins.png",
)
