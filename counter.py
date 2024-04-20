def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    lines = []
    addresses = {}
    with open(name) as file:
        for line in file:
            lines.append(line)
    for line in lines:
        if line[:5] == "From ":
            address = line.split(' ')[1]
            addresses[address] = addresses.get(address, 0) + 1
    maxaddress = ""
    for address, count in addresses.items():
        if count > addresses.get(maxaddress, 0):
            maxaddress = address
    print(maxaddress, addresses[maxaddress])


# if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
