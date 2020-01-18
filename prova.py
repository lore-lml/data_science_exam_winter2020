import re
text = "..ciao ..lo *come *****ahsahha ..akjsldklas . .. *** come..come -cici ahah-chch a++++"
#print(re.sub(r"([\\*\\.\-/])+[.]*", r"\0", text))
print(re.sub("([*.\-/+])", " ", text))