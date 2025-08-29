f = open("fake_subregions.txt", "r")
f.readline()
for line in f:
    print(line)

#sub_region = sub_region.strip()

f = open("fake_subregions.txt", "r")
f.readline()
sub_region = f.readline().strip()
for line in f:
    line.strip()
    print(line)
#print(sub_region)
