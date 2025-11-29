while True:
    name = input("Enter your name: ")
    if name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid input. Please enter letters only.")
f_name=input("enter father name:")
m_name=input("enter mother name:")
std = input("enter your standared:")
ROLL_NO = int(input("enter your roll number:"))
adm_no = int(input("enter your adm_no.:"))
    
eng = int(input("enter your english marks:"))
math = int(input("enter your maths marks:"))
com = int(input("enter your computer science  marks:"))
phy = int(input("enter your physics marks:"))
chem = int(input("enter your chemistry marks:"))
phy_ed = int(input("enter your physical_education marks:"))
sum = eng+math+com+phy+chem+phy_ed
percentage = (sum/6)
print()
print()
print()
print("----------- RESULT CARD -----------")
print()
print("----------- GOOD LUCK -----------")
print()

print("STUDENT NAME:",        name)
print("CLASS:",std,", ROLL:",   ROLL_NO)
print("ADMISSION NUMBER:",    adm_no)
print("FATHER NAME:",        f_name)
print("MOTHER NAME:",        m_name)

if eng > 100:
    print("MARKS SHOULD BE LESS THAN 100")
elif eng >=90 and eng <=100:
    print("ENGLISH GRADE = A")
elif eng >=80 and eng <=89:
    print("ENGLISH GRADE = B")
elif eng >=70 and eng <=79:
    print("ENGLISH GRADE = C")
elif eng >=60 and eng <=69:
    print("ENGLISH GRADE = D")
else:
    print("ENGLISH GRADE = E")

if math > 100:
    print("MARKS SHOULD BE LESS THAN 100")
elif math >=90 and math <=100:
    print("MATHS GRADE = A")
elif math >=80 and math <=89:
    print("MATHS GRADE = B")
elif math >=70 and math <=79:
    print("MATHS GRADE = C")
elif math >=60 and math <=69:
    print("MATHS GRADE = D")
else:
    print("MATHS GRADE = E")
    
if com > 100:
    print("MARKS SHOULD BE LESS THAN 100")
elif com >=90 and com <=100:
    print("COMPUTER_SCIENCE GRADE = A")
elif com >=80 and com <=89:
    print("COMPUTER_SCIENCE GRADE = B")
elif com >=70 and com <=79:
    print("COMPUTER_SCIENCE GRADE = C")
elif com >=60 and com <=69:
    print("COMPUTER_SCIENCE GRADE = D")
else: 
    print("COMPUTER_SCIENCE GRADE = E ")

if phy > 100:
    print("MARKS SHOULD BE LESS THAN 100")
elif phy >=90 and phy <=100:
    print("PHYSICS GRADE = A")
elif phy >=80 and phy <=89:
    print("PHYSICS GRADE = B")
elif phy >=70 and phy <=79:
    print("PHYSICS GRADE = C")
elif phy >=60 and phy <=69:
    print("PHYSICS GRADE = D")
else:
    print("PHYSICS GRADE = E")

if chem > 100:
    print("MARKS SHOULD BE LESS THAN 100")
elif chem >=90 and chem <=100:
    print("CHEMISTRY GRADE = A")
elif chem >=80 and chem <=89:
    print("CHEMISTRY GRADE = B")
elif chem >=70 and chem <=79:
    print("CHEMISTRY GRADE = C")
elif chem >=60 and chem <=69:
    print("CHEMISTRY GRADE = D")
else:
    print("CHEMISTRY GRADE = E")


if phy_ed > 100:
    print("MARKS SHOULD BE LESS THAN 100")
elif phy_ed >=90 and phy_ed <=100:
    print("PHYSICAL_EDUCATION GRADE = A")
elif phy_ed >=80 and phy_ed <=89:
    print("PHYSICAL_EDUCATION GRADE = B")
elif phy_ed >=70 and phy_ed <=79:
    print("PHYSICAL_EDUCATION GRADE = C")
elif phy_ed >=60 and phy_ed <=69:
    print("PHYSICAL_EDUCATION GRADE = D")
else:
    print("PHYSICAL_EDUCATION GRADE = E")

print(f"PERCENTAGE OF {name} : {percentage}")

print()
print()
print()
print("----------- GOOD LUCK -----------")