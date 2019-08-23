import sys

def print_headlines():
    row_labels = ['Student','Name','Midterm','Final','Average','Grade']
    print("{0:^10}{1:>15}{2:^15}{3:^8}{4:^13}{5:^9}".format(*row_labels))
    print("-"*70)

def avrg_grade(m,f):
    avrg = (int(m)+int(f))/2

    if avrg // 10 == 9:
        grade = 'A'
    elif avrg // 10 == 8:
        grade = 'B'
    elif avrg // 10 == 7:
        grade = 'C'
    elif avrg // 10 == 6:
        grade = 'D'
    else:
        grade = 'F'
    return float(avrg), grade

# 내림차순 처리
def show():
    count = 0
    stu_list.sort(key=lambda e : e[4], reverse=True)
    print_headlines()
    for line in stu_list:
        print("{0:^10}{1:>15}{2:^15}{3:^8}{4:^13}{5:^9}".format(*line))
    print()

def search():
    studentID = input("Student ID:")
    isnall = False
    for line in stu_list:
        if line[0] == studentID:
            isnall = True
            print_headlines()
            print("{0:^10}{1:>15}{2:^15}{3:^8}{4:^13}{5:^9}\n".format(*line))
            break
    if not isnall :
        print("NO SUCH PERSON.\n")

def changescore():
    studentID = input("Student ID:")
    isnall = False

    for line in stu_list:
        if line[0] == studentID:
            isnall = True
            newsc = -1
            term = input("Mid/Final?").lower()

            if (term =='mid') or (term =="final"):
                newsc = int(input("Input new score:"))

                if newsc >= 0 and newsc <= 100:
                    print_headlines()
                    print("{0:^10}{1:>15}{2:^15}{3:^8}{4:^13}{5:^9}".format(*line))
                    print("Score changed.")

                    if term == "mid":
                        line[2] = newsc   
                    else : 
                        line[3] = newsc
                    line[4], line[5] = avrg_grade(line[2],line[3])
                    print("{0:^10}{1:>15}{2:^15}{3:^8}{4:^13}{5:^9}\n".format(*line))
    if not isnall :
        print("NO SUCH PERSON.\n")

def searchgrade():
    grade = input("Grade to search:")

    if grade in ['A','B','C','D','F']:
        l = []
        for line in stu_list:
            if line[5] == grade:
                l.append(line)
        if l :
            print_headlines()
            for i in l:
                print("{0:^10}{1:>15}{2:^15}{3:^8}{4:^13}{5:^9}".format(*i))
        else :
            print("NO RESULTS.\n")

def add():
    newID = input("Student ID:")
    isnall = False
    for line in stu_list:
        if line[0] == newID:
            print("ALREADY EXISTS.\n")
            isnall = True
            break

    if not isnall :    
        name = input("Name:")
        midscore = input("Midterm Score:")
        finalscore = input("Final Score:")
        avr, grade =  avrg_grade(midscore, finalscore)
        stu_list.append([newID,name, midscore, finalscore, avr, grade])
        print("Student added.\n")

def remove():
    if not stu_list:
        print("List is empty.\n")
    else :
        isnall = False
        studentID = input("Student ID:")
        cnt = 0
        for line in stu_list:
            if line[0] == studentID:
                isnall = True
                del stu_list[cnt]
                print("Student removed.")
                break
            cnt += 1
            
        if not isnall :
            print("NO SUCH PERSON.\n")

def quit():
    savedata = input("Save data?[yes/no]")
    if savedata == 'yes':
        stu_list.sort(key=lambda e : e[4], reverse = True)
        filename = input("File name:")
        f_write = open(filename,'w')
                      
        for line in stu_list:
            f_write.write("{0}\t{1}\t{2}\t{3}\n".format(*line))

        f_write.close()

args = sys.argv # 리스트 형태

if len(args) == 1:
    f = open("students.txt","r")
else :
    f = open(args[1],"r")      
data =f.read() 

stu_list = []
count = 0
lines = data.split("\n")
f.seek(0)

for line in f:
    stu_list.append(lines[count].split("\t"))
    avrg, grade = avrg_grade(stu_list[count][2], stu_list[count][3])

    stu_list[count].append(avrg)
    stu_list[count].append(grade)
    stu_list.sort(key=lambda e : e[4], reverse = True)
    count += 1

show()

while True:
    command = input("\n#").lower()
    
    if command == 'show':
        show()

    elif command == 'search':
        search()

    elif command == 'changescore':
        changescore()

    elif command == 'searchgrade':
        searchgrade()

    elif command == 'add':
        add()

    elif command == 'remove':
        remove()

    elif command == 'quit':
        quit()
        break
        
    else :
        continue