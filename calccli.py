print("This is a calculator cpi program for your calculations this aims to make them easier")
import math as m
print('''Pls choose by entering the number infront of the menu item you wish to perform
          1.addition
          2.subtraction
          3.multiply
          4.divide
          5.exponentation
          6. square root
          7. tan
          8. sin 
          9.cos
          10.cosec
          11.sec
          12.cot
          13.factorial
          14 square
          15.ceiling
          16. modulus
          17. floor
          18. log
          19. log10
          20. degree to radians
          21.radians to degree
          22. power of function e''')
def get_number():
    while True:
        try:
            a=int(input("Pls enter your number"))
            return a 
        except ValueError:
            print("Only a no. reenter")

def badval():
    while True:
        try:
            a=int(input("Enter the menu"))
            if a<24 and a>0:
                return a
            print("Outta range")
        except ValueError:
            print("Menu value not in range")
         
def dval():
    while True:
        try:
            b=int(input("Enter ur number"))
            l.append(b)
            return l
        except ValueError:
            print("Sorry only nos. pls") 
def dval2():
    while True:
        try:
            b2=int(input("Enter ur menu pls"))
            if b2<=2 and b2>=1:
                return b2
            print('Menu out of range sir')
        except ValueError:
            print("Sorry only nos. pls")
def dval3():
    while True:
        try:
            b=int(input("Enter ur number"))
            l.append(b)
            try:
                difference=l[-2]-l[-1]
                l.append(difference)
                return l
            except IndexError:
                l.append(b)
                return l
        except ValueError:
            print("Sorry only nos. pls")
def dval4():
    while True:
        try:
            b=int(input("Enter ur number"))
            l.append(b)
            multiply=l[-2]*l[-1]
            l.append(multiply)
            return l
        except ValueError:
            print("Sorry only nos. pls")
def add_more_number():
            print('''you want to enter any more numbers
                  1.Yes
                  2.No
                  Enter the menu value pls''')
def dval5():
    while True:
        try:
            b_dividend=int(input('Enter your dividend'))
            b=int(input("Enter ur divisor"))
            while True:
                try:
                    q=float(b_dividend/b)
                    return q
                except ZeroDivisionError:
                    print("Aborting pls reenter zero division error")
                    b=int(input("This time dont enter a zero divisor"))

        except ValueError:
            print("Sorry only nos. pls")
def degree_to_radians():
    while True:
        try:
            k=int(input('Enter your value in degrees pls'))
            radi=m.radians(k)
            print("This is yourr value is radians",radi)
            return radi
        except ValueError:
            print('only nos pls')
def string_to_randians(text):#my first black box
    text=text.lower().replace("π","pi").replace("*","").replace(" ","")
    if "pi" in text:
        find_pi=text.find("pi")
        pre=text[:find_pi]
        if pre=="" or pre=="+":
            pre="1"
        elif pre=="-":
            pre="-1"
        numerator=float(pre)*m.pi
        if "/" in text:
            text2=text.split("/")
            denominator=float(text2[1])
            return numerator/denominator
        return numerator
    if 'pi' not in text:
        numerator=float(text)
        return numerator
def get_popup_menu():
    print("""Do you know you value in radians or not
        1.Yes
        2.No""")
    while True:
        try:
            k=int(input('Enter ur value of menu'))
            if k<3 and k>0:
                return k
            print("Menu outta range")
        except ValueError:
            print('Only numbers sir')
def return_trig_rsult():
    while True:
        try:
            inp_user=input('Enter value in radians')
            f=string_to_randians(inp_user)
            z=f
            return z
        except ValueError:
            print("Error in value reenter")
