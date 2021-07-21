#...____TRAUMA CARE AND DOCTOR APPOINTMENT SYSTEM_____... 
print("\n""..........TRAUMA CARE AND DOCTOR APPOINTMENT SYSTEM..........""\n"
      "_____________________________________________________________") 
def DISTRICTS():
        print("\n"".............WELCOME TO TRAUMA CARE SYSTEM............")
        a="yes"
        while(a=="yes"):
            print("\n""SELECT YOUR DISTRICT :")
            print("\n","1.Alappuzha | 08.Kozhikode","\n",
                       "2.Ernakulam | 09.Malappuram","\n",
                       "3.Idukki    | 10.Palakkad","\n",
                       "4.Kannur    | 11.Pathanamthitta","\n",
                       "5.Kasaragod | 12.Thiruvananthapuram","\n",
                       "6.Kollam    | 13.Thrissur","\n",
                       "7.Kottayam  | 14.Wayanad","\n")
            choice=int(input("SELECT YOUR DISTRICT FROM 1 - 14 : "))
            if choice==1:
                f=open(r'D:\TRAUMA CARE\Alappuzha.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==2:
                f=open(r'D:\TRAUMA CARE\Ernakulam.txt',"r")
                str1=f.read()
                print(str1)           
            elif choice==3:
                f=open(r'D:\TRAUMA CARE\Idukki.txt',"r")
                str1=f.read()
                print(str1)           
            elif choice==4:
                f=open(r'D:\TRAUMA CARE\Kannur.txt',"r")
                str1=f.read()
                print(str1)           
            elif choice==5:
                f=open(r'D:\TRAUMA CARE\Kasaragod.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==6:
                f=open(r'D:\TRAUMA CARE\Kollam.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==7:
                f=open(r'D:\TRAUMA CARE\Kottayam.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==8:
                f=open(r'D:\TRAUMA CARE\Kozhikode.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==9:
                f=open(r'D:\TRAUMA CARE\Malappuram.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==10:
                f=open(r'D:\TRAUMA CARE\Palakkad.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==11:
                f=open(r'D:\TRAUMA CARE\Pathanamthitta.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==12:
                f=open(r'D:\TRAUMA CARE\Thiruvananthapuram.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==13:
                f=open(r'D:\TRAUMA CARE\Thrissur.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==14:
                 f=open(r'D:\TRAUMA CARE\Wayanad.txt',"r")
                 str1=f.read()
                 print(str1)                   
            else:
                print("ENTER THE RIGHT CHOICE FROM 1 - 14")
            a=input("DO YOU WANT TO CHANGE YOUR DISTRICT 'yes or no' : ")
        print("\n""..............THANKYOU FOR CHOOSING OUR SERVICE..............")    
def DOCTORS():
        print("\n"".............WELCOME TO DOCTOR APPOINTMENT SYSTEM............")
        c="yes"
        while c=="yes":
            print("\n""SELECT YOUR CATEGORIES :")
            print("\n","1.AYURVEDIC DOCTORS | 5.CARDIOLOGISTS  | 09.CHEST SPECIALISTS","\n",
                       "2.COSMETIC SURGEONS | 6.DENTISTS       | 10.ENT SPECIALISTS","\n",
                       "3.EYE SPECIALISTS   | 7.NEUROLOGISTS   | 11.PAEDIATRICIANS","\n",
                       "4.PSYCHIATRISTS     | 8.PSYCHOLOGISTS  | 12.VETERINARY","\n")
            choice=int(input("SELECT YOUR SERVICE FROM 1 - 12 : "))
            if choice==1:
                f=open(r'D:\TRAUMA CARE\AYURVEDIC_DOCTORS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==2:
                f=open(r'D:\TRAUMA CARE\COSMETIC_SURGEONS.txt',"r")
                str1=f.read()
                print(str1)           
            elif choice==3:
                f=open(r'D:\TRAUMA CARE\EYE_SPECIALISTS.txt',"r")
                str1=f.read()
                print(str1)           
            elif choice==4:
                f=open(r'D:\TRAUMA CARE\PSYCHIATRISTS.txt',"r")
                str1=f.read()
                print(str1)           
            elif choice==5:
                f=open(r'D:\TRAUMA CARE\CARDIOLOGISTS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==6:
                f=open(r'D:\TRAUMA CARE\DENTISTS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==7:
                f=open(r'D:\TRAUMA CARE\NEUROLOGISTS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==8:
                f=open(r'D:\TRAUMA CARE\PSYCHLOGISTS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==9:
                f=open(r'D:\TRAUMA CARE\CHEST_SPECIALISTS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==10:
                f=open(r'D:\TRAUMA CARE\ENT_SPECIALISTS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==11:
                f=open(r'D:\TRAUMA CARE\PAEDIATRICIANS.txt',"r")
                str1=f.read()
                print(str1)
            elif choice==12:
                f=open(r'D:\TRAUMA CARE\VETERINARY.txt',"r")
                str1=f.read()
                print(str1)
            else:
                print("ENTER THE RIGHT CHOICE FROM 1 - 12")
                break
            d=int(input("\n""Enter your choice 1-3 : "))
            if d>3:
                print("ENTER THE RIGHT CHOICE FROM 1 - 3")
                break
            name=input("\n""PATIENT'S NAME : ")
            email=input("EMAIL ID ( IF YOU HAVE ): ")
            phone_no=int(input("PATIENT'S CONTACT NUMBER : "))
            import calendar
            print("\n""......................CHOOSE YOUR DATE......................")
            year=int(input("\n""ENTER YEAR : "))
            month=int(input("ENTER MONTH '1-12' : "))
            print("\n",calendar.month(year,month))
            day=int(input("SELECT YOUR DAY :"))
            print("\n","......................CHOOSE YOUR TIME......................""\n",
              "\n","___________________________MORNING____________________________","\n",
              "\n","1. 9:30 | 2. 10:00 | 3. 10:30 | 4. 11:00 | 5. 11:30 | 6. 12:00""\n",
              "\n","___________________________EVENING____________________________","\n",
              "\n","7. 1:30 | 8. 2:00  | 9. 2:30  | 10. 3:00 | 11. 3:30 | 12. 4:00")
            choice=int(input("\n""SELECT YOUR APPOINTMENT TIME : "))
            print("\n","NAME:",name.upper(),"\n","EMAIL:",email.lower(),"\n","PHONE:",phone_no,"\n","DATE:",day,"|",month,"|",year,"\n")
            confirm=input("DO YOU WANT TO CONFIRM YOUR APPOINTMENT 'yes or no': ")      
            c=input("DO YOU WANT TO APPOINT ANOTHER DOCTOR 'yes or no' : ")
        print("\n""..............THANKYOU FOR CHOOSING OUR SERVICE..............")    
b="yes"
while(b=="yes"):
    print("\n""1.TRAUMA CARE""\n""2.DOCTOR APPOINMENT")
    choice=int(input("\n""Choose your service 1 or 2 : "))
    if choice==1:
        DISTRICTS()
    elif choice==2:
        DOCTORS()
    b=input("\n""DO YOU WANT TO CHANGE YOUR SERVICE 'yes or no' : ")
print("\n""..............THANKYOU FOR CHOOSING OUR SERVICE..............")    

