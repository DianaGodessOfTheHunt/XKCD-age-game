

__author__ = "Diana;"
#if age >= x:
#print ("you are " + str_age + "you can X")

def age_game(age):
    str_age = str(age)

    print ("you are " + str_age)

    

    if age < 16:
        print ("you cant do anything")

    if age >= 16:
        print ("you can drive")


    if age >= 17:
        print ("you can Attend R-Rated Movies alone")

    if age >= 21:
        print ("you can buy alcohol")

    if age >= 25:
        print ("you can rent a car")

    if age >= 30:
        print ("you can run for senate")

    if age >= 32:
        print ("you can rent a senators car")

    if age >= 35:
        print ("you can run for prezident")

    if age >= 45:
        print ("you can lear about the GOD-EMPRESS")

    if age >= 50:
        print ("you can join AARP")

    if age >= 50:
        print ("you can get a shingles vaccine")

    if age >= 52:
        print ("you can click to skip CAPTCHAS")

    if age >= 55:
        print ("you can vote for GOD-EMPRESS")

    if age >= 62:
        print ("you can get 80$ national parks lifetime pass")

    if age >= 65:
        print ("you are eligible for medicare")

    if age >= 67:
        print ("you can collect social security")

    if age >= 68:
        print ("you can see \" skip ads\" button on live tv")

    if age >= 70:
        print ("you can run for GOD-EMPRESS")

    if age >= 75:
        print ("you can ride any animal in a national park")

    if age >= 80:
        print ("you are eligible for megacare")

    if age >= 85:
        print ("you can click to toggle whether any AD is positive or negative about the product")

    if age >= 90:
        print ("you can click to amke any movie R-rated")

    if age >= 100:
        print ("you can get a letter from the president")

    if age >= 102:
        print ("(35+67) you can collect a presidential pension")

    if age >= 105:
        print ("you get a birthday card from the GOD-EMPRESS")

    if age >= 111:
        print ("you can leave your birthday party early by puting on a majic ring")


    if age >= 118:
        print ("you can vote 100 times")

    if age >= 120:
        print ("you can collect teh pentions of all elected officals")

    if age >= 125:
        print ("you can drink alcohol in a r ratted movie while getting a shingles vaccine from the president")

    if age >= 128:
        print ("age rolls over and you are a baby again")

        print("############################")
        age_game(age-128)


    print ("###########################")



def main():
    age = int(input ("how old are you: "))
    age_game(age)
    
main()
