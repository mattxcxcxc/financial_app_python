def user_inputs():
    while True:
        try:
            bi_weekly_income =float(input("Enter your bi-weekly income: "))
            rent =float(input("Enter your rent for apartment or house: "))
            car_payment =float(input("Enter your monthly car payment: "))
            car_insurance =float(input("Enter your monthly car insurance: "))
            if bi_weekly_income<=0:
                print('Bi-weekly income must be positive')
                continue
            if rent<0 or car_payment<0 or car_insurance<0:
                print("Expenses(rent,car_insurance,car_payment)cannot be negative")
                continue
            if bi_weekly_income>1000000:
                print("Bi_weekly income is a way to high,please re-enter")
                continue
            
            return {
                "bi_weekly_income":bi_weekly_income,
                "rent":rent,
                "car_payment":car_payment,
                "car_insurance":car_insurance
            }
        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")
       
    
def calculations(inputs):
        bi_weekly_income=inputs["bi_weekly_income"]
        rent=inputs["rent"]
        car_payment=inputs["car_payment"]
        car_insurance=inputs["car_insurance"]
        total_monthly_expenses=rent+car_payment+car_insurance
        
        bi_weekly_expenses=total_monthly_expenses/4.33
        remaining_income=bi_weekly_income-bi_weekly_expenses
        savings=remaining_income*0.20
        return {
            "bi_weekly_expenses":bi_weekly_expenses,
            "remaining_income":remaining_income,
            "savings":savings
        }
def display_results(inputs,results):
    print("\n"+"_"*30)
    print("Financial Summary:")
    print("_"*30)

    print(f"Your bi_weekly_income:$ {inputs['bi_weekly_income']:.2f}")
    print(f"Your rent:$ {inputs['rent']:.2f}")
    print(f"Your car_payment:$ {inputs['car_payment']:.2f}")
    print(f"Your car_insurance:$ {inputs['car_insurance']:.2f}")
    print(f"Your bi_weekly_expenses:$ {results['bi_weekly_expenses']:.2f}")
    print(f"Your remaining_income:$ {results['remaining_income']:.2f}")
    print(f"Your savings:$ {results['savings']:.2f}")

    if results['remaining_income']<0:
        print("\n Warning:Your expenses exceed your income:Consider reducing expenses.\n")
    print("_"*30+"\n")

while True:
    user_data=user_inputs()
    results_calc=calculations(user_data)
    display_results(user_data,results_calc)
    while True:
        repeat_program=input('Do you want to calulate again?(yes/no)').strip().lower()
        if repeat_program=='yes':
            break
        elif repeat_program=='no':
            print('Thank you for using the Financial app.Goodbye!')
            exit()
        else:
            print('Warning Invalid input,please enter yes or no.')

    
    
    
   
    