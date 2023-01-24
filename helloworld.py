import json

str1 = "Hello I'm Habba Dobba \nCan you hear me?"
print(str1)

input("[Yes?]")

good=("Good.")
print(good)

answer1=input("What is your name?")

str2="Ok "+answer1+", let me explain..."
print(str2)

str3="Were pretty sure you're a human. \nYou crash landed on our planet. \nYou were knocked out for three months, \nso everybody knows about you."
print(str3)

str4="We saved you from the Bigot."
print(str4)

input("[Whats the Biggot?]")

print("The Bigot is a big harry monster with huge spikes on it's back,\nand two big horns on it's head.")

d={
   "name": answer1, 
}

f=open("cp1.json", "w")
save=json.dumps(d, indent=4)
f.write(save)
f.close()

str5=("Game saved.")
print(str5)
