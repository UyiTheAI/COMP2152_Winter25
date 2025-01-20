import random
healthPoints = 10
mHealthPoints = 10
diceOptions = [1, 2, 3, 4, 5, 6]
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

int(input("Roll the dice for your combat strength (Press 1): "))
combatStrength = random.choice(diceOptions)
print("You rolled " + str(combatStrength) + " for your combat strength")

int(input("Roll the dice for the monster's combat strength (Press 1): "))
mCombatStrength = random.choice(diceOptions)
print("The monster rolled " + str(mCombatStrength) + " for its combat strength")

input("===Status Sheet=== (Press enter)")

# Equality operators
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

# Relational operators
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# or keyword
print("--- Things are getting dangerous: " + str(healthPoints == 1))

# in keyword
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 10:
    print("--- Your health is ok")
else:
    print("--- Your health is low at " + str(healthPoints))

weaponRoll = random.choice(diceOptions)
combatStrength += weaponRoll
weapon = weapons[weaponRoll - 1] 
print("\nYou rolled " + str(weaponRoll) + " for your weapon. Your weapon is: " + weapon)

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("Your weapon is meh")
else:
    print("Nice weapon, friend!")

if weapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

while healthPoints > 0 and mHealthPoints > 0:
    input("You meet the monster. FIGHT!! Press enter to continue.")

    input("You strike first (Press enter)")
    combatStrength = random.choice(diceOptions)
    print("Your " + weapon +"(" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")

    # Apply player's strike on the monster
    if combatStrength >= mHealthPoints:
        mHealthPoints = 0
        print("You've killed the monster")
        break
    else:
        mHealthPoints -= combatStrength
        print("You've reduced the monster's health to: " + str(mHealthPoints))

    # Monster strikes back
    input("MONSTER'S TURN!!! (Press enter to continue.)")
    mCombatStrength = random.choice(diceOptions)
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")

    # Apply monster's strike on the player
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
        break
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))

    print("\nNext round...\n")

if healthPoints <= 0:
    print("Game Over. The monster wins.")
else:
    print("Congratulations! You defeated the monster.")
