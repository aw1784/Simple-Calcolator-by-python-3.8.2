num= input  ("enter your 1st number ")
result =num


while (float (num)!=0):
    y = input()
    #summation
    if (y== "+") :
     
     num=input("Enter the next number: ") 
    
     result =float (result)+float (num)

     print ("the result now is " + str (result))  

    #substraction 
    elif (y== "-") :
     
     num= input ("Enter the next number: ")
     
     result=float(result)- float(num)
      
     print ("the result now is " + str (result))
     
    #multiblling
    elif (y=="*"):
     num= input ("Enter the next number: ")
       
     result =float(num)*float(result)
     print ("the result now is " + str (result))
     
    #Division
    elif (y=="/"):
        num= input ("Enter the next number: ")
       
        result =float(result)/float(num)
        print ("the result now is " + str (result)) 
         
    elif y=="^":
        base=input("Enter the base of the power operation ") 
        power=input("Enter the power ")   
        num=pow(float(base),float(power))
        y= input("Enter the operation ")
        if y=="+":
           result =float (result)+float (num)

           print ("the result now is " + str (result)) 
        elif y=="-":
            diffence=float(result)- float(num)
            result = diffence
            print ("the result now is " + str (result))


        elif y=="*":
            result =float(num)*float(result)
            print ("the result now is " + str (result))
             
        elif y=="/":
            result =float(result)/float(num)
            print ("the result now is " + str (result))
             
        else:
            print("Enter the operation (+,-,*,/)")      
        

    elif (y=="=") :
        break
    else:
        print ("Please enter +,-,*,/")
print ("the result now is " + str (result))

    










     
     

