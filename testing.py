from tabulate import tabulate as tb

# table = [["Price on INR","23434"],["Market Cap in INR","23434"]]
table = [[14]]
print(tb(table,tablefmt="fancy_grid",numalign="center"))

from datetime import datetime as dt


dot = dt.strptime("2021-11-10T14:24:11.849Z","%Y-%m-%dT%H:%M:%S.%fZ")
print(str(dot.timestamp())[:-4])
# print(dt.timestamp("2021-11-10T14:24:11.849Z"))

print(len("LMaoooooo"))


