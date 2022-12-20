import requests
import json
# import crud

# url_work = 'https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=$italian'
# url = "https://api.spoonacular.com/recipes/complexSearch?"
# params = { 'apiKey' : '33f7af9664464e1fad151db6e46c6399',
#             'fillIngredients' : True,
#             'instructionsRequired' : True,
#             'cuisine' : True,
#             'number' : 2
#         }

# url = 'https://api.spoonacular.com/recipes/informationBulk?'
# params = {'apiKey' : '33f7af9664464e1fad151db6e46c6399',
#             'includeNutrition': False,
#             'ids' : '649195, 715424, 716426'
#             }

# response = requests.get(url, params)
# data = response.json()
# results = []

# for recipe in data:
#     id = recipe["id"]
#     title = recipe['title']
#     image = recipe["image"]
#     cuisine = recipe["cuisines"]

#     element = {'id': id, 'title': title, 'image': image, 'cuisines': cuisine}

#     results.append(element)

# print(results)

# for recipe in results:
#     print(recipe['title'])
#     print(recipe['image'])



#-----------------------TRYING TO GET DATA FROM Python, it works on app.py file not here
#     search_recipe = request.form.get("search_recipe")

#     url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_recipe}&number=10"

#     data = '{"key": "value"}'

#     headers = {
#         "Content-Type": "application/json",
#         "apikey" : "33f7af9664464e1fad151db6e46c6399"
#         }
#     response = requests.get(url=url, data={}, headers=headers)
#     cuisine = response.json()
# #    # results = cuisine['results']



# def play_api():

#     url = 'https://api.spoonacular.com/recipes/informationBulk?'
#     params = {'apiKey' : 'a2bcd060e3b446968f90d3b2639acae4',
#                 'ids' : 795751,
#                 }

#     response = requests.get(url, params)
#     data = response.json()
#   #  print(data[0]['id'])
#     instructions_recipe = []

#     for recipe in data:
#         id = recipe["id"]
#         title = recipe['title']
#         image = recipe["image"]
#         instructions = recipe["instructions"].split(".")

#         element = {'id': id, 'title': title, 'image': image, "instructions" : instructions}

#         instructions_recipe.append(element) 

#         ingredients = recipe['extendedIngredients']
#         ingredients_list = []
#         for item in ingredients:
#             name = item['name']
#             amount = item['amount']
#             unit = item['unit']

#             elements = {'name': name, 'amount' : amount, "unit" : unit}
#             ingredients_list.append(elements)

#         for key in instructions_recipe:
#             for item in instructions:
#                 print(item)

#     return f'This are the instructions: {instructions_recipe}...... this are ingredients: {ingredients_list}'



        

# #     #return(instructions_recipe)
# # def play_api():
# #     url ='https://api.spoonacular.com/recipes/715497/information?&apiKey=a2bcd060e3b446968f90d3b2639acae4'

# #     response = requests.get(url)
# #     data = response.json()
# #     print(data)
# #     print('*'*20)
  

# #     instructions_recipe = []

# #     for recipe in data:
# #         id = recipe["id"]
# #         title = recipe['title']
# #         image = recipe["image"]
# #         instructions = recipe["instructions"]

# #         element = {'id': id, 'title': title, 'image': image, "instructions" : instructions}
# #         instructions_recipe.append(element) 

# #     for recipe in data:
# #         ingredients = recipe['extendedIngredients']
        
# #         ingredients_list = []
# #         for item in ingredients:
# #             name = item['name']
# #             amount = item['amount']
# #             unit = item['unit']

# #             elements = {'name': name, 'amount' : amount, "unit" : unit}
# #             ingredients_list.append(elements)
# #     print(instructions_recipe)
# #     print('*'*20)
# #     print(ingredients_list)


#================== GROCERIES =====================
# Get list of total ingredients to buy for all recipes added to meal plan

# Query data to get all recipes ID's added to Meal plan

# list_of_recipe_ids = crud.get_meal_plan_recipe_ids(19)

# print(list_of_recipe_ids)
#[511728, 664411, 654944, 651426, 644218]



    # recipe_ids = [511728, 664411, 654944, 651426, 644218]

    # url = 'https://api.spoonacular.com/recipes/informationBulk?'
    # params = {'apiKey' : 'c898613fbd5c45b090f0a929ffabebab',
    #             'ids' : recipe_ids,
    #             }

    # response = requests.get(url, params)
    # data = response.json()
