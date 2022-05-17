from src.classes import Bill, Flatmate

the_bill = Bill(amount=250, period='March 2022')
jhonny = Flatmate(name="Jhonny", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print(jhonny.pays(bill=the_bill))
