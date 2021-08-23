import random as r
import string

# function to generate otp
def otp_generator(character):
    otp_character_list = character
    otp = ""
    for i in range(6):
        otp += r.choice(otp_character_list)
    return otp

#result
otp_sender = otp_generator(list(string.ascii_letters+string.digits))
print(otp_sender)
