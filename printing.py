name = "Sars_cov_2"
disease = "Covid 19"

print("The name of the virus is: ", name)
print("The name of the virus is: {}" .format(name))
print("{} is the name of the virus".format(name))
print("the name of the virus is: {} and the disease is: {}".format(name, disease))

# the below print works only after python 3.6
print(f"the name of the virus is:{name} and the disease is:{disease}")

# concatenation
print("the name of the virus is:" + " "+name)


