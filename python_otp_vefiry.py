import random  # Importing the random module for generating OTP
def generate_otp():  # Function to generate a 6-digit OTP randomly
    otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
    return otp
def send_otp(email, otp):  # Function to simulate sending the OTP to the user's email address
    print("OTP has been sent to your email:", email)  # Notify user that OTP has been sent
    print("OTP:", otp)  # Display the OTP
def enter_otp():  # Function to prompt the user to enter the OTP received in their email
    user_otp = int(input("Enter the OTP received in your email: "))  # Prompt user to enter OTP
    return user_otp
def verify_otp(otp, user_otp):  # Function to verify if the entered OTP matches the generated OTP
    if otp == user_otp:  # Verification
        return "OTP verification completed. Access granted!"  # Return success message
    else:
        return "Invalid OTP. Access denied."  # Return failure message
def otp_verification():  # Function to perform OTP verification
    print("Welcome to OdinSchool Email Verification")  # Display welcome message
    email = input("Enter your email: ")  # Prompt user to enter email
    otp = generate_otp()  # Generate OTP
    send_otp(email, otp)  # Send OTP to user's email
    entered_otp = enter_otp()  # Prompt user to enter OTP
    result = verify_otp(otp, entered_otp)  # Verify entered OTP
    return result  # Return verification result
# Perform OTP verification
verification_result = otp_verification()
print(verification_result)  # Print verification result
'''(or) without functions 
import random 
print("welcome to email verification ")
email=input("enter your email:")
print("otp have been sent your",email)
otp=random.randint(100000,999999)
print("otp",otp," received from odinschool")
user_otp=int(input("enter your otp:"))
if otp==user_otp:
    print("OTP verification completed. Access granted!") 
else:
    print("invalid otp ! .Access denied.") '''
