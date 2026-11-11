print("------------------")
print("Welcome to Payup")
print("------------------")
print()
print("Please answer the following questions to add bill information")
print()
event = input("What was the event? ")
cost = int(input("How much was the bill? "))
service_charge =float(input("Was there a service charge percentage? "))
group = int(input("How many in your group? "))

total_service_charge = cost * service_charge / 100
total_cost = cost + total_service_charge
price_per_person = total_cost / group

print()
print("---------------------------------------------------")
print(f"Your groups bill for {event}")
print()
print(f"price £{cost:.2f}")
print(f"Service Charge £{total_service_charge:.2f}")
print(f"Total Price £{total_cost:.2f}")
print()
print(f"Each person owes {price_per_person:.2f}")
print()
print("---------------------------------------------------")




