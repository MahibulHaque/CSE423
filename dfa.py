def validEmailAddress(s):
    state = 0
    email = False
    i=0
    while(i<len(s)):
        match state:
            case 0:
                if(ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                    state = 1
                else:
                    state = 6
                i+=1

            case 1:
                if(s[i]=='@'):
                    state=2
                elif(ord(s[i])>=65 and ord(s[i])<=90)or(ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57):
                    state = 1
                else:
                    state=6
                i+=1

            case 2:
                if(ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                    state = 3
                else:
                    state = 6
                i+=1

            case 3:
                if(s[i]=='.'):
                    state = 4
                elif(ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                    state=3
                else:
                    state=6
                i+=1

            case 4:
                if(ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                    state=5
                    email = True
                    print("yes")
                else:
                    state=6
                i+=1

            case 5:
                if(ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
                    state=5
                elif(s[i]=='.'):
                    state=4
                else:
                    state=6
                i+=1

            case 6:
                email = False
                if(s[i]):
                    state = 6
                i+=1

    return email

print(validEmailAddress("abc@g.bracu.ac.bd"))