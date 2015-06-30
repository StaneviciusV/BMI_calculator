####################################
# Author Vaidotas                  #
#                                  #
# https://github.com/StaneviciusV  #
#                                  #
####################################

welcome = '''
# Underweight below 18.5
# Normal weight 18.5 - 24.9
# Overweight 25 - 29.9
# Obesity 30.0 and Above

Hello,
and welcome to BMI (Body Mass Index) calculator!
Let's check Your's!
'''

print welcome

def bmi_compare(x):
    print "It is "
    if x < 18.5:
        return "UDERWEIGHT."
    elif 18.5 <= x <= 24.9:
        return "NORMAL WEIGHT. You are Healthy!"
    elif 25 <= x <= 29.9:
        return "OVERWEIGHT."
    else:
        return "OBESE."


try:
    mass = float(raw_input("Write Your mass in 'kg': "))
    height = float(raw_input("Write Your height in 'cm': "))
    bmi = mass/(height/100)**2
except:
    quit("Only numeric inputs!")

print "Your BMI is:", bmi
print bmi_compare(bmi)

