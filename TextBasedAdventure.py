import os

print("Hello lone traveler! the strange bartender says..")

print("""
1. say hello
2. ignore him
""")

answer1 = input(">")

if answer1 == "1":
    print("""ah, finally a traveler that doesnt ignore me! I have a quest for you,
  Do you accept?
  1. yes
  2. no""")

if answer1 == "2":
    print("well alright then, I guess you dont want to slay a dragon..")

questacceptornot = input(">")

if questacceptornot == "2":
    print("well okay goodbye then")
    play_again()

if questacceptornot == "1":
    print("""well, let me tell you a story.
  a long, long time ago, someone found an egg, it was bigger then normal, no one knew what it was.. 

  but in casual human nature, they thought about eating it,
  so, they went to the middle of the village, made a big fire, and placed the egg on the fire.


  but what they didnt expect was that it was a dragon, a fiery blazing hot dragon. 
  it hatched in the middle of the night houses burnt to ash, thousands of trees were gone.

  now the dragon rests in his lair, with all the gold and diamond he could gather.


  """)

print("type ok to continue")

isoktypedclicked = input(">")

if isoktypedclicked == "ok":
    os.system('clear')

    print("""Now, I will give you a map. but for that, I get 20% of the gold and diamonds, you get the rest. 

  alright?

  1. Agree
  2. try to lower it""")

quest20percentquestion = input(">")

if quest20percentquestion == "1":
    print("""alright traveller! good luck!

    Where do you want to go? left or right?
    1. left
    2. right""")

leftorright = input(">")

if leftorright == "2":
    print("placeholder")

    if leftorright == "1":
        print("""you met a troll and died!

  want to play again?
  """)

if quest20percentquestion == "2":
    print("well then, I will not help you, goodbye")


    def play_again():
        print("placeholder")