data = [
{
    "vegetarian": False,
    "vegan": False,
    "glutenFree": False,
    "dairyFree": False,
    "veryHealthy": False,
    "cheap": False,
    "veryPopular": False,
    "sustainable": False,
    "lowFodmap": False,
    "weightWatcherSmartPoints": 24,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 1,
    "healthScore": 27,
    "creditsText": "pickfreshfoods.com",
    "sourceName": "pickfreshfoods.com",
    "pricePerServing": 274.82,
    "extendedIngredients": [
        {
            "id": 2044,
            "aisle": "Produce",
            "image": "fresh-basil.jpg",
            "consistency": "SOLID",
            "name": "fresh basil",
            "nameClean": "fresh basil",
            "original": "¼ cup fresh basil, thinly sliced",
            "originalName": "fresh basil, thinly sliced",
            "amount": 0.25,
            "unit": "cup",
            "meta": [
                "fresh",
                "thinly sliced"
            ],
            "measures": {
                "us": {
                    "amount": 0.25,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 59.147,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 1026,
            "aisle": "Cheese",
            "image": "mozzarella.png",
            "consistency": "SOLID",
            "name": "fresh mozzarella cheese",
            "nameClean": "mozzarella",
            "original": "12 ounces fresh mozzarella cheese, cut into ½-inch cubes",
            "originalName": "fresh mozzarella cheese, cut into ½-inch cubes",
            "amount": 12.0,
            "unit": "ounces",
            "meta": [
                "fresh",
                "cut into ½-inch cubes"
            ],
            "measures": {
                "us": {
                    "amount": 12.0,
                    "unitShort": "oz",
                    "unitLong": "ounces"
                },
                "metric": {
                    "amount": 340.194,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 11215,
            "aisle": "Produce",
            "image": "garlic.png",
            "consistency": "SOLID",
            "name": "garlic clove",
            "nameClean": "garlic",
            "original": "1 garlic clove, pressed",
            "originalName": "garlic clove, pressed",
            "amount": 1.0,
            "unit": "",
            "meta": [
                "pressed"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 10111529,
            "aisle": "Produce",
            "image": "cherry-tomatoes.png",
            "consistency": "SOLID",
            "name": "grape tomatoes",
            "nameClean": "grape tomato",
            "original": "10 oz grape tomatoes, cut in half lengthwise",
            "originalName": "grape tomatoes, cut in half lengthwise",
            "amount": 10.0,
            "unit": "oz",
            "meta": [
                "cut in half lengthwise"
            ],
            "measures": {
                "us": {
                    "amount": 10.0,
                    "unitShort": "oz",
                    "unitLong": "ounces"
                },
                "metric": {
                    "amount": 283.495,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 1082047,
            "aisle": "Spices and Seasonings",
            "image": "salt.jpg",
            "consistency": "SOLID",
            "name": "kosher salt",
            "nameClean": "kosher salt",
            "original": "½ tsp kosher salt",
            "originalName": "kosher salt",
            "amount": 0.5,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 4053,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "olive-oil.jpg",
            "consistency": "LIQUID",
            "name": "olive oil",
            "nameClean": "olive oil",
            "original": "¼ cup extra-virgin olive oil",
            "originalName": "extra-virgin olive oil",
            "amount": 0.25,
            "unit": "cup",
            "meta": [
                "extra-virgin"
            ],
            "measures": {
                "us": {
                    "amount": 0.25,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 59.147,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 20420,
            "aisle": "Pasta and Rice",
            "image": "fusilli.jpg",
            "consistency": "SOLID",
            "name": "pasta",
            "nameClean": "pasta",
            "original": "1 pound linguine pasta",
            "originalName": "linguine pasta",
            "amount": 1.0,
            "unit": "pound",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "lb",
                    "unitLong": "pound"
                },
                "metric": {
                    "amount": 453.592,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        }
    ],
    "id": 511728,
    "title": "Pasta Margherita",
    "readyInMinutes": 45,
    "servings": 4,
    "sourceUrl": "http://pickfreshfoods.com/pasta-margherita/",
    "image": "https://spoonacular.com/recipeImages/511728-556x370.jpg",
    "imageType": "jpg",
    "summary": "Pasta Margherita might be just the main course you are searching for. One serving contains <b>809 calories</b>, <b>34g of protein</b>, and <b>34g of fat</b>. This recipe serves 4 and costs $2.75 per serving. 1 person has made this recipe and would make it again. If you have basil, linguine pasta, garlic clove, and a few other ingredients on hand, you can make it. To use up the olive oil you could follow this main course with the <a href=\"https://spoonacular.com/recipes/sauteed-banana-granola-and-yogurt-parfait-624619\">Sauteed Banana, Granolan and Yogurt Parfait</a> as a dessert. All things considered, we decided this recipe <b>deserves a spoonacular score of 69%</b>. This score is pretty good. Similar recipes include <a href=\"https://spoonacular.com/recipes/margherita-pizza-with-pesto-pasta-salad-31919\">Margherita Pizza With Pesto Pasta Salad</a>, <a href=\"https://spoonacular.com/recipes/pasta-margherita-with-rhubarb-and-apple-compote-613006\">Pasta margherita with rhubarb and apple compote</a>, and <a href=\"https://spoonacular.com/recipes/margherita-pizzette-516272\">Margherita Pizzette</a>.",
    "cuisines": [],
    "dishTypes": [
        "lunch",
        "main course",
        "main dish",
        "dinner"
    ],
    "diets": [],
    "occasions": [],
    "winePairing": {
        "pairedWines": [],
        "pairingText": "No one wine will suit every pasta dish. Pasta in a tomato-based sauce will usually work well with a medium-bodied red, such as a montepulciano or chianti. Pasta with seafood or pesto will fare better with a light-bodied white, such as a pinot grigio. Cheese-heavy pasta can pair well with red or white - you might try a sangiovese wine for hard cheeses and a chardonnay for soft cheeses. We may be able to make a better recommendation if you ask again with a specific pasta dish.",
        "productMatches": []
    },
    "instructions": "Whisk oil, garlic, basil, salt together in large bowl. Add tomatoes and mozzarella then gently toss to combine; set aside.Cook pasta according to package directions for al dente. Drain well.Add pasta to tomato mixture and gently toss to combine.Serve immediately.",
    "analyzedInstructions": [
        {
            "name": "",
            "steps": [
                {
                    "number": 1,
                    "step": "Whisk oil, garlic, basil, salt together in large bowl.",
                    "ingredients": [
                        {
                            "id": 11215,
                            "name": "garlic",
                            "localizedName": "garlic",
                            "image": "garlic.png"
                        },
                        {
                            "id": 2044,
                            "name": "basil",
                            "localizedName": "basil",
                            "image": "basil.jpg"
                        },
                        {
                            "id": 2047,
                            "name": "salt",
                            "localizedName": "salt",
                            "image": "salt.jpg"
                        },
                        {
                            "id": 4582,
                            "name": "cooking oil",
                            "localizedName": "cooking oil",
                            "image": "vegetable-oil.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404661,
                            "name": "whisk",
                            "localizedName": "whisk",
                            "image": "whisk.png"
                        },
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        }
                    ]
                },
                {
                    "number": 2,
                    "step": "Add tomatoes and mozzarella then gently toss to combine; set aside.Cook pasta according to package directions for al dente.",
                    "ingredients": [
                        {
                            "id": 1026,
                            "name": "mozzarella",
                            "localizedName": "mozzarella",
                            "image": "mozzarella.png"
                        },
                        {
                            "id": 11529,
                            "name": "tomato",
                            "localizedName": "tomato",
                            "image": "tomato.png"
                        },
                        {
                            "id": 20420,
                            "name": "pasta",
                            "localizedName": "pasta",
                            "image": "fusilli.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 3,
                    "step": "Drain well.",
                    "ingredients": [],
                    "equipment": []
                },
                {
                    "number": 4,
                    "step": "Add pasta to tomato mixture and gently toss to combine.",
                    "ingredients": [
                        {
                            "id": 11529,
                            "name": "tomato",
                            "localizedName": "tomato",
                            "image": "tomato.png"
                        },
                        {
                            "id": 20420,
                            "name": "pasta",
                            "localizedName": "pasta",
                            "image": "fusilli.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 5,
                    "step": "Serve immediately.",
                    "ingredients": [],
                    "equipment": []
                }
            ]
        }
    ],
    "originalId": "null",
    "spoonacularSourceUrl": "https://spoonacular.com/pasta-margherita-511728"
},
{
    "vegetarian": True,
    "vegan": True,
    "glutenFree": False,
    "dairyFree": True,
    "veryHealthy": False,
    "cheap": False,
    "veryPopular": False,
    "sustainable": False,
    "lowFodmap": False,
    "weightWatcherSmartPoints": 6,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 1,
    "healthScore": 2,
    "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
    "license": "CC BY 3.0",
    "sourceName": "Foodista",
    "pricePerServing": 31.85,
    "extendedIngredients": [
        {
            "id": 2048,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "apple-cider-vinegar.jpg",
            "consistency": "LIQUID",
            "name": "apple cider vinegar",
            "nameClean": "apple cider vinegar",
            "original": "1 teaspoon apple cider vinegar",
            "originalName": "apple cider vinegar",
            "amount": 1.0,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                }
            }
        },
        {
            "id": 18371,
            "aisle": "Baking",
            "image": "white-powder.jpg",
            "consistency": "SOLID",
            "name": "baking powder",
            "nameClean": "low sodium baking powder",
            "original": "1 1/2 tsp of baking powder",
            "originalName": "baking powder",
            "amount": 1.5,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 1.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 18372,
            "aisle": "Baking",
            "image": "white-powder.jpg",
            "consistency": "SOLID",
            "name": "baking soda",
            "nameClean": "baking soda",
            "original": "1 teaspoon baking soda",
            "originalName": "baking soda",
            "amount": 1.0,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                }
            }
        },
        {
            "id": 4582,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "vegetable-oil.jpg",
            "consistency": "LIQUID",
            "name": "canola oil",
            "nameClean": "cooking oil",
            "original": "cup canola oil",
            "originalName": "canola oil",
            "amount": 1.0,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "cup",
                    "unitLong": "cup"
                },
                "metric": {
                    "amount": 236.588,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 19165,
            "aisle": "Baking",
            "image": "cocoa-powder.png",
            "consistency": "SOLID",
            "name": "cocoa powder",
            "nameClean": "cacao powder",
            "original": "cup cocoa powder",
            "originalName": "cocoa powder",
            "amount": 1.0,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "cup",
                    "unitLong": "cup"
                },
                "metric": {
                    "amount": 236.588,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 20081,
            "aisle": "Baking",
            "image": "flour.png",
            "consistency": "SOLID",
            "name": "flour",
            "nameClean": "wheat flour",
            "original": "1 1/2 cups of flour",
            "originalName": "flour",
            "amount": 1.5,
            "unit": "cups",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 354.882,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 19335,
            "aisle": "Baking",
            "image": "sugar-in-bowl.png",
            "consistency": "SOLID",
            "name": "granulated sugar",
            "nameClean": "sugar",
            "original": "3/4 cup granulated sugar",
            "originalName": "granulated sugar",
            "amount": 0.75,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.75,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 177.441,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 2047,
            "aisle": "Spices and Seasonings",
            "image": "salt.jpg",
            "consistency": "SOLID",
            "name": "salt",
            "nameClean": "table salt",
            "original": "1/2 teaspoon salt",
            "originalName": "salt",
            "amount": 0.5,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 16223,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "soy-milk.jpg",
            "consistency": "LIQUID",
            "name": "soy milk",
            "nameClean": "soymilk",
            "original": "1/8 cup of soy milk",
            "originalName": "soy milk",
            "amount": 0.125,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.125,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 29.573,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 2050,
            "aisle": "Baking",
            "image": "vanilla-extract.jpg",
            "consistency": "LIQUID",
            "name": "vanilla extract",
            "nameClean": "vanilla extract",
            "original": "2 teaspoons vanilla extract",
            "originalName": "vanilla extract",
            "amount": 2.0,
            "unit": "teaspoons",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        }
    ],
    "id": 664411,
    "title": "Vegan Chocolate Cupcakes",
    "readyInMinutes": 45,
    "servings": 10,
    "sourceUrl": "http://www.foodista.com/recipe/XDFZ4LTV/vegan-chocolate-cupcakes",
    "image": "https://spoonacular.com/recipeImages/664411-556x370.jpg",
    "imageType": "jpg",
    "summary": "The recipe Vegan Chocolate Cupcakes could satisfy your American craving in roughly <b>45 minutes</b>. For <b>32 cents per serving</b>, this recipe <b>covers 7%</b> of your daily requirements of vitamins and minerals. One serving contains <b>170 calories</b>, <b>4g of protein</b>, and <b>4g of fat</b>. Head to the store and pick up granulated sugar, vanillan extract, soy milk, and a few other things to make it today. 1 person were impressed by this recipe. It is a good option if you're following a <b>vegan</b> diet. It works well as a cheap dessert. All things considered, we decided this recipe <b>deserves a spoonacular score of 28%</b>. This score is rather bad. Try <a href=\"https://spoonacular.com/recipes/eggless-orange-chocolate-cupcakes-vegan-cupcakes-600454\">Eggless Orange Chocolate Cupcakes | Vegan Cupcakes</a>, <a href=\"https://spoonacular.com/recipes/vegan-chocolate-ganache-cupcakes-with-salted-caramel-and-dark-chocolate-buttercream-295336\">Vegan Chocolate Ganache Cupcakes with Salted Caramel and Dark Chocolate Buttercream</a>, and <a href=\"https://spoonacular.com/recipes/vegan-mini-vanilla-and-chocolate-swirl-cupcakes-and-how-to-make-mini-cupcakes-575642\">Vegan Mini Vanillan and Chocolate Swirl Cupcakes (and how to make mini cupcakes)</a> for similar recipes.",
    "cuisines": [
        "American"
    ],
    "dishTypes": [
        "side dish"
    ],
    "diets": [
        "dairy free",
        "lacto ovo vegetarian",
        "vegan"
    ],
    "occasions": [],
    "winePairing": {
        "pairedWines": [],
        "pairingText": "",
        "productMatches": []
    },
    "instructions": "<ol><li>Preheat oven to 350 degrees and line muffin pan with paper or foil liners</li><li>Whisk together the soy milk and vinegar in a large bowl, and set aside for a few minutes to curdle. Add the sugar, oil, and vanilla extract to the soy milk mixture and beat until foamy. In a separate bowl, sift together the flour, cocoa powder, baking soda, baking powder and salt. Add in two batches to wet ingredients and beat until no large lumps remain.</li><li>Pour into liners, filling three-quarters of the way. Bake 18 to 20 minutes or until a toothpick inserted in the center comes out clean. Transfer to cooling rack and let cool completely.</li></ol>",
    "analyzedInstructions": [
        {
            "name": "",
            "steps": [
                {
                    "number": 1,
                    "step": "Preheat oven to 350 degrees and line muffin pan with paper or foil liners",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404671,
                            "name": "muffin tray",
                            "localizedName": "muffin tray",
                            "image": "muffin-tray.jpg"
                        },
                        {
                            "id": 404765,
                            "name": "aluminum foil",
                            "localizedName": "aluminum foil",
                            "image": "aluminum-foil.png"
                        },
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ]
                },
                {
                    "number": 2,
                    "step": "Whisk together the soy milk and vinegar in a large bowl, and set aside for a few minutes to curdle.",
                    "ingredients": [
                        {
                            "id": 16223,
                            "name": "soymilk",
                            "localizedName": "soymilk",
                            "image": "soy-milk.jpg"
                        },
                        {
                            "id": 2053,
                            "name": "vinegar",
                            "localizedName": "vinegar",
                            "image": "vinegar-(white).jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404661,
                            "name": "whisk",
                            "localizedName": "whisk",
                            "image": "whisk.png"
                        },
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        }
                    ]
                },
                {
                    "number": 3,
                    "step": "Add the sugar, oil, and vanilla extract to the soy milk mixture and beat until foamy. In a separate bowl, sift together the flour, cocoa powder, baking soda, baking powder and salt.",
                    "ingredients": [
                        {
                            "id": 2050,
                            "name": "vanilla extract",
                            "localizedName": "vanilla extract",
                            "image": "vanilla-extract.jpg"
                        },
                        {
                            "id": 18369,
                            "name": "baking powder",
                            "localizedName": "baking powder",
                            "image": "white-powder.jpg"
                        },
                        {
                            "id": 19165,
                            "name": "cocoa powder",
                            "localizedName": "cocoa powder",
                            "image": "cocoa-powder.png"
                        },
                        {
                            "id": 18372,
                            "name": "baking soda",
                            "localizedName": "baking soda",
                            "image": "white-powder.jpg"
                        },
                        {
                            "id": 16223,
                            "name": "soymilk",
                            "localizedName": "soymilk",
                            "image": "soy-milk.jpg"
                        },
                        {
                            "id": 20081,
                            "name": "all purpose flour",
                            "localizedName": "all purpose flour",
                            "image": "flour.png"
                        },
                        {
                            "id": 19335,
                            "name": "sugar",
                            "localizedName": "sugar",
                            "image": "sugar-in-bowl.png"
                        },
                        {
                            "id": 2047,
                            "name": "salt",
                            "localizedName": "salt",
                            "image": "salt.jpg"
                        },
                        {
                            "id": 4582,
                            "name": "cooking oil",
                            "localizedName": "cooking oil",
                            "image": "vegetable-oil.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        }
                    ]
                },
                {
                    "number": 4,
                    "step": "Add in two batches to wet ingredients and beat until no large lumps remain.",
                    "ingredients": [],
                    "equipment": []
                },
                {
                    "number": 5,
                    "step": "Pour into liners, filling three-quarters of the way.",
                    "ingredients": [],
                    "equipment": []
                },
                {
                    "number": 6,
                    "step": "Bake 18 to 20 minutes or until a toothpick inserted in the center comes out clean.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404644,
                            "name": "toothpicks",
                            "localizedName": "toothpicks",
                            "image": "toothpicks.jpg"
                        },
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ],
                    "length": {
                        "number": 18,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 7,
                    "step": "Transfer to cooling rack and let cool completely.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 405900,
                            "name": "wire rack",
                            "localizedName": "wire rack",
                            "image": "wire-rack.jpg"
                        }
                    ]
                }
            ]
        }
    ],
    "originalId": "null",
    "spoonacularSourceUrl": "https://spoonacular.com/vegan-chocolate-cupcakes-664411"
},
{
    "vegetarian": False,
    "vegan": False,
    "glutenFree": False,
    "dairyFree": False,
    "veryHealthy": False,
    "cheap": False,
    "veryPopular": False,
    "sustainable": False,
    "lowFodmap": False,
    "weightWatcherSmartPoints": 13,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 3,
    "healthScore": 20,
    "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
    "license": "CC BY 3.0",
    "sourceName": "Foodista",
    "pricePerServing": 160.13,
    "extendedIngredients": [
        {
            "id": 1001,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "butter-sliced.jpg",
            "consistency": "SOLID",
            "name": "butter",
            "nameClean": "butter",
            "original": "2 tablespoons butter - (¼ stick)",
            "originalName": "butter - (¼ stick)",
            "amount": 2.0,
            "unit": "tablespoons",
            "meta": [
                "()"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        },
        {
            "id": 20081,
            "aisle": "Baking",
            "image": "flour.png",
            "consistency": "SOLID",
            "name": "flour",
            "nameClean": "wheat flour",
            "original": "2 teaspoons Flour, all purpose",
            "originalName": "Flour, all purpose",
            "amount": 2.0,
            "unit": "teaspoons",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 1077,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "milk.png",
            "consistency": "LIQUID",
            "name": "milk",
            "nameClean": "milk",
            "original": "1 1/4 cups Milk",
            "originalName": "Milk",
            "amount": 1.25,
            "unit": "cups",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.25,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 295.735,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 11282,
            "aisle": "Produce",
            "image": "brown-onion.png",
            "consistency": "SOLID",
            "name": "onion",
            "nameClean": "onion",
            "original": "2 teaspoons Onion, minced",
            "originalName": "Onion, minced",
            "amount": 2.0,
            "unit": "teaspoons",
            "meta": [
                "minced"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 1033,
            "aisle": "Cheese",
            "image": "parmesan.jpg",
            "consistency": "SOLID",
            "name": "parmesan cheese",
            "nameClean": "parmesan",
            "original": "1/2 cup Parmesan cheese, grated",
            "originalName": "Parmesan cheese, grated",
            "amount": 0.5,
            "unit": "cup",
            "meta": [
                "grated"
            ],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 118.294,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 11297,
            "aisle": "Produce;Spices and Seasonings",
            "image": "parsley.jpg",
            "consistency": "SOLID",
            "name": "parsley",
            "nameClean": "parsley",
            "original": "1/4 cup Parsley",
            "originalName": "Parsley",
            "amount": 0.25,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.25,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 59.147,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 11304,
            "aisle": "Produce",
            "image": "peas.jpg",
            "consistency": "SOLID",
            "name": "peas",
            "nameClean": "petite peas",
            "original": "1 cup Peas",
            "originalName": "Peas",
            "amount": 1.0,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "cup",
                    "unitLong": "cup"
                },
                "metric": {
                    "amount": 236.588,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 11120420,
            "aisle": "Pasta and Rice",
            "image": "penne-pasta.jpg",
            "consistency": "SOLID",
            "name": "penne",
            "nameClean": "penne",
            "original": "8 ounces Penne or zita or other tubul",
            "originalName": "Penne or zita or other tubul",
            "amount": 8.0,
            "unit": "ounces",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 8.0,
                    "unitShort": "oz",
                    "unitLong": "ounces"
                },
                "metric": {
                    "amount": 226.796,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 1002030,
            "aisle": "Spices and Seasonings",
            "image": "pepper.jpg",
            "consistency": "SOLID",
            "name": "pepper",
            "nameClean": "black pepper",
            "original": "1/4 teaspoon Pepper",
            "originalName": "Pepper",
            "amount": 0.25,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.25,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.25,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 15076,
            "aisle": "Seafood",
            "image": "salmon.png",
            "consistency": "SOLID",
            "name": "salmon",
            "nameClean": "salmon",
            "original": "1 cup Salmon, red sockeye",
            "originalName": "Salmon, red sockeye",
            "amount": 1.0,
            "unit": "cup",
            "meta": [
                "red"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "cup",
                    "unitLong": "cup"
                },
                "metric": {
                    "amount": 236.588,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        }
    ],
    "id": 654944,
    "title": "Pasta With Salmon Cream Sauce",
    "readyInMinutes": 45,
    "servings": 4,
    "sourceUrl": "http://www.foodista.com/recipe/WRF73JT3/pasta-with-salmon-cream-sauce",
    "image": "https://spoonacular.com/recipeImages/654944-556x370.jpg",
    "imageType": "jpg",
    "summary": "Pasta With Salmon Cream Sauce is a <b>pescatarian</b> main course. This recipe makes 4 servings with <b>439 calories</b>, <b>23g of protein</b>, and <b>15g of fat</b> each. For <b>$1.6 per serving</b>, this recipe <b>covers 23%</b> of your daily requirements of vitamins and minerals. 3 people have made this recipe and would make it again. If you have onion, parsley, milk, and a few other ingredients on hand, you can make it. To use up the milk you could follow this main course with the <a href=\"https://spoonacular.com/recipes/milky-way-brownie-bites-540544\">Milky Way Brownie Bites</a> as a dessert. From preparation to the plate, this recipe takes roughly <b>45 minutes</b>. All things considered, we decided this recipe <b>deserves a spoonacular score of 69%</b>. This score is pretty good. Try <a href=\"https://spoonacular.com/recipes/spinach-pasta-with-salmon-and-cream-sauce-86877\">Spinach Pasta with Salmon and Cream Sauce</a>, <a href=\"https://spoonacular.com/recipes/artisan-farfalle-pasta-with-smoked-salmon-and-cream-sauce-632778\">Artisan Farfalle Pasta With Smoked Salmon and Cream Sauce</a>, and <a href=\"https://spoonacular.com/recipes/chocolate-pasta-with-gorgonzola-cream-sauce-and-10-romantic-pasta-dishes-532706\">Chocolate Pasta with Gorgonzola Cream Sauce and 10 Romantic Pasta Dishes</a> for similar recipes.",
    "cuisines": [],
    "dishTypes": [
        "lunch",
        "main course",
        "main dish",
        "dinner"
    ],
    "diets": [
        "pescatarian"
    ],
    "occasions": [],
    "winePairing": {
        "pairedWines": [],
        "pairingText": "No one wine will suit every pasta dish. Pasta in a tomato-based sauce will usually work well with a medium-bodied red, such as a montepulciano or chianti. Pasta with seafood or pesto will fare better with a light-bodied white, such as a pinot grigio. Cheese-heavy pasta can pair well with red or white - you might try a sangiovese wine for hard cheeses and a chardonnay for soft cheeses. We may be able to make a better recommendation if you ask again with a specific pasta dish.",
        "productMatches": []
    },
    "instructions": "<ol><li>Calories per serving: 300 In large pot of boiling water, cook pasta al dente (tender but firm) about 10 12 minutes. Drain and return to pot. In saucepan, melt butter over medium heat add onion and cook until tender.</li><li>Stir in flour and cook for a few seconds. Whisk in milk and bring to sa simmer, stirring constantly. Add peas, salmon brokin into chunks and salmon juices, parsley, cheese, pepper. Pour mixture over pasta and stir gently to mix. Serve Immediately. Microwave method: Cook pasta as above in glass bowl or 4 cup measure. Microwave butter and onion at Medium-High for 1 minute or until onion is tender. Stir in flour to form smooth paste. Gradually whisk in milk. </li></ol>",
    "analyzedInstructions": [
        {
            "name": "",
            "steps": [
                {
                    "number": 1,
                    "step": "Calories per serving: 300 In large pot of boiling water, cook pasta al dente (tender but firm) about 10 12 minutes.",
                    "ingredients": [
                        {
                            "id": 20420,
                            "name": "pasta",
                            "localizedName": "pasta",
                            "image": "fusilli.jpg"
                        },
                        {
                            "id": 14412,
                            "name": "water",
                            "localizedName": "water",
                            "image": "water.png"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404752,
                            "name": "pot",
                            "localizedName": "pot",
                            "image": "stock-pot.jpg"
                        }
                    ],
                    "length": {
                        "number": 12,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 2,
                    "step": "Drain and return to pot. In saucepan, melt butter over medium heat add onion and cook until tender.Stir in flour and cook for a few seconds.",
                    "ingredients": [
                        {
                            "id": 1001,
                            "name": "butter",
                            "localizedName": "butter",
                            "image": "butter-sliced.jpg"
                        },
                        {
                            "id": 20081,
                            "name": "all purpose flour",
                            "localizedName": "all purpose flour",
                            "image": "flour.png"
                        },
                        {
                            "id": 11282,
                            "name": "onion",
                            "localizedName": "onion",
                            "image": "brown-onion.png"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404669,
                            "name": "sauce pan",
                            "localizedName": "sauce pan",
                            "image": "sauce-pan.jpg"
                        },
                        {
                            "id": 404752,
                            "name": "pot",
                            "localizedName": "pot",
                            "image": "stock-pot.jpg"
                        }
                    ]
                },
                {
                    "number": 3,
                    "step": "Whisk in milk and bring to sa simmer, stirring constantly.",
                    "ingredients": [
                        {
                            "id": 1077,
                            "name": "milk",
                            "localizedName": "milk",
                            "image": "milk.png"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404661,
                            "name": "whisk",
                            "localizedName": "whisk",
                            "image": "whisk.png"
                        }
                    ]
                },
                {
                    "number": 4,
                    "step": "Add peas, salmon brokin into chunks and salmon juices, parsley, cheese, pepper.",
                    "ingredients": [
                        {
                            "id": 11297,
                            "name": "parsley",
                            "localizedName": "parsley",
                            "image": "parsley.jpg"
                        },
                        {
                            "id": 1041009,
                            "name": "cheese",
                            "localizedName": "cheese",
                            "image": "cheddar-cheese.png"
                        },
                        {
                            "id": 1002030,
                            "name": "pepper",
                            "localizedName": "pepper",
                            "image": "pepper.jpg"
                        },
                        {
                            "id": 15076,
                            "name": "salmon",
                            "localizedName": "salmon",
                            "image": "salmon.png"
                        },
                        {
                            "id": 11304,
                            "name": "peas",
                            "localizedName": "peas",
                            "image": "peas.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 5,
                    "step": "Pour mixture over pasta and stir gently to mix.",
                    "ingredients": [
                        {
                            "id": 20420,
                            "name": "pasta",
                            "localizedName": "pasta",
                            "image": "fusilli.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 6,
                    "step": "Serve Immediately. Microwave method: Cook pasta as above in glass bowl or 4 cup measure. Microwave butter and onion at Medium-High for 1 minute or until onion is tender. Stir in flour to form smooth paste. Gradually whisk in milk.",
                    "ingredients": [
                        {
                            "id": 1001,
                            "name": "butter",
                            "localizedName": "butter",
                            "image": "butter-sliced.jpg"
                        },
                        {
                            "id": 20081,
                            "name": "all purpose flour",
                            "localizedName": "all purpose flour",
                            "image": "flour.png"
                        },
                        {
                            "id": 11282,
                            "name": "onion",
                            "localizedName": "onion",
                            "image": "brown-onion.png"
                        },
                        {
                            "id": 20420,
                            "name": "pasta",
                            "localizedName": "pasta",
                            "image": "fusilli.jpg"
                        },
                        {
                            "id": 1077,
                            "name": "milk",
                            "localizedName": "milk",
                            "image": "milk.png"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404762,
                            "name": "microwave",
                            "localizedName": "microwave",
                            "image": "microwave.jpg"
                        },
                        {
                            "id": 404661,
                            "name": "whisk",
                            "localizedName": "whisk",
                            "image": "whisk.png"
                        },
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        }
                    ],
                    "length": {
                        "number": 1,
                        "unit": "minutes"
                    }
                }
            ]
        }
    ],
    "originalId": "null",
    "spoonacularSourceUrl": "https://spoonacular.com/pasta-with-salmon-cream-sauce-654944"
},
{
    "vegetarian": False,
    "vegan": False,
    "glutenFree": False,
    "dairyFree": False,
    "veryHealthy": False,
    "cheap": False,
    "veryPopular": False,
    "sustainable": False,
    "lowFodmap": False,
    "weightWatcherSmartPoints": 12,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 4,
    "healthScore": 38,
    "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
    "license": "CC BY 3.0",
    "sourceName": "Foodista",
    "pricePerServing": 197.13,
    "extendedIngredients": [
        {
            "id": 10920420,
            "aisle": "Pasta and Rice",
            "image": "orzo.jpg",
            "consistency": "SOLID",
            "name": "orzo",
            "nameClean": "orzo",
            "original": "1 pound orzo",
            "originalName": "orzo",
            "amount": 1.0,
            "unit": "pound",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "lb",
                    "unitLong": "pound"
                },
                "metric": {
                    "amount": 453.592,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 1082047,
            "aisle": "Spices and Seasonings",
            "image": "salt.jpg",
            "consistency": "SOLID",
            "name": "kosher salt",
            "nameClean": "kosher salt",
            "original": "Kosher salt",
            "originalName": "Kosher salt",
            "amount": 1.0,
            "unit": "serving",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "serving",
                    "unitLong": "serving"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "serving",
                    "unitLong": "serving"
                }
            }
        },
        {
            "id": 12147,
            "aisle": "Produce;Baking",
            "image": "pine-nuts.png",
            "consistency": "SOLID",
            "name": "pine nuts",
            "nameClean": "pine nuts",
            "original": "1/2 cup pine nuts",
            "originalName": "pine nuts",
            "amount": 0.5,
            "unit": "cup",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 118.294,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 1034053,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "olive-oil.jpg",
            "consistency": "LIQUID",
            "name": "EVOO",
            "nameClean": "extra virgin olive oil",
            "original": "8 tablespoons EVOO",
            "originalName": "EVOO",
            "amount": 8.0,
            "unit": "tablespoons",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 8.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 8.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        },
        {
            "id": 11291,
            "aisle": "Produce",
            "image": "spring-onions.jpg",
            "consistency": "SOLID",
            "name": "green onions",
            "nameClean": "spring onions",
            "original": "4 green onions, chopped",
            "originalName": "green onions, chopped",
            "amount": 4.0,
            "unit": "",
            "meta": [
                "chopped"
            ],
            "measures": {
                "us": {
                    "amount": 4.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 4.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 11297,
            "aisle": "Produce;Spices and Seasonings",
            "image": "parsley.jpg",
            "consistency": "SOLID",
            "name": "parsley",
            "nameClean": "parsley",
            "original": "1/2 cup Italian parsley, chopped",
            "originalName": "Italian parsley, chopped",
            "amount": 0.5,
            "unit": "cup",
            "meta": [
                "italian",
                "chopped"
            ],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 118.294,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 9156,
            "aisle": "Produce",
            "image": "zest-lemon.jpg",
            "consistency": "SOLID",
            "name": "lemon zest",
            "nameClean": "lemon peel",
            "original": "1 Juice and zest of 1 lemon",
            "originalName": "Juice and zest of 1 lemon",
            "amount": 1.0,
            "unit": "",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 11206,
            "aisle": "Produce",
            "image": "cucumber.jpg",
            "consistency": "SOLID",
            "name": "cucumber",
            "nameClean": "cucumber",
            "original": "1 cucumber, diced",
            "originalName": "cucumber, diced",
            "amount": 1.0,
            "unit": "",
            "meta": [
                "diced"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 11333,
            "aisle": "Produce",
            "image": "green-pepper.jpg",
            "consistency": "SOLID",
            "name": "green bell pepper",
            "nameClean": "green pepper",
            "original": "1 green bell pepper, chopped",
            "originalName": "green bell pepper, chopped",
            "amount": 1.0,
            "unit": "",
            "meta": [
                "green",
                "chopped"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 10311529,
            "aisle": "Produce",
            "image": "cherry-tomatoes.png",
            "consistency": "SOLID",
            "name": "cherry tomatoes",
            "nameClean": "cherry tomato",
            "original": "1 pint cherry tomatoes",
            "originalName": "cherry tomatoes",
            "amount": 1.0,
            "unit": "pint",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "pts",
                    "unitLong": "pint"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "pts",
                    "unitLong": "pint"
                }
            }
        },
        {
            "id": 10011282,
            "aisle": "Produce",
            "image": "red-onion.png",
            "consistency": "SOLID",
            "name": "red onion",
            "nameClean": "red onion",
            "original": "1/2 red onion, finely chopped",
            "originalName": "red onion, finely chopped",
            "amount": 0.5,
            "unit": "",
            "meta": [
                "red",
                "finely chopped"
            ],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 11976,
            "aisle": "Canned and Jarred",
            "image": "pepperoncini.jpg",
            "consistency": "SOLID",
            "name": "pepperoncinis",
            "nameClean": "banana pepper",
            "original": "12 pepperoncinis, sliced",
            "originalName": "pepperoncinis, sliced",
            "amount": 12.0,
            "unit": "",
            "meta": [
                "sliced"
            ],
            "measures": {
                "us": {
                    "amount": 12.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 12.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 1019,
            "aisle": "Cheese",
            "image": "feta.png",
            "consistency": "SOLID",
            "name": "feta cheese",
            "nameClean": "feta cheese",
            "original": "1 1/2 cups crumbled feta cheese",
            "originalName": "crumbled feta cheese",
            "amount": 1.5,
            "unit": "cups",
            "meta": [
                "crumbled"
            ],
            "measures": {
                "us": {
                    "amount": 1.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 354.882,
                    "unitShort": "ml",
                    "unitLong": "milliliters"
                }
            }
        },
        {
            "id": 1022068,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "red-wine-vinegar.jpg",
            "consistency": "LIQUID",
            "name": "red wine vinegar",
            "nameClean": "red wine vinegar",
            "original": "4 tablespoons red wine vinegar",
            "originalName": "red wine vinegar",
            "amount": 4.0,
            "unit": "tablespoons",
            "meta": [
                "red"
            ],
            "measures": {
                "us": {
                    "amount": 4.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 4.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        }
    ],
    "id": 651426,
    "title": "Mediterranean Orzo Salad",
    "readyInMinutes": 45,
    "servings": 10,
    "sourceUrl": "https://www.foodista.com/recipe/P6QQ46HN/mediterranean-orzo-salad",
    "image": "https://spoonacular.com/recipeImages/651426-556x370.jpg",
    "imageType": "jpg",
    "summary": "The recipe Mediterranean Orzo Salad can be made <b>in about about 45 minutes</b>. This recipe serves 10. One portion of this dish contains approximately <b>11g of protein</b>, <b>22g of fat</b>, and a total of <b>396 calories</b>. For <b>$1.97 per serving</b>, this recipe <b>covers 19%</b> of your daily requirements of vitamins and minerals. Head to the store and pick up pepperoncinis, bell pepper, wine vinegar, and a few other things to make it today. It works well as an affordable side dish. It is brought to you by Foodista. This recipe is liked by 4 foodies and cooks. With a spoonacular <b>score of 79%</b>, this dish is solid. If you like this recipe, take a look at these similar recipes: <a href=\"https://spoonacular.com/recipes/mediterranean-orzo-salad-30149\">Mediterranean Orzo Salad</a>, <a href=\"https://spoonacular.com/recipes/mediterranean-orzo-salad-924212\">Mediterranean Orzo Salad</a>, and <a href=\"https://spoonacular.com/recipes/mediterranean-orzo-salad-892728\">Mediterranean Orzo Salad</a>.",
    "cuisines": [],
    "dishTypes": [
        "side dish",
        "salad"
    ],
    "diets": [],
    "occasions": [],
    "winePairing": {
        "pairedWines": [
            "chardonnay",
            "sauvignon blanc",
            "gruener veltliner"
        ],
        "pairingText": "Chardonnay, Sauvignon Blanc, and Gruener Veltliner are great choices for Salad. Sauvignon Blanc and Gruner Veltliner both have herby notes that complement salads with enough acid to match tart vinaigrettes, while a Chardonnay can be a good pick for creamy salad dressings.",
        "productMatches": [
            {
                "id": 432786,
                "title": "Tom Eddy Manchester Ridge Chardonnay",
                "description": "The aroma is intense with many nuanced layers that marry classic California Chardonnay characteristics with a kiss of old world style. Right off the top, beautiful Chardonnay varietal notes commingle with subtle toast, understated butter cream and crisp green apple. During the ageing process, weekly lees stirring in the barrel left the palate rich and full without being flabby as the signature Manchester acidity leaves a clean and lingering finish. The French Oak barrels bestow a tinge of brown sugar that is nuanced and inviting without being overbearing. This allows for the showcasing of the superb fruit that comes from this one-of-a-kind vineyard. Cheers!",
                "imageUrl": "https://spoonacular.com/productImages/432786-312x231.jpg",
                "averageRating": 1.0,
                "ratingCount": 1.0,
                "score": 0.75,
                "link": "https://www.amazon.com/Tom-Eddy-Manchester-Ridge-Chardonnay/dp/B00GYDZYJO?tag=spoonacular-20"
            }
        ]
    },
    "instructions": "Bring a pot of water to a rapid boil. Generously salt water and cook orzo until tender, approximately 7-9 minutes. Drain and set aside.\nWhile orzo is cooking, spread pine nuts on a baking sheet and toast lightly in oven on 400 degrees. Remove from oven and set aside.\nHeat two tablespoons of EVOO on medium heat in a non-stick pan. Saute chopped green onions for approximately 2 minutes. Add parsley, lemon juice, lemon zest, toasted pine nuts and cooked orzo. Saute for 3-4 minutes for flavors to combine and absorb into the orzo. Remove from heat.\nIn a large bowl, combine cucumber, green bell pepper, cherry tomatoes, red onion and pepperoncinis to orzo mixture. Additionally add crumbled feta cheese, red wine vinegar and remaining six tablespoons of EVOO. Mix well. Can be refrigerated or served immediately.",
    "analyzedInstructions": [
        {
            "name": "",
            "steps": [
                {
                    "number": 1,
                    "step": "Bring a pot of water to a rapid boil. Generously salt water and cook orzo until tender, approximately 7-9 minutes.",
                    "ingredients": [
                        {
                            "id": 14412,
                            "name": "water",
                            "localizedName": "water",
                            "image": "water.png"
                        },
                        {
                            "id": 10920420,
                            "name": "orzo",
                            "localizedName": "orzo",
                            "image": "orzo.jpg"
                        },
                        {
                            "id": 2047,
                            "name": "salt",
                            "localizedName": "salt",
                            "image": "salt.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404752,
                            "name": "pot",
                            "localizedName": "pot",
                            "image": "stock-pot.jpg"
                        }
                    ],
                    "length": {
                        "number": 9,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 2,
                    "step": "Drain and set aside.",
                    "ingredients": [],
                    "equipment": []
                },
                {
                    "number": 3,
                    "step": "While orzo is cooking, spread pine nuts on a baking sheet and toast lightly in oven on 400 degrees.",
                    "ingredients": [
                        {
                            "id": 12147,
                            "name": "pine nuts",
                            "localizedName": "pine nuts",
                            "image": "pine-nuts.png"
                        },
                        {
                            "id": 0,
                            "name": "spread",
                            "localizedName": "spread",
                            "image": ""
                        },
                        {
                            "id": 18070,
                            "name": "toast",
                            "localizedName": "toast",
                            "image": "toast"
                        },
                        {
                            "id": 10920420,
                            "name": "orzo",
                            "localizedName": "orzo",
                            "image": "orzo.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404727,
                            "name": "baking sheet",
                            "localizedName": "baking sheet",
                            "image": "baking-sheet.jpg"
                        },
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ]
                },
                {
                    "number": 4,
                    "step": "Remove from oven and set aside.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ]
                },
                {
                    "number": 5,
                    "step": "Heat two tablespoons of EVOO on medium heat in a non-stick pan.",
                    "ingredients": [
                        {
                            "id": 1034053,
                            "name": "extra virgin olive oil",
                            "localizedName": "extra virgin olive oil",
                            "image": "olive-oil.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404645,
                            "name": "frying pan",
                            "localizedName": "frying pan",
                            "image": "pan.png"
                        }
                    ]
                },
                {
                    "number": 6,
                    "step": "Saute chopped green onions for approximately 2 minutes.",
                    "ingredients": [
                        {
                            "id": 11291,
                            "name": "green onions",
                            "localizedName": "green onions",
                            "image": "spring-onions.jpg"
                        }
                    ],
                    "equipment": [],
                    "length": {
                        "number": 2,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 7,
                    "step": "Add parsley, lemon juice, lemon zest, toasted pine nuts and cooked orzo.",
                    "ingredients": [
                        {
                            "id": 10920421,
                            "name": "cooked orzo",
                            "localizedName": "cooked orzo",
                            "image": "orzo.jpg"
                        },
                        {
                            "id": 9152,
                            "name": "lemon juice",
                            "localizedName": "lemon juice",
                            "image": "lemon-juice.jpg"
                        },
                        {
                            "id": 9156,
                            "name": "lemon zest",
                            "localizedName": "lemon zest",
                            "image": "zest-lemon.jpg"
                        },
                        {
                            "id": 12147,
                            "name": "pine nuts",
                            "localizedName": "pine nuts",
                            "image": "pine-nuts.png"
                        },
                        {
                            "id": 11297,
                            "name": "parsley",
                            "localizedName": "parsley",
                            "image": "parsley.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 8,
                    "step": "Saute for 3-4 minutes for flavors to combine and absorb into the orzo.",
                    "ingredients": [
                        {
                            "id": 10920420,
                            "name": "orzo",
                            "localizedName": "orzo",
                            "image": "orzo.jpg"
                        }
                    ],
                    "equipment": [],
                    "length": {
                        "number": 4,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 9,
                    "step": "Remove from heat.",
                    "ingredients": [],
                    "equipment": []
                },
                {
                    "number": 10,
                    "step": "In a large bowl, combine cucumber, green bell pepper, cherry tomatoes, red onion and pepperoncinis to orzo mixture.",
                    "ingredients": [
                        {
                            "id": 11333,
                            "name": "green pepper",
                            "localizedName": "green pepper",
                            "image": "green-pepper.jpg"
                        },
                        {
                            "id": 10311529,
                            "name": "cherry tomato",
                            "localizedName": "cherry tomato",
                            "image": "cherry-tomatoes.png"
                        },
                        {
                            "id": 11976,
                            "name": "peperoncini",
                            "localizedName": "peperoncini",
                            "image": "pepperoncini.jpg"
                        },
                        {
                            "id": 10011282,
                            "name": "red onion",
                            "localizedName": "red onion",
                            "image": "red-onion.png"
                        },
                        {
                            "id": 11206,
                            "name": "cucumber",
                            "localizedName": "cucumber",
                            "image": "cucumber.jpg"
                        },
                        {
                            "id": 10920420,
                            "name": "orzo",
                            "localizedName": "orzo",
                            "image": "orzo.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        }
                    ]
                },
                {
                    "number": 11,
                    "step": "Additionally add crumbled feta cheese, red wine vinegar and remaining six tablespoons of EVOO.",
                    "ingredients": [
                        {
                            "id": 1022068,
                            "name": "red wine vinegar",
                            "localizedName": "red wine vinegar",
                            "image": "red-wine-vinegar.jpg"
                        },
                        {
                            "id": 1019,
                            "name": "feta cheese",
                            "localizedName": "feta cheese",
                            "image": "feta.png"
                        },
                        {
                            "id": 1034053,
                            "name": "extra virgin olive oil",
                            "localizedName": "extra virgin olive oil",
                            "image": "olive-oil.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 12,
                    "step": "Mix well. Can be refrigerated or served immediately.",
                    "ingredients": [],
                    "equipment": []
                }
            ]
        }
    ],
    "originalId": "null",
    "spoonacularSourceUrl": "https://spoonacular.com/mediterranean-orzo-salad-651426"
},
{
    "vegetarian": True,
    "vegan": True,
    "glutenFree": True,
    "dairyFree": True,
    "veryHealthy": False,
    "cheap": False,
    "veryPopular": False,
    "sustainable": False,
    "lowFodmap": False,
    "weightWatcherSmartPoints": 1,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 23,
    "healthScore": 2,
    "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
    "license": "CC BY 3.0",
    "sourceName": "Foodista",
    "pricePerServing": 20.08,
    "extendedIngredients": [
        {
            "id": 9277,
            "aisle": "null",
            "image": "null",
            "consistency": "SOLID",
            "name": "plantains",
            "nameClean": "null",
            "original": "2 plantains",
            "originalName": "plantains",
            "amount": 2.0,
            "unit": "",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 4053,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "olive-oil.jpg",
            "consistency": "LIQUID",
            "name": "olive oil",
            "nameClean": "olive oil",
            "original": "2 Tbs olive oil",
            "originalName": "olive oil",
            "amount": 2.0,
            "unit": "Tbs",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "Tbs",
                    "unitLong": "Tbs"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "Tbs",
                    "unitLong": "Tbs"
                }
            }
        },
        {
            "id": 1022020,
            "aisle": "Spices and Seasonings",
            "image": "garlic-powder.png",
            "consistency": "SOLID",
            "name": "garlic powder",
            "nameClean": "garlic powder",
            "original": "1 tsp garlic powder",
            "originalName": "garlic powder",
            "amount": 1.0,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                }
            }
        },
        {
            "id": 2028,
            "aisle": "Spices and Seasonings",
            "image": "paprika.jpg",
            "consistency": "SOLID",
            "name": "paprika",
            "nameClean": "paprika",
            "original": "1/2 tsp paprika",
            "originalName": "paprika",
            "amount": 0.5,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 1002014,
            "aisle": "Spices and Seasonings",
            "image": "ground-cumin.jpg",
            "consistency": "SOLID",
            "name": "cumin",
            "nameClean": "cumin",
            "original": "1/2 tsp cumin",
            "originalName": "cumin",
            "amount": 0.5,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 2031,
            "aisle": "Spices and Seasonings",
            "image": "chili-powder.jpg",
            "consistency": "SOLID",
            "name": "cayenne pepper",
            "nameClean": "ground cayenne pepper",
            "original": "1/4 tsp cayenne pepper",
            "originalName": "cayenne pepper",
            "amount": 0.25,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.25,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.25,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 2047,
            "aisle": "Spices and Seasonings",
            "image": "salt.jpg",
            "consistency": "SOLID",
            "name": "salt",
            "nameClean": "table salt",
            "original": "1/2 tsp salt",
            "originalName": "salt",
            "amount": 0.5,
            "unit": "tsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        }
    ],
    "id": 644218,
    "title": "Garlic & Spice Plantain Chips",
    "readyInMinutes": 45,
    "servings": 8,
    "sourceUrl": "https://www.foodista.com/recipe/4LR867R5/garlic-spice-plantain-chips",
    "image": "https://spoonacular.com/recipeImages/644218-556x370.jpg",
    "imageType": "jpg",
    "summary": "The recipe Garlic & Spice Plantain Chips can be made <b>in roughly roughly 45 minutes</b>. One serving contains <b>88 calories</b>, <b>1g of protein</b>, and <b>4g of fat</b>. For <b>20 cents per serving</b>, you get a side dish that serves 8. 23 people have made this recipe and would make it again. If you have cayenne pepper, paprika, garlic powder, and a few other ingredients on hand, you can make it. It is a good option if you're following a <b>gluten free, dairy free, lacto ovo vegetarian, and whole 30</b> diet. It is brought to you by Foodista. With a spoonacular <b>score of 34%</b>, this dish is not so outstanding. <a href=\"https://spoonacular.com/recipes/plantain-chips-150821\">Plantain Chips</a>, <a href=\"https://spoonacular.com/recipes/plantain-chips-salsa-588295\">Plantain chips & salsa</a>, and <a href=\"https://spoonacular.com/recipes/plantain-chips-sauce-148288\">Plantain Chips Sauce</a> are very similar to this recipe.",
    "cuisines": [],
    "dishTypes": [
        "side dish"
    ],
    "diets": [
        "gluten free",
        "dairy free",
        "paleolithic",
        "lacto ovo vegetarian",
        "primal",
        "whole 30",
        "vegan"
    ],
    "occasions": [],
    "winePairing": {},
    "instructions": "Preheat oven to 400F. Line a baking sheet with parchment paper or silicone mats.\nCut off both ends of the plantains. Make a cut along the entire length of a plantain, and peel off the skin.\nSlice each plantain into thin slices. Dont worry if the slices are not perfect.\nPlace the plantains in a medium-sized bowl. Mix in all the other ingredients and stir until everything is well incorporated.\nPlace the plantain slices on the baking sheets in a single layer.\nBake for about 15-20 minutes, flipping them at about the 8- or 9-minute mark. Because of the uneven heat distribution in my oven, I also like to swap the baking sheets between the top and bottom racks.\nRemove the chips from the oven when the edges turn into a nice golden brown color.",
    "analyzedInstructions": [
        {
            "name": "",
            "steps": [
                {
                    "number": 1,
                    "step": "Preheat oven to 400F. Line a baking sheet with parchment paper or silicone mats.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404770,
                            "name": "baking paper",
                            "localizedName": "baking paper",
                            "image": "baking-paper.jpg"
                        },
                        {
                            "id": 404727,
                            "name": "baking sheet",
                            "localizedName": "baking sheet",
                            "image": "baking-sheet.jpg"
                        },
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg",
                            "temperature": {
                                "number": 400.0,
                                "unit": "Fahrenheit"
                            }
                        }
                    ]
                },
                {
                    "number": 2,
                    "step": "Cut off both ends of the plantains. Make a cut along the entire length of a plantain, and peel off the skin.",
                    "ingredients": [
                        {
                            "id": 99295,
                            "name": "plantain",
                            "localizedName": "plantain",
                            "image": "plantains.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 3,
                    "step": "Slice each plantain into thin slices. Dont worry if the slices are not perfect.",
                    "ingredients": [
                        {
                            "id": 99295,
                            "name": "plantain",
                            "localizedName": "plantain",
                            "image": "plantains.jpg"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 4,
                    "step": "Place the plantains in a medium-sized bowl.",
                    "ingredients": [
                        {
                            "id": 99295,
                            "name": "plantain",
                            "localizedName": "plantain",
                            "image": "plantains.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        }
                    ]
                },
                {
                    "number": 5,
                    "step": "Mix in all the other ingredients and stir until everything is well incorporated.",
                    "ingredients": [],
                    "equipment": []
                },
                {
                    "number": 6,
                    "step": "Place the plantain slices on the baking sheets in a single layer.",
                    "ingredients": [
                        {
                            "id": 99295,
                            "name": "plantain",
                            "localizedName": "plantain",
                            "image": "plantains.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404727,
                            "name": "baking sheet",
                            "localizedName": "baking sheet",
                            "image": "baking-sheet.jpg"
                        }
                    ]
                },
                {
                    "number": 7,
                    "step": "Bake for about 15-20 minutes, flipping them at about the 8- or 9-minute mark. Because of the uneven heat distribution in my oven, I also like to swap the baking sheets between the top and bottom racks.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404727,
                            "name": "baking sheet",
                            "localizedName": "baking sheet",
                            "image": "baking-sheet.jpg"
                        },
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ],
                    "length": {
                        "number": 20,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 8,
                    "step": "Remove the chips from the oven when the edges turn into a nice golden brown color.",
                    "ingredients": [
                        {
                            "id": 11408,
                            "name": "french fries",
                            "localizedName": "french fries",
                            "image": "french-fries-isolated.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ]
                }
            ]
        }
    ],
    "originalId": "null",
    "spoonacularSourceUrl": "https://spoonacular.com/garlic-spice-plantain-chips-644218"
}
]


total = []
for key in data:
    # print(key["id"])
    #print(key["extendedIngredients"])
    
    for ingredient in key["extendedIngredients"]:
        name = (ingredient["name"])
        unit =(ingredient["unit"])
        amount =(ingredient["amount"])

        elements = {name: {'amount' : amount, "unit" : unit}}

        total.append(elements)
print(total)

# final = {}
# # Combine ingredients
# for ingredient in total:

#     key = ingredient.keys()

    # if final[key]:
    # try:
    #     # Check if units are the same
    #     # temp = final[key]
    #     if final[key]['unit'] == ingredient[key]['unit']:
    #         final[key]['amount'] = final[key]['amount'] + ingredient[key]['amount']
        
    # except KeyError:
    #     final[key] = ingredient


    # final.append(total)

# print(final)

#===================================================================
#each item in list is a dict of each meal_id
# for item in final:
#     print(item)

# total = []
# for key in data:
#     # print(key["id"])
#     #print(key["extendedIngredients"])
#     list = []
#     for i in key["extendedIngredients"]:
#         print(i["name"])
#         print(i["unit"])
#        amount =(i["amount"])

#         elements = {'name': name, 'amount' : amount, "unit" : unit}
#         list.append(elements)
#     total.append(list)
# # print(total)


# for item in total:
#     print(item)



# for recipe in data:
#     id = recipe["id"]
#     ingredients = recipe['extendedIngredients']
    
#     ingredients_list = []
#     for item in ingredients:
#         name = item['name']
#         amount = item['amount']
#         unit = item['unit']

#         elements = {'name': name, 'amount' : amount, "unit" : unit}
#         ingredients_list.append(elements)

# print(f'{ingredients_list}')
    # # print(instructions_recipe)

    # instructions_recipe = []

    # for recipe in data:
    #     id = recipe["id"]
    #     title = recipe['title']
    #     image = recipe["image"]
    #     instructions = recipe["instructions"]

    #     element = {'id': id, 'title': title, 'image': image, "instructions" : instructions}
    #     instructions_recipe.append(element) 

    # recipe_ids = [511728, 664411, 654944, 651426, 644218]

    
    # for recipe in data:
    #     ingredients = recipe['extendedIngredients']
        
    #     ingredients_list = []
    #     for item in ingredients:
    #         id = item["id"]
    #         name = item['name']
    #         amount = item['amount']
    #         unit = item['unit']

    #         elements = {'id': id, 'name': name, 'amount' : amount, "unit" : unit}
    #         ingredients_list.append(elements)

    # # # print(instructions_recipe)
    # print('*'*20)
    # print(ingredients_list)
