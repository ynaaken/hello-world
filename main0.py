f = open('e-mails.txt', 'r')
string_mail = f.read()
f.close()
print(string_mail)



my_file = open("some.txt", "w")
my_file.write("Мне нравится Python!\nЭто классный язык!")
my_file.close()