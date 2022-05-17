from src.classes import Bill, Flatmate, PdfReport

amount = float(input('Enter the bill amount: '))
period = input('What is the bill period ? E.g. December 2020: ')

flatmate1_name = input('What is your name ? ')
flatmate1_days_in_house = int(input(f"How many days did {flatmate1_name} stay in the house during teh bill period ? "))

flatmate2_name = input('Who is the other flatmate ? ')
flatmate2_days_in_house = int(input(f"How many days did {flatmate2_name} stay in the house during teh bill period ? "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days_in_house)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days_in_house)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
