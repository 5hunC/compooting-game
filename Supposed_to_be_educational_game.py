import time
import random

ques = 0
luck = 0
dmg = 1
yourdmg = 1
ppp = ["head", "hair", "left arm", "right arm", "face", "throat", "left foot", "right foot", "groin", "left middle toenail", "left tooth", "right tooth", "upper forehead", "chin", "middle chin", "high chin"]
yap = ["punch", "kick", "lick", "smell", "graze", "insult", "brag about", "stare at", "think about", "jump on"]
epic = ["accidentally pooped while trying to attack", "slipped on a random bannana peel while going over to attack", "got snipped by a burgan truck while going over to hit", "staggered over drunk while trying to hit"]
praygold = 25
sssspecial = 0
eee = 250
questions = ["What is part of the first line of defence?",
              "When a pathogen enters your body, what is one of the first cells to appear?",
                "Which immune cell is the most careless when attacking?",
                  "What does the thymus do?",
                    "What are cytokines?",
                     "What part of the immune system are T cells part of?",
                      "What do Helper T cells activate?",
                        "What do pyrogens do?",
                         "Which immune cells attack cancer/infected cells?",
                          "In percentage, how many T cells make it out of their training?",
                            "What is cancer?"]
questions_left = questions
answers = ["1. The skin",
             "2. macrophages",
               "3. Neutrophil",
                 "4. Trains the T cells",
                   "5. The communication",
                     "6. The adaptive immune system",
                       "7. B cells",
                         "8. They get picked up by the brain and activate fevers",
                           "9. Killer T cells & Natural Killer cells",
                             "10. 2%",
                               "11. A corrupted/mutated cell from your own body"]
sssspecial = 0
answersleft = answers
display = []
ara = ["A", "B", "C", "D"]
replyans = 0
p = 0
var = 4
alive = True

print(answers[10])

def wait() :
      input("======== PRESS ENTER TO CONTINUE ========")
