import sys

f = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "w")

for line in f:
    f2.write(line)
    
f.close()
f2.close()

# args = sys.argv # 리스트 형태

# for i in args:
#     print(i)