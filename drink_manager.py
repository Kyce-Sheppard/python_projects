# A project to keep links for drink recipes. I just want to get it working and then work on customization

def add_drink():
    drink_name = input("Recipe name: ")
    drink_type = input("What is the drink base? ")
    drink_link = input("Paste the link: ")

    with open('drink_recipes.txt', 'a') as f:
        f.write(f"{drink_name.title()} | {drink_type.lower()} | {drink_link}\n")

def view_drink():
    drink_recipes = []
    with open('drink_recipes.txt', 'r') as f:
        for line in sorted(f.readlines()):
            drink_name, drink_type, drink_link = line.strip().split('|')
            print(f"Drink: {drink_name.title()}| Base spirit: {drink_type.title()}| Link: {drink_link}")
            drink_recipes.append({
                'drink_name': drink_name,
                'drink_type': drink_type,
                'drink_link': drink_link
            })

while True:
    mode = input(
        "Would you like to add a new drink recipe or view the list (view, add), press q to quit. "
        ).lower()
    if mode == "q":
        break
    if mode == "view":
        view_drink()
    elif mode == "add":
        add_drink()
    else:
        print("Invalid mode.")
        continue
