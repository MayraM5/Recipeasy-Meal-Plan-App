// DELETE RECIPE FROM FAVORITES WHEN USER CLICK "DELETE" BUTTON
const deleteButton = document.querySelectorAll('.delete_fav');

for (const button of deleteButton) {
    button.addEventListener('click', (evt) => {
        const recipeId = button.id
        console.log(evt);
        const recipe_to_delete = {
            recipe_id : recipeId
        }
        // console.log(recipe_to_delete)
        fetch("/remove-fav", {
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