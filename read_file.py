f = open("save_game.txt","r")
text = f.read()
users = eval(text)
f.close
print users
