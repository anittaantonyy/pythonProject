class MyRules:
    def check_odd_even(self, number):
      if number % 2 == 0:
          print(f"{number} is even")
      else:
          print(f"{number} is odd")

    def check_vote_eligibility(self, age):
        if age >= 18:
            print("The citizen is eligible to vote")
        else:
            print("The citizen is not eligible to vote")

    def check_number_range(self, number):
        if number >= 20 and number <= 50 and number % 5 == 0:
            print(f"{number} is between 20 and 50 and divisible by 5")
        else:
            print(f"{number} does not meet the criteria")

x = MyRules()
x.check_odd_even(10)
x.check_vote_eligibility(25)
x.check_number_range(25)
def create_triangle_pattern(rows):
  for i in range(0, rows):
      for j in range(0, i + 1):
          print("*", end=' ')
      print("\r")

create_triangle_pattern(5)
