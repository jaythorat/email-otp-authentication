# Using smtplib for testing perpose you can choose Google's gmail API for production level
# Importing Modules
import smtplib
import random

class otp_verification:

    # Func. to generate random 4 digit no.
    def generate_otp(self):
        self.otp = random.randint(1000,9999)
        self.message = f"Your OTP for vrification is {self.otp}"

    # func to send mail with the help of smtp server
    def send_mail(self,receiver):
        # Note = make sure to enable less secure apps for senders google id
        # link to enavle it = https://myaccount.google.com/lesssecureapps
        email = 'senders.emailId@gmail.com'   
        password = 'sendersPassword'
        from_addr = email
        to_addrs = receiver
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465 )
        server.login(email, password)
        server.sendmail(from_addr, to_addrs, self.message)
        print('OTP sent successfully')
        server.quit()

    # To check if entered otp is valid or not
    def validate_otp(self):
        validate = int(input('Enter the otp you\' received '))
        print(self.otp)
        if validate == self.otp:
            print("OTP verification successful..!!!")
        else:
            print("Otp varification failed")

# Creating instance for class otp_verification
ov = otp_verification()
ov.generate_otp()
ov.send_mail("receivers.emailId@gmail.com")
ov.validate_otp()