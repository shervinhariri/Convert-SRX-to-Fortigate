list_of_Services = []
with open('allservices.txt') as searchfile:
    for line in searchfile:
        if "destination-port" in line:
            left,sep,right = line.partition(" application ")
            stripped_line = right.strip()
            line_list = stripped_line.split()
            list_of_Services.append(line_list)

print("config firewall service custom")
for object in list_of_Services:
    conf = f"edit {object[0]}\n        set tcp-portrange {object[2]}\n    next"
    print(conf)
print("end")
