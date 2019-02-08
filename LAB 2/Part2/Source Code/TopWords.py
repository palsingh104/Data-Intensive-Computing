def read(input,list):
    inp = open(input, "r");

    confirm = False
    for line in inp.readlines():
        linesp = line.split()
        word = linesp[0]
        word = word[1:len(word)-1]
        value = int(linesp[1])
        x = (word,value)
	list.append(x)
		


list = []
read("part-00000",list)
out = open("TopSorted", "w");
jout = open("Top50", "w");
j = sorted(list,key=lambda a:a[1])
j.reverse()
i = int(0)
k = j[0:19]
l = j[0:49]
for x in j:	
  print(x)
  out.write(str(x[0]))
  out.write("\t")
  out.write(str(x[1]))
  out.write("\n")
for x in l:	
  jout.write(str(x[0]))
  jout.write("\t")
  jout.write(str(x[1]))
  jout.write("\n")        