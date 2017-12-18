min_GPA = 3.5
min_SAT = 1300
min_asvab = 90

f=open("data.csv",'r')
count = 0.0
lineCount = 0
for line in f:
    lineCount+=1
    line = line.strip().split(',')
    name = line[0]
    gpa=float(line[1])
    sat=float(line[2])
    asvab=float(line[3])
    if gpa>=min_GPA and sat>=min_SAT and asvab >= min_asvab:
        count += 1.0

print "acceptance rate:",100*count/lineCount,"%"
