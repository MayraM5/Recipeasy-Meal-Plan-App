
//ADD INGREDIENT DATA TO RECIPE

function addRow() {
    const table = document.getElementById('ingredients-table');
    const row = table.insertRow();
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    const cell3 = row.insertCell(2);
    const cell4 = row.insertCell(3);
    const cell5 = row.insertCell(4);
    cell1.innerHTML = '<input type="text" name="ingredient" placeholder="Enter your ingredient name" size="25" required>';
    cell2.innerHTML = '<select name="unit"><option value=""></option><option value="tsp">teaspoon</option><option value="tbsp">tablespoon</option>\
                      <option value="cup">cup</option><option value="oz">ounce</option><option value="lb">pound</option>\
                      <option value="servings">serving</option><option value="container">container</option></select>';
    cell3.innerHTML = '<input type="number" name="quantity" step="0.01" required>';
    cell4.innerHTML = '<select name="category" required><option value="Oil, Vinegar, Salad Dressing">Oil, Vinegar, Salad Dressing</option>\
                      <option value="Refrigerated">Refrigerated</option><option value="Pasta and Rice">Pasta and Rice</option>\
                      <option value="Spices and Seasonings">Spices and Seasonings</option>\
                      <option value="Milk, Eggs, Other Dairy">Milk, Eggs, Other Dairy</option><option value="Meat">Meat</option>\
                      <option value="Produce">Produce</option><option value="Seafood">Seafood</option><option value="Cheese">Cheese</option>\
                      <option value="Other">Other</option><select> ';
    cell5.innerHTML = '<button type="button" onclick="removeRow(this)">Remove</button>';
  }
  
  function removeRow(button) {
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
  }

// DELETE RECIPE FROM COOCKBOOK
const deleteButton = document.querySelectorAll('.delete_recipe');

for (const button of deleteButton) {
    button.addEventListener('click', (evt) => {
        const recipeId = button.id
        console.log(evt);
        const recipe_to_delete = {
            recipe_id : recipeId
        }
        // console.log(recipe_to_delete)
        fetch("/remove-recipe", {
            method: 'POST',
            body: JSON.stringify(recipe_to_delete),
            headers: {
                "Content-Type": "application/json",   
            },
        })
            .then((Response) => Response.json())
            .then((recipeJson) => {
                console.log(recipeJson)
        });

        // Remove HTML for this recipe
        let el = document.getElementById('div_' + recipeId);
        el.parentNode.removeChild(el);

    })
}

// ADD RECIPE TO MEAL PLAN
const addRecipe = document.querySelectorAll('.add_to_meal_plan');

for (const button of addRecipe) {
    button.addEventListener('click', (evt) => {
        const recipe_id = button.id
        console.log(evt);
        const recipeId = {
            recipe_Id : recipe_id
        }
        // console.log(recipe_to_delete)
        fetch("/api/meal-plan", {
            method: 'POST',
            body: JSON.stringify(recipeId),
            headers: {
                "Content-Type": "application/json",   
            },
        })
            .then((Response) => Response.json())
            .then((recipeJson) => {
                console.log(recipeJson)
        });

    })
}
