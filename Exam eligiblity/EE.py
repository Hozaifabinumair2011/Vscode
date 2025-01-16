def check_exam_eligibility(attendance, marks):
    """
    Check eligibility for the exam based on attendance and marks.
    Criteria:
    - Minimum attendance: 75%
    - Minimum marks: 40%
    """
    if attendance >= 75 and marks >= 40:
        return "Eligible for the exam."
    elif attendance < 75 and marks < 40:
        return "Not eligible: Attendance and marks are both below the required threshold."
    elif attendance < 75:
        return "Not eligible: Attendance below the required threshold."
    elif marks < 40:
        return "Not eligible: Marks below the required threshold."

# Input from the user
try:
    attendance = float(input("Enter attendance percentage (0-100): "))
    marks = float(input("Enter marks percentage (0-100): "))

    # Validate input range
    if 0 <= attendance <= 100 and 0 <= marks <= 100:
        result = check_exam_eligibility(attendance, marks)
        print(result)
    else:
        print("Please enter values between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter numeric values.")