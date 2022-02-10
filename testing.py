from tabulate import tabulate as tb

table = [["Price on INR","23434"],["Market Cap in INR","23434"]]

print(tb(table,tablefmt="fancy_grid",numalign="center"))

# tb(val_list,tablefmt="fancy_grid",numalign="center",floatfmt=(".3f"))