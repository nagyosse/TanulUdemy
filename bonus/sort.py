wating_list = ["sen", "ben", "john"]
wating_list.sort(reverse=True)
for index, item in enumerate(wating_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
    # help(list)
