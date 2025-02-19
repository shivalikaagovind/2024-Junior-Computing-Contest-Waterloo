#Problem 1
R=int(input("Number of red plates:"))
G=int(input("Number of green plates:"))
B=int(input("Number of blue plates:"))

C=(R*3)+(G*4)+(B*5)
print(C) 

#Problem 2
D=int(input("Dusa's starting size:"))
current_dusa=D
while True: 
    next_yobi=int(input("Size of next Yobi:"))
    if current_dusa>next_yobi: 
        current_dusa+=next_yobi 
    else: 
        print(current_dusa)
        break

#Problem 3
N=int(input("Number of participants:"))
gold=0
silver=0
bronze=0
scores=[]
for i in range(N):
    score=int(input("score:"))
    scores.append(score)
gold=max(scores)
scores.remove(gold)
silver=max(scores)
scores.remove(silver)
bronze=max(scores)
print(bronze)

#Problem 4 
typed=input("type the phrase")
display=input("what is displayed?")

typed_list=list(typed)
display_list=list(display)
length=len(typed_list)
new=0
if len(typed_list)!=len(display_list): 
    new=len(typed_list)-len(display_list)
    for i in range(new):
        display_list.append(' ')
print(display_list)
letter=''
wrong_letter=''
quiet_letter='-'
for i in range(length):
    if typed_list[i]!=display_list[i]:
        if display_list[i]==' ':
            quiet_letter=typed_list[i]
        else:
            letter=typed_list[i]
            wrong_letter=display_list[i]
print(letter, wrong_letter)
print(quiet_letter)
