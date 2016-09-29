import re,sys
def fun_sen_splitter(string1):
    ff=open("C:\python codes\q-42file.txt","w+")
    ff.write("bbbbbbb\n");
    for i in string1:
        if re.match(r"[.?!]",i):
            
            ff.write("  HHHH   ");

            obj = re.search(r"[.?!]+",i ).group()
            pos = i.find(obj)
            pos = pos+len(obj)-1
            
            string2=string1[pos+1::]
            if str(re.match(r" [a-z]",string2)):
                ff.write(i)
                ff.write("  11111   ");
            
            elif re.match(r"[0-9]+",string2):
               ff.write("\n",i);
               
               ff.write("  3333  ");     
            elif():
                ff.write(i)

            elif(re.match(r"[a-zA-Z]",string2))and(re.match(r"[a-zA-Z]",string1[pos-1:])):
                ff.write(i)

            elif(re.match(r"[,/:;\"'\\/*]",string2)):
                ff.write(i)

            else:
                 ff.write("  2222   ");
                 ff.write("\n", i);
   
        else:
            ff.write(i)


string1=str(input("enter the string"))

fun_sen_splitter(string1)
                 

                 
