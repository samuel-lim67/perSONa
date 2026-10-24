def character_selector(choices, character):
    while True:
        print("Choose a persona")
        for index, persona in enumerate(choices):
            print(f"{index+1}. {persona.name}")
        try:
            selection = int(input())
        except ValueError:
            print("Please enter a valid input!")
            continue
        else:
            if selection <= 0:
                print("Please enter a valid input!")
                continue
            else:
                confirm = str(input((f"Are you sure you want to select {choices[selection-1].name}? Y/N\n")))
                if confirm.lower().strip() == "y":
                    character.personas.append(choices[selection - 1])
                    print(f"Successfully selected {choices[selection - 1].name}")
                    return
                else:
                    print("Please enter a valid input!")
                    continue
