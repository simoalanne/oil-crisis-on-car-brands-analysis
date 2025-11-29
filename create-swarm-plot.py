import matplotlib.pyplot as plt
from fetchalldata import fetchalldata
from measurable_keys import measurable_keys
from shared import set_and_save_plot


def create_swarm_plot(
    df,
    key1: measurable_keys,
    key2: measurable_keys,
    title: str,
    xlabel: str,
    ylabel: str,
    savepath: str,
):
    if key1 == key2:
        raise ValueError("key1 and key2 must be different measurable keys.")

    colors = {"USA": "red", "JP": "blue", "EU": "green"}

    fig, ax = plt.subplots(figsize=(8, 5))

    for origin, color in colors.items():
        subset = df[df["origin"] == origin]
        ax.scatter(subset[key1], subset[key2], label=origin, color=color, alpha=0.7)

    ax.legend()
    set_and_save_plot(fig, ax, title, xlabel, ylabel, savepath)

# Adjust to create different swarm plots as needed
create_swarm_plot(
    fetchalldata(),
    "fuel_ec",
    "hp",
    "Polttoainetehokkuuden ja hevosvoimien välinen korrelaatio",
    "Polttoainetehokkuus (l/100km)",
    "Hevosvoimat",
    "fuel_efficiency_hp_correlation.png",
)
