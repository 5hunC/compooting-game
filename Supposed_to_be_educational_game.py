import time
import random

ques = 0
luck = 0
dmg = 0
ppp = ["head", "hair", "left arm", "right arm", "face", "throat", "left foot", "right foot", "groin", "left middle toenail", "left tooth", "right tooth", "upper forehead", "chin", "middle chin", "high chin"]
yap = ["punch", "kick", "lick", "smell", "graze", "insult", "brag about", "stare at", "think about", "jump on"]
epic = ["accidentally pooped while trying to attack", "slipped on a random bannana peal while going over to attack", "got snipped by a burgan truck while going over to hit", "staggered over drunk while trying to hit"]
praygold = 25
sssspecial = 0
eee = 250
questions = ["What is part of the first line of defence?",
              "When a pathogen enters your body, what is one of the first cells to appear?",
                "Which immune cell is the most careless when attacking?",
                  "What does the thymus do?",
                    "What are cykotynes?",
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
                   "5. The comunication",
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
p = 1
var = 4
alive = True

print(answers[10])

def wait() :
      input("======== PRESS ENTER TO CONTINUE ========")
while alive:
  print("Score: " + str(p))
  print(f"Health: {eee}")
  action = input("What do you want to do? (casino, work, fight, pray): ")
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
    elif random.randint(1,100) == 3:
        print("You caught cancer and begin to try beat Stage 1 Cancer")
        ene = random.randint(9999,99999)       # SpEcIaL guard hp
        ssspecial = random.randint(20, 30)  # special guard damage increase
        print(f"SPECIAL CANCER POWER LEVEL: {round(((ene - 180)/3) + ssspecial)}")
        sssspecial = round(((ene - 180)/3) + ssspecial)
    elif random.randint(1,100) == 4:
      alive = False
      print("You died to slipping on a random banana peel... Better luck next time I guess...")
      break
    elif random.randint(1,10) == 5:
      print("An angle comes down and heals you for all your health before the fight!")
      eee += 250 - eee
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
      dmg = random.randint(10,40)
      if random.randint(1,10) == 1 :
        print(f"You {epic[random.randint(0,len(epic) - 1)]} damaging you for {dmg} instead!")
        eee -= dmg
      else :
        print(f"You {yap[random.randint(0,len(yap) - 1)]} their {ppp[random.randint(0,len(ppp) - 1)]} for {dmg} damage!")
        ene -= dmg
      dmg = random.randint(10 + sssspecial, 40 + sssspecial)
      print(f" Enemy HP: {ene} ===0=== Player HP: {eee}")
      if random.randint(1,10 - luck) == 1 :
        print(f"They {epic[random.randint(0,len(epic) - 1)]} damaging them for {dmg} instead!")
        ene -= dmg
      else :
        print(f"They {yap[random.randint(0,len(yap) - 1)]} your {ppp[random.randint(0,len(ppp) - 1)]} for {dmg} damage!")
        eee -= dmg
      print(f" Enemy HP: {ene} ===0=== Player HP: {eee}")
    if eee < 0.1 :
      alive = False
    else :
      print("YOU WON!")
      print("You stole some cash off their corpse")
      p += random.randint(2,36) + sssspecial
      print("Score: " + str(p))
  if action == "work":
    if eee < 250:
      eee += 100
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
                  print(f"Your points are now at {p}")
                  if p != 0:
                        print("Don't gamble your life away")
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
      else :
          print("You walk away.")
print("You died")
print("Score: " + str(p))
