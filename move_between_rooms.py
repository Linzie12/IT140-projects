# Module Six Milestone - Move Between Rooms

rooms = {
  'Great Hall': {'south': 'Bedroom'},
  'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
  'Cellar' : {'west' : 'Bedroom'}
}

current_room = 'Great Hall'

while True:
  print(f"You are in the {current_room}")
  command = input("Enter a command: ").strip().lower()
  if command == 'exit':
    current_room = 'exit'
    print("Thanks for playing")
    break
  elif command.startswith('go '):
    direction = command[3:]
    if direction in rooms[current_room]:
      current_room = rooms[current_room][direction]
    else:
      print("You can't go that way.")
      print("Available exits:", ". ".join(rooms[current_room].keys()))
  else:
    print("Invalid command. Try again.")      
