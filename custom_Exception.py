class AccountNotFoundError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


AccNo = [1001, 1002, 1004, 1007, 1000]

try:
    Ac = int(input("Enter Your Account Number: "))

    if Ac not in AccNo:
        raise AccountNotFoundError("Sorry! Account Number Not Found...")

    print("Account Verified Successfully!")

except ValueError:
    print("ValueError: Please enter numbers only, not letters or symbols.")

except TypeError:
    print("TypeError: Invalid type encountered.")

except AccountNotFoundError as e:
    print(e)

else:
    print("No Exception Occurred...")

finally:
    print("Rest Code -> (Means Exception Was Handled...)")
