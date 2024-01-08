# Conditions with variables
DevOps = ["Linux","AWS","Jenkins","Python","Ansible","Docker","Kubernetes"]
Development = ("Java",".Net","C")

empl1 = {"Name":"ABC","Skill":"IOT"}
empl2 = {"Name":"xyz","Skill":"AI"}

usr_skill = input("Enter your desired skill :")
print(usr_skill)

# Check, if the skill is available in Database:
if usr_skill in DevOps:
    print(f"The skill {usr_skill} is available in DevOps")
elif usr_skill in Development:
    print(f"The skill {usr_skill} is available in Development")
elif usr_skill in empl1.values() or usr_skill in empl2.values():
    print("The employees the skill")
else:
    print("The skill is not found")
