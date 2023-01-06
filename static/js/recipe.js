
// SEARCH RECIPES => TITLE + IMAGE
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let recipeList = document.querySelector('#recipe')

search_btn.addEventListener("click", () => {
   // console.log(search_box.value)
    fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=${spoonacularApiKey}&query=${search_box.value}`)  
    .then((response) => response.json())
    .then((data) => {

        let html = "";
        if (data.results) {
            data.results.forEach(recipe => {
                html += `
                <div class = "recipe_name">
                    <h3><a href="/recipe-details-${recipe.id}">${recipe.title}</a></h3>
                
                <div class = "recipe_img">
                    <a href="/recipe-details-${recipe.id}"><img src = ${recipe.image}></a>
                </div>
                <div id="recipe_id" value= "${recipe.id}">
                    <button id="addToFav-${recipe.id}" onclick="AddtoFavorites(${recipe.id})">Favorite</button>
                    <button id="addToMealPlan-${recipe.id}" onclick="AddtoMealPlan(${recipe.id})">Add to Meal Plan</button>
                </div>
                `;
            });
            recipeList.classList.remove('notFound');
        } else{
            html = "Sorry, we didn't find any meals! Try again!";
            recipeList.classList.add('notFound');
        }

        recipeList.innerHTML = html;
        })
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
                            text: 'Recipe already exists in database',
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