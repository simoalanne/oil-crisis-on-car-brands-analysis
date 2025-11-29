def set_and_save_plot(
    fig, ax, title: str, xlabel: str, ylabel: str, savepath: str
):
    fig.suptitle("")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.savefig(savepath)
