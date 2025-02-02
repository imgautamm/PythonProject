#Dictionary = collection of key-value pairs

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "UK":"London",
            "France":"Paris",
            "Germany":"Berlin"}

#print(capitals.get("USA"))

#if capitals.get ("Japan"):
#    print("Capital exists")
#else:
#    print("Capital does not exists")

#capitals.update({"Germany":"Munich"})
#print(capitals)

keys = capitals.keys()
for key in capitals.keys():
    print(key)
values = capitals.values()
for value in capitals.values():
    print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key} : {value}")