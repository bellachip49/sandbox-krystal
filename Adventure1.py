# Krystal Kwan
# Choose Your Own Adventure
# 11/10/2018
print("The New Agent by Krystal Kwan. Enter q to quit.")
def answer():
  answer = input("> ")
  return answer
try:
    while answer != "q":
        print ("You are standing at the doors of a building, resembling a post office, but you when you look through the windows on each side of the doors, something seems strange. Enter?(y/n)")
        answer = answer()
        if answer == "y":
          print("You realize that the door has an old, rusty lock. Do you attempt to pull the door open nonetheless?(y/n)")
          answer = answer()
          if answer == "y":
            print("You continuously shake the doors, until the lock breaks open. They fall on the floor, causing dust to fly. You slowly open the doors and as you open them, and the lights in the room gradually brighten up. It appears to be a completely new work office of sorts, even though the outside look seemed misleading. A large TV on a wall on the opposite side of where you are standing. You approach the TV.Turn the TV on?(y/n)")
            answer = answer()
            if answer == "y":
              print("You turn on the TV. It turns on, and you see a mysterious dark figure appear on the screen. He welcomes you to a Top Secret Spy Agency and says that he admires your spirit of curiosity and determination. The mysterious figure tells you that everything you have witnessed must be kept secret, and goes on to ask you if you are interested to join this agency. Do you join?(y/n)")
              answer = answer()
                if answer == "y":
                  print("The mysterious figure is pleased that you have joined and tells you that your tools should be somewhere around the room. There are many places the items are hidden: file cabinets, desks, shelves, and even the kitchen. Where do you want to look?")
                  answer = answer()
                  tools = 0
                  while tools < 5:
                  if answer == "file cabinets":
                      print("You look inside the cabinet and find a wrench. Pick it up?(y/n)")
                      if answer == "y":
                          tools += 1
                      elif answer == "desks":
                          print("You look under, on top and inside the desks, but you find nothing there.")
                          continue
                      elif answer == "shelves":
                          print("The shelves are stuffed with various kinds of books. Search deeper?(y/n)")
                          answer = answer()
                          if answer == "y":
                              print("You find a small phone hidden behind the books in the bookshelf. Pick it up?(y/n)")
                              answer = answer()
                              if answer == "y":
                                  tool += 1
                              elif answer == "kitchen":
                                  print("For some reason you decided to go to the kitchen out of your own curiosity. There are cabinets, a fridge, and a freezer. You also notice that some kitchen tiles are missing and damaged and some aren't even placed well onto the floor. Where do you want to look? (Hint: the 'floor' is an option)")
                                  answer = answer()
                                  if answer == "floor":
                                      print("You see that some of the kitchen floor tiles are loose and proceed to yank out some tiles to see if there is anything under them. You find a piece of paper under a tile (Why is it there!?). Pick it up?(y/n)")
                                        if answer == "y":
                                            print("You picked up the strange piece of paper and found out that it is a code sheet.")
                                            tool += 1
    except:
        print("Invalid")
