#!/usr/bin/env python
# coding: utf-8

# In[108]:


import random
import time
print('''Welcome to Battle
Enemy is Randomly chosen
Buff adds damage, Heal will add 5 - 20 HP
\n''')

wins = 0

def choose():
    global wins
    wins = 0
    fighter = 0
    
    print("Fighter 1: ❤️ = 100, ⚔️ = 20")
    print("Fighter 2: ❤️ = 80,  ⚔️ = 25")
    print("Fighter 3: ❤️ = 120, ⚔️ = 15")
    choice = int(input("Select a fighter: "))

    if choice == 1:
        fighter += 1
    elif choice == 2:
        fighter += 2
    elif choice == 3:
        fighter += 3
        
    fighter_select(fighter)
    
def fighter_select(fighter_choice):
    player_hp = 0
    player_damage = 0
    
    enemy_hp = 0
    enemy_damage = 0
    
    if fighter_choice == 1:
        player_hp = 100
        player_damage = 20
    elif fighter_choice == 2:
        player_hp = 80
        player_damage = 25
    elif fighter_choice == 3:
        player_hp = 120
        player_damage = 15
    
    #Use if you want enemy to be a random fighter
    #enemy = random.randint(1, 3)
    #if enemy == 1:
        #enemy_hp = 100
        #enemy_damage = 20
    #elif enemy == 2:
        #enemy_hp = 80
        #enemy_damage = 25
    #elif enemy == 3:
        #enemy_hp = 120
        #enemy_damage = 15
        
    enemy_hp = random.randint(75, 150)
    enemy_damage = random.randint(12, 30)
        
    begin_battle(player_hp, player_damage, enemy_hp, enemy_damage)
    
    
def begin_battle(playerHP, playerDMG, enemyHP, enemyDMG):
    global wins
    turn = 1
    
    print("\nYour Stats: ❤️ =", round(playerHP, 2), "⚔️ =", round(playerDMG, 2))
    print("Your Enemy: ❤️ =", enemyHP, "⚔️ =", round(enemyDMG, 2))
    
    while playerHP > 0 and enemyHP > 0:
        print("TURN:", turn)
        move = input("\nWill you heal, attack or buff? (h / a / b): ")
        dodge = random.randint(0,4)
        
        print("------------")
        if move == "h":
            healP = random.randint(5, 20)
            playerHP += healP
            print("Player Heal by", healP, "HP")
        if move == "b":
            playerDMG = playerDMG * 1.2
            print("Player Buff")
        if move == "a" and dodge > 0:
            enemyHP -= playerDMG
            print("Player Attack")
        if move == "a" and dodge == 0:
            print("Player Miss")
        if move == "e":
            break
        if enemyHP <= 0:
            print("------------")
            break
            
        enemy_move = random.randint(-1,2)
        if enemy_move == -1:
            enemyDMG = enemyDMG * 1.2
            print("Enemy Buff")
        if enemy_move == 0:
            healE = random.randint(10, 20)
            enemyHP += healE
            print("Enemy Heal by", healE, "HP")
        if enemy_move > 0 and dodge != 1:
            playerHP -= enemyDMG
            print("Enemy Attack")
        elif enemy_move > 0 and dodge == 1:
            print("Enemy Miss")
        print("------------")
        
        print("\nYour Stats: ❤️ =", round(playerHP, 2), "⚔️ =", round(playerDMG, 2))
        print("Your Enemy: ❤️ =", round(enemyHP, 2), "⚔️ =", round(enemyDMG, 2), end = "\n\n")
        
        turn = turn + 1
    
    
    if playerHP > enemyHP:
        if enemyHP < 0:
            enemyHP = 0
        print("\nCongrats you won")
        print("\nYour Stats: ❤️ =", round(playerHP, 2), "⚔️ =", round(playerDMG, 2))
        print("Your Enemy: ❤️ =", round(enemyHP, 2), "⚔️ =", round(enemyDMG, 2), end = "\n\n")
        
        wins = wins + 1
        print("WINS:", wins)
        again = input("Keep Fighting? (y / n): ")
        if again == "y":
            new_battle(playerHP, playerDMG)
        if again == "n":
            print("You won", wins, "times")
            time.sleep(500)
            
    elif enemyHP > playerHP:
        if playerHP < 0:
            playerHP = 0
        print("\nSorry you Lost")
        print("\nYour Stats: ❤️ =", round(playerHP, 2), "⚔️ =", round(playerDMG, 2))
        print("Your Enemy: ❤️ =", round(enemyHP, 2), "⚔️ =", round(enemyDMG, 2), end = "\n\n")
        print("WINS:", wins)
        again = input("Keep Fighting? (y / n): ")
        if again == "y":
            choose()
        if again == "n":
            print("You won", wins, "times")
            time.sleep(500)
        
def new_battle(hp, dmg):
    enemy_hp = random.randint(75, 150)
    enemy_damage = random.randint(12, 30)
        
    begin_battle(hp, dmg, enemy_hp, enemy_damage)
    
choose()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




