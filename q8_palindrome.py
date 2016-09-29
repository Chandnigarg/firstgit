def fun_palindrome(string1):
    string3=""
    string4=""
    string2=string1[::-1]
    for i in string2:
        if (str(i)!=" "):
            string3=string3+str(i)

    for j in string1:
        if (str(j)!=" "):
            string4=string4+str(j)

            
    if(string3==string4):
        print(string1,"is palindrome")
    else:
        print("not a palindrome")


string1=str(input("enter string"))
fun_palindrome(string1)
