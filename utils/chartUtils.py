from tabnanny import check
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import date2num, DateFormatter
import utils.osUtils as osu
import utils.databaseUtils as dbu
# import databaseUtils as dbu

cg = CoinGeckoAPI()

def make_chart(coin_id:str, vs_curr:str, days:str, type:str, save_name:str):
    check_type = {
        "p": "prices",
        "m": "market_caps",
        "t": "total_volumes"
    }
    type = check_type.get(type[-1].lower())

    data = dict(cg.get_coin_market_chart_by_id(id=coin_id,vs_currency=vs_curr,days=days,interval="hourly"))

    x = [datetime.datetime.fromtimestamp(int(str(e[0])[:-3])) for e in data[type]]
    y = [e[1] for e in data[type]] # Main Stuff

    clr = "limegreen" if y[0] < y[len(y)-1] else "firebrick"

    fig, ax = plt.subplots()
    ax.grid()
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M\n%d %b,%y"))
    ax.yaxis.set_major_locator(plt.MaxNLocator(25))

    plt.ylabel(vs_curr.upper())

    fig.set_figwidth(16)
    fig.set_figheight(9)

    # plt.show()
    ax.annotate(
        vs_curr.upper()+ ": " + str(round(y[-1],8)) + "\nTime: " + x[-1].strftime("%H:%M\nDate: %d %b, %Y"),
        xy=(x[-1],y[-1]),
        xytext=(1.01, 0.5),xycoords='data',
        textcoords='axes fraction',
        arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"),
        bbox=dict(boxstyle="round", fc="0.8")
    )
    ax.set_title(dbu.get_coin_name(coin_id=coin_id) + "'s " + type.replace("_"," ").capitalize()[:-1])

    ax.plot(date2num(x),y,marker=".",markersize=1.2,linewidth=0.75,color=clr)
    plt.savefig(f'./charts/{save_name}.png',bbox_inches="tight",dpi=int(osu.get("DPI")),orientation='landscape')



# make_chart("shiba-inu","inr","1","p","hmmmlmao")