while True:
    c=badval()
    if c==1:
        l=[]
        f=dval()
        f=dval()
        while True:
            add_more_number()
            b3=dval2()
            if b3==1:
                 dval()
            if b3==2:
                 print("Thank You for your operations")
                 print('Your answer is',sum(f))
                 break
    if c==2:
        l=[]
        f=dval3()
        f=dval3()
        while True:
            add_more_number()
            b3=dval2()
            if b3==1:
                dval3()
            if b3==2:
                print("Thank You for your operations")
                print('Your answer is',l[-1])
                break
    if c==3:
        l=[1]
        f=dval4()
        f=dval4()
        while True:
            add_more_number()
            b3=dval2()
            if b3==1:
                dval4()
            if b3==2:
                print("Thank You for your operations")
                print('Your answer is',l[-1])
                break
    if c==4:
        f=dval5()
        print("The value after your operation is",f)
    if c==5:
        print("The nos. you will be entering will be used as base and exponent for your operation, first input is base the second input is an exponent")
        f=get_number()
        k=get_number()
        print('The value of ur operations is',m.pow(f,k))
    if c==6:
        f=get_number()
        print('Your value of the operation is',m.sqrt(f))
    if c==7:
        print("""Do you know you value in radians or not
        1.Yes
        2.No""")
        while True:
           try:
            k=int(input('Enter ur value of menu'))
            if k<3 and k>0:
                break
            print("Menu outta range")
           except ValueError:
               print('Only numbers sir')
        if k==1:
            g=return_trig_rsult()
            print("The val of your tan is",m.tan(g))
        if k==2:
            puredegree=degree_to_radians()
            print("The value of your tan is",m.tan(puredegree))
    if c==8:
        k=get_popup_menu()
        if k==1:
            g=return_trig_rsult()
            print("Your value in sin is",m.sin(g))
        if k==2:
            puredegree=degree_to_radians()
            print("The val of your sin",m.sin(puredegree))
    if c==9:
        k=get_popup_menu()
        if k==1:
            g=return_trig_rsult()
            print("Your value in sin is",m.cos(g))
        if k==2:
            puredegree=degree_to_radians()
            print("The val of your sin",m.cos(puredegree))
    if c==10:
        k=get_popup_menu()
        if k==1:
            g=return_trig_rsult()
            print("Your value in sin is",1/m.sin(g))
        if k==2:
            puredegree=degree_to_radians()
            print("The val of your sin",1/m.sin(puredegree))
    if c==11:
        k=get_popup_menu()
        if k==1:
            g=return_trig_rsult()
            print("Your value in sin is",1/m.cos(g))
        if k==2:
            puredegree=degree_to_radians()
            print("The val of your sin",1/m.cos(puredegree))
    if c==12:
        k=get_popup_menu()
        if k==1:
            g=return_trig_rsult()
            print("Your value in sin is",1/m.tan(g))
        if k==2:
            puredegree=degree_to_radians()
            print("The val of your sin",1/m.tan(puredegree))
    if c==13:
        while True:
            try:
                fact=int(input("Enter the number you would like to get a fcatorial of"))
                print("The value is",m.factorial(fact))
                break
            except:
                print("Reenter only nos. sir")
    if c==14:
        while True:
            try:
                sq=float(input("Enter the number you would like to get the square of"))
                print("The value is",sq*sq)
                break
            except:
                print("Reenter only nos. sir")
    if c==15:
        while True:
            try:
                ceil=float(input("Enter the number you would like to get ceiling of"))
                print("The value is",m.ceil(ceil))
                break
            except:
                print("Reenter only nos. sir")
    if c==16:
        while True:
            try:
                abs=float(input("Enter the number you would like to get a modulus of"))
                print("The value is",m.fabs(abs))
                break
            except:
                print("Reenter only nos. sir")
    if c==17:
        while True:
            try:
                floor=float(input("Enter the number you would like to get the floor of"))
                print("The value is",m.floor(floor))
                break
            except:
                print("Reenter only nos. sir")
    if c==18:
        while True:
            try:
                base=int(input("Enter the base"))
                num=int(input("Enter number"))
                print("The value is",m.log(num,base))
                break
            except:
                print("Issue in your input")
    if c==19:
        while True:
            try:
                log10num=int(input("Enter the number you would like to get the base 10 log of"))
                print("The value is",m.log10(log10num))
                break
            except:
                print("Reenter only nos. sir")
    if c==20:
        f=degree_to_radians()
    if c==21:
        while True:
            try:
                radians_to_degree=input("Enter your radians to get in degrees")
                f=string_to_randians(radians_to_degree)
                break
            except:
                print('Issue in ur value')
        print("your val in degree is",m.degrees(f))
    if c==22:
        exparg=int(input("Enter ur exponent you wish e to be raised to"))
        print('Your value is',m.exp(exparg))
        
    
        
                
        
                
            



        
            

                


                    
                      
                 
                 
            
                    
            
                           
                
    
