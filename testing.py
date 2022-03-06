from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

print(cg.get_coin_ohlc_by_id("bitcoin","inr","2"))
