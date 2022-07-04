list_of_lists = []
with open('alladdress.txt') as searchfile:
    for line in searchfile:
        if not any(value in line for value in ("ipv4-only", "description", "zone", "address-set")):
            left,sep,right = line.partition(" address ")
            stripped_line = right.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)

print("config firewall address")
for object in list_of_lists:
    conf = f"edit {object[0]}\n   set type ipmask\n   set subnet {object[0]} {object[1]}\nnext"
    print(conf)
print("end")
