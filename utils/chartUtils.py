from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import date2num, DateFormatter
import utils.osUtils as osu
import utils.databaseUtils as dbu
import mplfinance as mpl
import pandas as pd


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
    # x = [int(str(e[0])[:-3]) for e in data[type]]
    y = [e[1] for e in data[type]] # Main Stuff

    clr = "limegreen" if y[0] < y[len(y)-1] else "firebrick"

    fig, ax = plt.subplots(figsize=(16,9))
    ax.grid()
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M\n%d %b,%y"))
    ax.yaxis.set_major_locator(plt.MaxNLocator(25))

    plt.ylabel(vs_curr.upper())

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

def make_ohlc_chart(id:str, vs_curr:str, days:str, save_name:str):

    assert days in ['1','7','14','30','90','180','365',"max","Max"], "Given Day Out of range."

    file = cg.get_coin_ohlc_by_id(id,vs_curr,days.lower())
    data = pd.DataFrame(file,columns=["time","open","high","low","close"])
    data.set_index("time")
    data['time'] = data['time'].apply(lambda x: int(str(x)[:-3]))

    data.index = pd.to_datetime(data["time"],unit='s')

    mpl.plot(
        data,
        style=mpl.make_mpf_style(marketcolors=mpl.make_marketcolors(up='limegreen',down='firebrick',inherit=True),gridstyle='-'),
        type="ohlc",
        savefig=dict(fname=f'./charts/{save_name}.png',bbox_inches="tight",dpi=int(osu.get("DPI")),orientation='landscape'),
        ylabel=vs_curr.upper(),
        tight_layout=True,
        figratio=(16,9),figscale=1.5,
        datetime_format='%H:%M\n%d %b,%y',
        xrotation=0
    )


def make_ranged_chart(coin_id:str, vs_curr:str, from_timestamp:int, to_timestamp:int, type:str, save_name:str):
    check_type = {
        "p": "prices",
        "m": "market_caps",
        "t": "total_volumes"
    }
    type = check_type.get(type[-1].lower())

    data = dict(cg.get_coin_market_chart_range_by_id(id=coin_id,vs_currency=vs_curr,from_timestamp=from_timestamp,to_timestamp=to_timestamp))

    x = [datetime.datetime.fromtimestamp(int(str(e[0])[:-3])) for e in data[type]]
    # x = [int(str(e[0])[:-3]) for e in data[type]]
    y = [e[1] for e in data[type]] # Main Stuff

    clr = "limegreen" if y[0] < y[len(y)-1] else "firebrick"

    fig, ax = plt.subplots(figsize=(16,9))
    ax.grid()
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M\n%d %b,%y"))
    ax.yaxis.set_major_locator(plt.MaxNLocator(25))

    plt.ylabel(vs_curr.upper())

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