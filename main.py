print('''
################
## Carrotland ##
################
''')
print("")
print(".:PLAY:.\n")
print(".:EXIT:.\n")
main_title = input("> ")
if main_title == "play" or "PLAY" or "Play":
	print("I see we have a newcomer. What is your name?")
	name = input("> ")
	print("Welcome, " + name + "!")
	print("You are in a land full of carrots. You can go left or right. Which way do you go? (left/right)")
	x = input("> ")
	if x == "left":
		print("You are now in a large carrot field. You are extremely hungry. Will you eat them, or risk starvation? (eat/risk)")
		y = input("> ")
		if y == "eat":
			print("Uh oh. Those carrots were poisonous.")
			print("You lose.")
		elif y == "risk":
			print("Thankfully, you didn't eat those carrots. They were poisonous!")
			print("You win!")
	elif x == "right":
		print("You find an evil 1,000 foot tall farmer who is farming carrots. What do you do? (run/hide)")
		farmer = input("> ")
		if farmer == "run":
			print("With a farmer that big, you are no match.")
			print("You lose.")
		elif farmer == "hide":
			print("You successfully hide from the farmer.")
			print("You win!")
elif main_title == "EXIT" or "exit" or "Exit":
	print("Bye bye!\n")
	exit()