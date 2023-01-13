// SEARCH RECIPES => TITLE + IMAGE
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let recipeList = document.querySelector('#recipe')
let randomRecipe = document.querySelector('#random-recipes')

search_btn.addEventListener("click", () => {
   // console.log(search_box.value)
    fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=${spoonacularApiKey}&query=${search_box.value}`)  
    .then((response) => response.json())
    .then((data) => {
        console.log(data.result)

        let html = `<div class='row'>`;
        if (data.results) {    
            data.results.forEach(recipe => {
                html += `
                        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-xs-12">
                            <div class="card">
                                <a href="/recipe-details-${recipe.id}"><img src= ${recipe.image} alt="recipe image" class="card-img-top" class="recipe_image"></a>
                            <div class="card-body">
                                <h5 class="card-title"> ${recipe.title}</h5>
                                <div class="buttons">
                                    <div id="recipe_id" value= "${recipe.id}">
                                    <button class="add_to_meal_plan"  id="addToFav-${recipe.id}" onclick="AddtoFavorites(${recipe.id})">Favorite</button>
                                    <button class="add_to_fav" id="addToMealPlan-${recipe.id}" onclick="AddtoMealPlan(${recipe.id})">Add to Meal Plan</button>
                                </div>
                            </div>    
                            </div>
                        </div>
                    </div>
                `;             
            });

        } else{
            recipeList.innerHTML = "Sorry, we didn't find any meals! Try again!";
            recipeList.classList.add('notFound');
        }
        recipeList.innerHTML = html;
        })

        // Hide random recipes result
        randomRecipe.style.visibility = "hidden";
});


    ///ADD ID TO FAV ======= Click fav button => SENDING ID to server
    function AddtoFavorites(recipeId) { 
        console.log("clickButton")
        console.log(recipeId)
        const body = {recipe_Id: recipeId,}

        fetch("/api/fav-recipe", {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((responseJson) => {
                // console.log(responseJson)
                // Check the status of the response
                if (responseJson.status === "success") {
                    // Display a success message to the user
                    swal.fire({
                        title: 'Recipe saved successfully!',
                        icon: 'success',
                    });
                } else if (responseJson.status === "error") {
                    // Display an error message to the user
                    if (responseJson.reason === "duplicate") {
                        // Display an error message to the user
                        swal.fire({
                            title: 'Error saving recipe',
                            text: 'Recipe already exists in Favorites',
                            icon: 'error',
                        });
                    } else {
                    // Display a generic error message to the user
                        swal.fire({
                            title: 'Error saving recipe',
                            text: 'Please try again',
                            icon: 'error',
                        });
                    }
                }
            });
    }

    //ADD TO MEAL PLAN :
    function AddtoMealPlan(recipeId) { 
        console.log("clickButton")
        console.log(recipeId)
        const body = {recipe_Id: recipeId,}

        fetch("/api/meal-plan", {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((responseJson) => {
               // console.log(responseJson)
                // Check the status of the response
                if (responseJson.status === "success") {
                    // Display a success message to the user
                    swal.fire({
                        title: 'Recipe added to Meal Plan!',
                        icon: 'success',
                    });
                } else if (responseJson.status === "error") {
                    // Display an error message to the user
                    if (responseJson.reason === "duplicate") {
                        // Display an error message to the user
                        swal.fire({
                            title: 'Error adding recipe',
                            text: 'Recipe already exists in Meal Plan',
                            icon: 'error',
                        });
                    } else {
                    // Display a generic error message to the user
                        swal.fire({
                            title: 'Error adding recipe',
                            text: 'Please try again',
                            icon: 'error',
                        });
                    }
                }
            });
        }