#declare a list of colors
l=["blue","yellow","red","orange","rose"]
#add a new color 'yellow' on the list
l.append("violet")
#change the second color in the block
l[1]="white"
#print the updated list
print(l)
#print the second last color
print(l[-2])
#print the number of color
print(len(l))
#print the reverse list
print(l[::-1])
