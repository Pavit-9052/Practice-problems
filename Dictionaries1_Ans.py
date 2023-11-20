'''
Problem #1
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
Get user input for the name of the recipe, and then print the recipe. 
Eg: Input : Idli
Output : Here is the recipe for idli. 
You need ingrediants Rice and Dal.
 The procedure to cook is grind rice and dal, ferment and steam.
Input : Yogurt rice
Output :  Here is the recipe for Yogurt rice. 
You need ingrediants Rice and yogurt.
The procedure to cook is cook rice first and then add yogurt.'''

recipes = {
    "idli": {
        "ingredients": ["Rice", "Dal"],
        "procedure": "Grind rice and dal, ferment, and steam."
    },
    "yogurt rice": {
        "ingredients": ["Rice", "Yogurt"],
        "procedure": "Cook rice first and then add yogurt."
    }
}
recipe_name = input("Enter the name of the recipe: ").lower()
if recipe_name in recipes:
    print(f"Here is the recipe for {recipe_name}.")
    print(f"You need ingredients {', '.join(recipes[recipe_name]['ingredients'])}.")
    print(f"The procedure to cook is {recipes[recipe_name]['procedure']}")
else:
    print(f"The recipe {recipe_name} is not available.")

OUTPUT:-
Enter the name of the recipe: IDLI
Here is the recipe for idli.
You need ingredients Rice, Dal.
The procedure to cook is Grind rice and dal, ferment, and steam.


'''Problem #2
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
User input is any ingredient. List all the recipes that include the ingredient
Input : Rice
Output : You can make Idli and Yogurt rice with rice.'''

recipes = {
    "idli":  ["rice", "dal"],
    "yogurt rice": ["rice", "yogurt"],
    "fried rice": ["rice", "vegetables", "soy sauce"],
    "pulao": ["rice", "vegetables", "spices"]       
}
ingredient = input("Enter the name of the ingredient: ").lower()
matching_recipes = []
for recipe, ingredients in recipes.items():
    if ingredient in ingredients:
        matching_recipes.append(recipe)
if matching_recipes:
    print(f"You can make {', '.join(matching_recipes)} with {ingredient}.")
else:
    print(f"There are no recipes with {ingredient}.")

OUTPUT:-
Enter the name of the ingredient: yogurt
You can make yogurt rice with yogurt.


 



