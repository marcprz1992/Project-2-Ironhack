import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Configuration to set so that all the Seaborn figs come out with this size
sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")

def violin (df, col1, col2, title, n):
    path = f"images/violin_{n}.jpg"
    fig = sns.violinplot(x=df[col1], y=df[col2])
    plt.title(title)
    fig.figure.savefig(path, dpi=1000)

