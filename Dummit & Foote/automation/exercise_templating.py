chapter = 10
section = 5
exercises = 28

out = ""
for i in range(exercises):
    out+="\\begin{problem}\\label{ex:"+str(chapter)+"."+str(section)+"."+str(i+1)+"}"
    out+="\n\n"
    out+="\\end{problem}\n\\begin{solution}\n\n\\end{solution}"
    out+="\n\n\n\n"
print(out)
