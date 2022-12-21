import requests
import json
import crud


# def practice():
#     id = 511728

#     url = 'https://api.spoonacular.com/recipes/511728/information?'
#     params = {'apiKey' : '33f7af9664464e1fad151db6e46c6399',
#                 }
#     print("*"*20)

#     response = requests.get(url, params)
#     data = response.json()
    
#     print(data)

    # for ingredient in data["extendedIngredients"]:
    #     print(ingredient["name"])
    #     print(ingredient["unit"])
    #     print(ingredient["amount"])\\


results = [(True, 'flour', 2.75, 'cups'), (True, 'soy milk', 1.0, 'cup'), (True, 'cornmeal', 0.25, 'cup'), 
    (True, 'cucumber', 1.0, ''), (True, 'garlic powder', 2.0, ''), (True, 'EVOO', 8.0, 'tablespoons'), 
    (True, 'vanilla yogurt', 1.0, 'container'), (True, 'onion powder', 2.0, ''), (True, 'cheddar cheese', 1.0, 'cup'), 
    (True, 'black olives', 1.5, 'oz'), (True, 'kosher salt', 1.0, 'serving'), (True, 'parmesan', 0.25, 'cup'), 
    (True, 'active yeast', 1.0, 'packet'), (True, 'honey', 1.0, 'TBSP'), (True, 'tomato sauce', 0.5, 'jar'), 
    (True, 'lemon zest', 1.0, ''), (True, 'bell pepper', 1.0, ''), (True, 'pine nuts', 0.5, 'cup'), 
    (True, 'red wine vinegar', 4.0, 'tablespoons'), (True, 'shredded mozzarella cheese', 1.5, 'cups'), 
    (True, 'cherry tomatoes', 1.0, 'pint'), (True, 'green onions', 4.0, ''), (True, 'graham cracker crumbs', 2.0, 'tbsp'),
    (True, 'red onion', 0.75, ''), (True, 'green bell pepper', 1.0, ''), (True, 'parsley', 0.5, 'cup'), 
    (True, 'orzo', 1.0, 'pound'), (True, 'pesto', 4.0, 'TBSP'), (True, 'water', 1.0, 'cup'), (True, 'pepperoncinis', 12.0, ''),
    (True, 'tomatoes', 3.0, ''), (True, 'strawberries', 0.5, 'cup'), (True, 'banana', 0.25, 'cup'), (True, 'olive oil', 2.0, 'TBSP'), 
    (True, 'seasoning', 2.0, ''), (True, 'feta cheese', 1.5, 'cups'), (True, 'salt', 2.0, '')]

grocery_item = {}
total_list = []
for item in results:
    name = grocery_item["ingredient_name"] = item[1]
    amount = grocery_item["amount"] = item[2]
    unit = grocery_item["unit"] = item[3]

    
    total_list.append(grocery_item)


print(total_list)