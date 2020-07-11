text = page
list_tostore = []
list_tostore = text.split(".")
print(list_tostore)
for i in list_tostore:
    if "information" or "rights" or "delete" in i:
        print(i)

