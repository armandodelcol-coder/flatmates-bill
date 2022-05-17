from src.classes import Bill, Flatmate

the_bill = Bill(amount=120, period='March 2022')
jhonny = Flatmate(name="Jhonny", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("Jhonny pays: ", jhonny.pays(bill=the_bill, flatmate2=mary))
print("Mary pays: ", mary.pays(bill=the_bill, flatmate2=jhonny))
