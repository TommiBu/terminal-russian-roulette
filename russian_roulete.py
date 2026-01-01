import random
import time
import os

def vycistit_obrazovku():
	os.system('cls' if os.name == 'nt' else 'clear')

# INTRO
vycistit_obrazovku()
print("=========================================")
print("     R U S S I A N  R O U L E T T E      ")
print("    (Terminal edition for the brave)     ")
print("=========================================")
print(r"""
	+--^-----------,--------,-----,--------^-,
	| ||||||||||   '--------'     |          O
	'+----------------------------^----------|
	 '\_,---------,---------,----------------,
	    / XXXXXX /'|      /'
	   / XXXXXX /  '\    /'
      / XXXXXX /'-------'
	 / XXXXXX /
	/ XXXXXX /
   (_________)
""")

print("\nRules: 6 Chambers, 1 Bullet.")
print("Take turns at the keyboard")

input("\nPress ENTER to play")

# GAME SETUP
bullet_position = random.randint(1, 6)
actual_chamber = 1
player = 1

# GAME LOOP
while True:
	vycistit_obrazovku()
	print(f"\n--- IT IS PLAYER NUMBER {player} TURN! ---")
	print(f"The revolever is ready. Actual chamber: {actual_chamber}.")
	print("-----------------------------")

	# STRATEGIES
	if actual_chamber < 6:
		answer = input("Do you want to spin the cylinder? (Yes/No): ")

		if answer == "Yes" or answer == "Y":
			print("\n*The sound of spinning cylinder*")
			time.sleep(1)
			print("The cylinder came to stop...")
			bullet_position = random.randint(1, 6)
			actual_chamber = 1
			print(f"The odds are again 1 in 6! Actual chamber: {actual_chamber}.")
		else:
			print("\nA bold choice! The tension rises...")

	# --- SHOOTING ---
	input(f"\nPlayer {player}, Your turn. Pull the trigger (ENTER)")

	print("\nPutting the gun to your head...")
	time.sleep(1)
	print("Finger pulls the trigger...")
	time.sleep(1.5)
	print("...")
	time.sleep(1)

	# --- EVALUATION ---
	if actual_chamber == bullet_position:
		print("\n=====================")
		print("      B A N G !      ")
		print("=====================")
		print(f"\nLuck run out player number {player}")
		break
	else:
		print("\nCLICK")
		print("...")
		print("Lucky. It was empty.")
		time.sleep(2)

		actual_chamber = actual_chamber + 1

		if player == 1:
			player = 2
		else:
			player = 1

		if actual_chamber > 6:
			print("\nSomething goes  wrong in the Metrix")
			break

print("\nGame over")

