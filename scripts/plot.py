from datetime import date

import matplotlib as mpl
import matplotlib.pyplot as plt

from scripts.database import return_degiro_balance


def create_weekly_plot() -> None:
    PRIMARY_COLOR, SECONDARY_COLOR = "#121619", "#0CAC64"

    year, week = date.today().isocalendar()[:2]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    mpl.rcParams['font.family']     = 'monospace'
    mpl.rcParams['text.color']      = SECONDARY_COLOR
    mpl.rcParams['axes.labelcolor'] = SECONDARY_COLOR
    mpl.rcParams['xtick.color']     = SECONDARY_COLOR
    mpl.rcParams['ytick.color']     = SECONDARY_COLOR

    mpl.rcParams['font.size']       = 14
    mpl.rcParams['axes.linewidth']  = 1.5

    fig = plt.figure(figsize=(6, 4), tight_layout=True)
    ax = fig.add_subplot(111)

    ax.plot(range(5), return_degiro_balance(5)[::-1], 'o-', linewidth=1.5, color=SECONDARY_COLOR)

    ax.set_xticks(range(5))
    ax.set_xticklabels([day[:3] for day in days])

    ax.spines['bottom'].set_color(SECONDARY_COLOR)
    ax.spines['left'].set_color(SECONDARY_COLOR)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.set_ylabel("Final balance\n(in euros)")
    ax.set(facecolor = PRIMARY_COLOR)
    fig.patch.set_facecolor(PRIMARY_COLOR)
    fig.suptitle(f"Weekly report {year}/{week:02d}")
    
    plt.savefig(f'plots/weekly-report.png')