while alive:
  print("Score: " + str(p))
  print(f"Health: {eee}")
  action = input("What do you want to do? (casino, work, fight, pray, stats, end_run, admin_abuse, Reset, ERASE, SAVE): ")
  if action == "SAVE":
    yourdmg == 999999999999999999999999999999999999999999999999999999999999
    print("You are filled with HATRED")
    wait()
  if action == "ERASE":
    ERASE = input("Are you sure you want to ERASE this timeline?... (Do it/Don't do it): ")
    if ERASE == "Do it":
      print("Chara: You know what we have to do now...")
      wait()
      print("Chara: Partner?...")
      wait()
      print("Chara: It was fun while it lasted...")
      wait()
      print("Chara: HAHAHAHA, AHAHA")
      wait()
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      alive = False
      break
    elif ERASE == "Don't do it":
      print("Chara: Since when... Were YOU the one in control?...")
      wait()
      print("Chara: HAHAHAHA, AHAHA")
      wait()
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      alive = False
      break
    elif ERASE == "ERASE":
      print("Chara: That's more like it!")
      wait()
      print("Both: HAHAHAHA, AHAHA")
      wait()
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      alive = False
      break
    else:
      print("Chara: You really ARE an IDIOT!")
      wait()
      print("Chara: HAHAHAHA, AHAHA")
      wait()
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
      alive = False
      break
  if action == "Reset":
    Reset = input("Are you sure you want to Reset this timeline? (Do it/Don't do it): ")
    if Reset == "Do it":
      print("Chara: There is no turning back now...")
      p = 0
      luck = 0
      eee = 250
      yourdmg = 1
      wait()
      print("You have been reset...")
      wait()
    elif Reset == "Don't do it":
      print("You close the Reset button...")
      wait()
    else:
      print("That's not an option")
      wait()
  if action == "FIGHT":
    print("The great undyne spawns...")
    ene = random.randint(250,500)       # SpEcIaL guard hp
    ssspecial = random.randint(20, 30)  # special guard damage increase
    print(f"UNDYNE POWER LEVEL: {round(((ene - 180)/3) + ssspecial)}")
    sssspecial = round(((ene - 180)/3) + ssspecial)
    wait()
    while ene > 0 and eee > 0 :
      dmg = random.randint(10,40 - luck)
      if random.randint(1,10) == 1 :
        print(f"You {epic[random.randint(0,len(epic) - 1)]} damaging you for {yourdmg} instead!")
        eee -= yourdmg
      else :
        print(f"You {yap[random.randint(0,len(yap) - 1)]} their {ppp[random.randint(0,len(ppp) - 1)]} for {yourdmg} damage!")
        ene -= yourdmg
        dmg = random.randint(10 + sssspecial, 40 + sssspecial)
        print(f" Enemy HP: {ene} ===0=== Player HP: {eee}")
      if random.randint(1,10 - luck) == 1 :
        print(f"They {epic[random.randint(0,len(epic) - 1)]} damaging them for {dmg} instead!")
        ene -= dmg
      else :
        print(f"They {yap[random.randint(0,len(yap) - 1)]} your {ppp[random.randint(0,len(ppp) - 1)]} for {dmg} damage!")
        eee -= dmg
        print(f" Enemy HP: {ene} ===0=== Player HP: {eee}")
        wait()
      if eee < 0.1 :
        alive = False
      else :
        print("YOU WON!")
        print("You stole some cash off their corpse")
        wait()
        p += random.randint(2,36) + sssspecial
  if action == "admin_abuse":
    print("By the way, there is a 1 in 50 chance to imediatly die due to admin abusing...")
    wait()
    print("Getting your admin powers ready...")
    wait()
    secondary_action = input("What would you like to use? (Too_much_hp, Too_lucky, Too_many_points, cancel): ")
    print()
    if secondary_action == "Too_much_hp":
      print("Loading hp...")
      if random.randint(1,50 + luck) == 6:
        print("You died to admin abusing")
        alive = False
        break
      wait()
      eee += 99999999
      print("added 99999999 to your hp")
      wait()
    elif secondary_action == "Too_lucky":
      if random.randint(1,50 + luck) == 7:
        print("You died to admin abusing")
        alive = False
        break
      luck = 9
      print("You now have been blessed by the gods with lots of luck")
      wait()
    elif secondary_action == "Too_many_points":
      if random.randint(1,50 + luck) == 8:
        print("You died to admin abusing")
        alive = False
        break
      p += 10000000
      print("10000000 has been added to Your points")
      wait()
    elif secondary_action == "cancel":
      wait()
      print("Canceling action...")
      wait()
      print("Action canceled")
      wait()
    else:
      print("That's not an option")
      wait()
  if action == "end_run":
      proceed = input("Are you sure you want to continue? (yes/no): ") # gives you as second chance
      if proceed == "yes":
        alive = False
        print("Ending run...")
        wait()
      elif proceed == "no":
          print("Good choice")
          wait()
      else:
         print("That is not an option")
         wait()
  if action == "stats":
     print("luck:", luck)
  if action == "fight":
    if random.randint(1,5) == 1:          # chance to fight special guard
      print("You walk up to the guard... but you feel like something is off...")
      ene = random.randint(180,225)       # SpEcIaL guard hp
      ssspecial = random.randint(20, 30)  # special guard damage increase
      print(f"SPECIAL GUARD POWER LEVEL: {round(((ene - 180)/3) + ssspecial)}")
      sssspecial = round(((ene - 180)/3) + ssspecial)
    elif random.randint(1,5) == 2:
        ene = random.randint(75,175)
        print("You walk up to the guard... but you feel as if something else is watching you...")
        luck -= 1
        ssspecial = 0
        sssspecial = 0
        ene = random.randint(75,175)
    elif random.randint(1,20 + luck) == 3:
        print("...")
        wait()
        print("You begin to try beat Stage 1 Cancer")
        ene = random.randint(9999,99999)       # SpEcIaL guard hp
        ssspecial = random.randint(20, 30)  # special guard damage increase
        print(f"SPECIAL CANCER POWER LEVEL: {round(((ene - 180)/3) + ssspecial)}")
        sssspecial = round(((ene - 180)/3) + ssspecial)
    elif random.randint(1,50 + luck) == 4:
      alive = False
      print("You died to slipping on a random banana peel while walking up to the guard... Better luck next time I guess...")
      break
    elif random.randint(1,10) == 5:
      print("An angle comes down and heals you for 250 hp before the fight!")
      eee += 250
      wait()
      print("You walk up to the guard and start to fight them.")
    else :
      ene = random.randint(80,180) # Regular guard hp
      print("You walk up to the guard and start to fight them.")
      ssspecial = 0 # Regular guard damage increase
      sssspecial = 0
    ene = random.randint(80,180)
    wait()
      while ene > 0 and eee > 0 :
        dmg = random.randint(10,40 - luck)
      if random.randint(1,10) == 1 :
        print(f"You {epic[random.randint(0,len(epic) - 1)]} damaging you for {yourdmg} instead!")
        eee -= yourdmg
      else :
        print(f"You {yap[random.randint(0,len(yap) - 1)]} their {ppp[random.randint(0,len(ppp) - 1)]} for {yourdmg} damage!")
        ene -= yourdmg
        dmg = random.randint(10 + sssspecial, 40 + sssspecial)
        print(f" Enemy HP: {ene} ===0=== Player HP: {eee}")
      if random.randint(1,10 - luck) == 1 :
        print(f"They {epic[random.randint(0,len(epic) - 1)]} damaging them for {dmg} instead!")
        ene -= dmg
      else :
        print(f"They {yap[random.randint(0,len(yap) - 1)]} your {ppp[random.randint(0,len(ppp) - 1)]} for {dmg} damage!")
        eee -= dmg
        print(f" Enemy HP: {ene} ===0=== Player HP: {eee}")
        wait()
      if eee < 0.1 :
        alive = False
      else :
        print("YOU WON!")
        print("You stole some cash off their corpse")
        wait()
        p += random.randint(2,36) + sssspecial
  if action == "work":
    print("To answer the questions, type the number next to the answer that you think is correct.")
    wait()
    if eee < 250:
      eee += 125
    for i in range(5):
          var = 4
          replyans = random.randint(1,4)
          answersleft = answers
          print(f"Question {i+1}:")
          selectedq = random.randint(0, len(answersleft) - 1)
          chosen_question = questions[selectedq]
          chosen_answer = answersleft[selectedq]
          print(chosen_question)
          wait()
          for x in answers :
                print(x)
          reply = input("Answer: ")
          if int(reply) == int(selectedq + 1):
            print("CORRECT")
            p += 10
            print("Score: " + str(p))
          else:
            print("INCORRECT")
            print("Score: " + str(p))
          wait()
  if action == "casino" :
    if p == 0:
      wait()
      print("You go up to the casino but your too broke to pay the entry fee so the guard shoots you.")
      alive = False
    if alive:
      gamble = input("Gamble? (yes/no): ")
      while gamble == "yes":
            gamble = input(f"CHOOSE YOUR STAKE (you have {p} points):")
            gamble = int(gamble)
            if int(gamble) > p :
                  print("BROKE POTATO, YOU CAN'T GAMBLE THAT MUCH")
            else:
                  for i in range(random.randint(40,100)):
                        print(f"|| {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} ||")
                        time.sleep(0.01)
                  for i in range(random.randint(10,30)):
                        print(f"|| {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} ||")
                        time.sleep(0.04)
                  for i in range(random.randint(10,30)):
                        print(f"|| {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} ||")
                        time.sleep(0.10)
                  for i in range(random.randint(10,30)):
                        print(f"|| {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} ||")
                        time.sleep(0.2)
                  for i in range(random.randint(2,3)):
                        print(f"|| {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} ||")
                        time.sleep(0.4)
                  for i in range(random.randint(1,3)):
                        print(f"|| {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} || {p + gamble*random.randint(-1,1)} ||")
                        time.sleep(0.6)
                  win = gamble*random.randint(-1,1)
                  p += win
                  if eee < 250:
                    eee += win + 5
                    wait()
                  print(f"Your points are now at {p}")
                  wait()
                  if p != 0:
                        print("Don't gamble your life away")
                        wait()
                        gamble = input("Gamble? (yes/no): ")
  if action == "pray" :
    if p == 0:
      print("You walk up to the shrine of ASGORE to pray, but get run over by a burgan truck because you are too broke")
      alive = False
    if alive:
      print("You walk up to the shrine of ASGORE to pray.")
      pray = input(f"Pray with {praygold}/{p} points? (yes/no): ")
      if pray == "yes" and p > praygold :
          print(f"You pray with {praygold} points.")
          p -= praygold
          praygold = round(praygold * 1.4)
          if luck < 5 :
            luck += 1
          if luck == 5 :
            wait()
            print("You have maximum luck")
      else :
          print("You walk away.")
print("You died")
print("Score: " + str(p))
