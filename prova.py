import re
text = "..ciao ..lo *come *****ahsahha ..akjsldklas . .. *** come..come -cici ahah-chch"
#print(re.sub(r"([\\*\\.\-/])+[.]*", r"\0", text))
print(re.sub("([*.\-/])", " ", text))