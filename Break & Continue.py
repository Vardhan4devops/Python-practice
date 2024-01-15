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