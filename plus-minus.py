# imported from bard

import datetime

def calculate_age(date_of_birth):
  """Calculates the age of a person based on their date of birth.

  Args:
    date_of_birth: A datetime.date object representing the person's date of birth.

  Returns:
    An integer representing the person's age in years.
  """

  today = datetime.date.today()
  number_of_days = (today - date_of_birth).days
  age_in_years = number_of_days / 365.25
  age = round(age_in_years)
  return age


def main():
  date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
  date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
  age = calculate_age(date_of_birth)
  print("Your age is {} years.".format(age))


if __name__ == "__main__":
  main()


today = datetime.date.today()
print(today)
