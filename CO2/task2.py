A. Using while loop
Python
Run
correct_otp = "246810"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    otp = input("Enter OTP: ").strip()

    if otp == "":
        print("Blank entry! Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Wrong OTP!")

    if attempts == 2:
        pass

else:
    print("Account locked for 30 minutes.")
B. Using for loop with range(3)
Python
Run
correct_otp = "246810"

for attempt in range(1, 4):

    while True:
        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank entry! This attempt will not count.")
            continue

        break

    if otp == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Wrong OTP!")
        print("Attempts used:", attempt)

else:
    print("Account locked for 30 minutes.")
