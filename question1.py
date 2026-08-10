hours = int(input("Enter no of hours"))
t_amount = 0 
service_charge = 20 

if hours > 0  and hours <=2:
    t_amount = hours * 30   #30 rs for two hours
elif hours>2 and hours <= 5:
    t_amount = hours * 25  # 25 for 5 hrs
else:
    t_amount = hours * 20  # 20 for more than 5 hrs


if t_amount > 150:
    t_amount += service_charge  

print(t_amount)

