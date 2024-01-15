'''
# Break
vaccines = ["covaxin","covishield","Sputnik V","Pfizer","AstraZeneca"]
for i in vaccines:
    print(i)
    if i == "Pfizer":
        print("Found vaccine")
        break
print("Out of the loop")

# Continue
vaccines = ["covaxin","covishield","Sputnik V","Pfizer","AstraZeneca"]
for i in vaccines:
    if i == "Pfizer":
        continue
    print(f"Found vaccine: {i}")
print("Out of the loop")
'''
'''
# Random/shuffle - break
import random
vaccines = ["covaxin","covishield","Sputnik V","Pfizer","AstraZeneca"]

random.shuffle(vaccines)
print(vaccines)

my_vaccine=random.choice(vaccines)
print("My vaccine is: ",my_vaccine)

for vac in vaccines:
    print(f"********Testing {vac}")
    if vac==my_vaccine:
        print("******************************")
        print(f"Test is successful for {vac}")
        print()
        break
    print("******************************")
    print("Test failed")
    print()
'''
# Random/shuffle - continue
import random
vaccines = ["covaxin", "covishield", "Sputnik V", "Pfizer", "AstraZeneca"]

random.shuffle(vaccines)
print(vaccines)

my_vaccine = random.choice(vaccines)
print("My vaccine is: ", my_vaccine)

for vac in vaccines:
    print(f"********Testing {vac}")
    if vac == my_vaccine:
        print("******************************")
        print(f"Test is successful for {vac}")
        print()
        continue
    print("******************************")
    print("Test failed")
    print()

