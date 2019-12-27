# Name: Cholpon Zamir
# Date: 2019-09-12


"""A module to calculate the tuition of a UMD student based on their residency status, major, and credits amount"""


def get_user_info():
    """A function to get the necessary information from the student for tuition calculation purposes
    """

    credits = float(input("Please enter the number of credits you are enrolled in."))  # get credits number
    resident = input("Are you an in-state resident? State yes or no.")  # in state or out of state student
    if resident == "yes":  # see if string is yes
        resident = True
    if resident == "no":
        resident = False
    special_major = input("Are you a Business, Engineering, or Computer Science major? State yes or no.")  # pay more
    if special_major == "yes":
        special_major = input("Are you a Junior or a Senior?")
        if special_major == "yes":
            special_major = True
        if special_major == "no":
            special_major = False
    if special_major == "no":
        special_major = False

    print(calculate_tuition(credits, resident, special_major))


def calculate_tuition(credits, resident, special_major):
    """A function to calculate tuition
    Args:
        Credits (float): the number of credits that the student is enrolled in
        resident (boolean): whether the student is a resident(True) or not (False)
        special_major (boolean): whether the student is a junior or senior in CS, Engineering, or Business
    Returns:
        total (float): the calculated total based on all the information inputted by the user
    """
    if resident == True:
            if credits < 12:
                total = credits*360
                if credits >= 9:
                    total = total+972
                if special_major == True:
                    total = total+(credits*116)

                if credits == 1 or credits <= 8:
                    total = total+453
                if credits == 0:
                    total = 0
            if credits >= 12:
                total = 4325.5+972  # 12 credits price + mandatory fee for 9 + credits
                if special_major == True:
                    total = total+1400  # full time special major fee


    if resident == False:
            if credits < 12:  # part time non resident
                total = credits*813 # part time non resident per credit price
                if credits >= 9:
                    total = total+972  # mandatory fee for 9+ credits
                if special_major == True:
                    total = total+(credits*116)  # mandatory per credit special major fee

                if credits == 1 or credits <= 8:
                    total = total + 453  # part time student mandatory fee
                if credits == 0:
                    total = 0
            if credits >= 12:  # full time non resident
                total = 16636 + 972 # fee for full time non resident and mandatory fee for 9 + credits
                if special_major == True:
                    total = total+1400  # full time special major fee
    return total


if __name__ == "__main__":
    """This is the main function"""
    get_user_info()
