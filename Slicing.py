name = "My name is Vardhan"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[-5])
print(name[-6])
print(name[-7])

# slicing
print(name[0:7])
print(name[:])
print(name[:8])
print(name[:11])
print(name[:18])
print(name[0:18])

# slicing of a tuple
devops=("linux","aws","jenkins","python","ansible")
print(devops)
print(devops[0])
print(devops[3])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][3:8][-4])

# Dictionary example
skills={"Cloud":["AWS","Azure","GCP"], "DevOps":("Linux","Jenkins","Python","Ansible")}
print(skills)
print(skills["Cloud"])
print(skills["DevOps"])

print(skills["Cloud"][0])
print(skills["Cloud"][1])
print(skills["Cloud"][-1])

print(skills["DevOps"][-1])
print(skills["DevOps"][-1][:3])