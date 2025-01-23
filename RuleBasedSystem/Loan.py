def check_loan_eligibility():
    age = int(input("Enter the applicant's age: ").strip())
    stable_income = input("Does the applicant have a stable income? (yes/no): ").strip().lower()
    credit_score = int(input("Enter the applicant's credit score: ").strip())
    criminal_record = input("Does the applicant have a criminal record? (yes/no): ").strip().lower()
    loan_default = input("Has the applicant defaulted on a loan before? (yes/no): ").strip().lower()

    if criminal_record == "yes":
        return "The applicant is not eligible for a loan."
    elif loan_default == "yes":
        return "The applicant is not eligible for a loan."
    elif 18 <= age <= 65 and stable_income == "yes":
        return "The applicant is eligible for a loan."
    elif credit_score > 700:
        return "The applicant is eligible for a loan."
    else:
        return "The applicant is not eligible for a loan."


eligibility_result = check_loan_eligibility()
print(eligibility_result)
