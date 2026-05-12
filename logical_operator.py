print("------Pyloan Approval System------")
salary=int(input("Enter your salary:"))
age=int(input("Enter your age:"))
existing_loan=input("Do you have an existing loan (yes/no):")
employability_status=input("Enter your employability status:(yes/no)")
pay_bills_on_time=input("Do you pay bills on time:(yes/no)")
having_a_saving_account=input("Do you have an saving account:(yes/no)")
credit_score=0
if salary>=30000:
    credit_score+=30
if existing_loan=="yes":
    credit_score+=30
if pay_bills_on_time=="yes":
    credit_score+=20
if having_a_saving_account=="yes":
    credit_score+=20
if age>=21:
    credit_score+=20

if credit_score>=70 and employability_status=="yes" and age>=21:
    print("Loan Approved")
elif credit_score>50 and employability_status=="yes"and age>=21:
    print("Having a chance to get approved")
else:
    print("No chance to get approved")
