
c=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
z=[0,1,2,3,4,5,6,7,8]
print("the game boards numbers")
print("|",z[0],"|",z[1],"|",z[2],"|")
print("|",z[3],"|",z[4],"|",z[5],"|")
print("|",z[6],"|",z[7],"|",z[8],"|")

# set player to 1
player=1
odd=[1,3,5,7,9]
even=[0,2,4,6,8]
while True:
        while True:
            print("player",player)
            print("choose board number",z)
            x=int(input("name your board:"))
            if x in z:
                    while x in z:
                        z.remove(x)
                        if player==1:
                            print("choose numer",odd)
                            num=int(input("your number:"))
                            if num in odd:
                                odd.remove(num)
                                c.insert(x,num)
                                break
                            else:
                                print("error")
                                while True:
                                    print("player",player)
                                    print("choose number",odd)
                                    num=int(input("your number:"))
                                    if num in odd:
                                        odd.remove(num)
                                        c.insert(x,num)
                                        break
                        else:
                            print("choose number",even)
                            num=int(input("your number:"))
                            if num in even:
                                even.remove(num)
                                c.insert(x,num)
                                break
                            else:
                                print("error")
                                while True:
                                    print("player",player)
                                    print("choose number",even)
                                    num=int(input("your number:"))
                                    if num in even:
                                        even.remove(num)
                                        c.insert(x,num)
                                        break
                    break                    
            else:
                print("already taken")
        # check the wins
        if c[0]+c[1]+c[2]==15:
            print("player",player,"wins")
            break
        elif c[3]+c[4]+c[5]==15:
            print("player",player,"wins")
            break
        elif c[6]+c[7]+c[8]==15:
            print("player",player,"wins")
            break
        elif c[0]+c[3]+c[6]==15:
            print("player",player,"wins")
            break
        elif c[1]+c[4]+c[7]==15:
            print("player",player,"wins")
            break
        elif c[2]+c[5]+c[8]==15:
            print("player",player,"wins")
            break
        elif c[0]+c[4]+c[8]==15:
            print("player",player,"wins")
            break
        elif c[2]+c[1]+c[6]==15:
            print("player",player,"wins")
            break
        # switch players
        if player==1:
            player=2
        else:
            player=1
print("game over")
