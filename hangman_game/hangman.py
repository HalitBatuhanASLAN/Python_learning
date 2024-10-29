secret_word = "fenerbahce"#size is 10
guessed_word = ""
index = 0
rights = 10
flag = 0
while rights > 0:
	flag = 0
	for character in secret_word:
		if character in guessed_word:
			print(character)
		else:
			print("|")
			flag = 1
	if flag == 0:
		print("You won congrts")
		break

	letter = input("Enter a letter : ")
	if letter not in secret_word:
		if rights == 0:
			print("You died. Next time maybe:)")
			break
		rights -= 1
		print(f"Wrong guess. You have {rights} more turns")
	else:
		guessed_word += letter