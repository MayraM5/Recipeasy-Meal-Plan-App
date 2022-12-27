
// SEARCH RECIPES => TITLE + IMAGE
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let recipeList = document.querySelector('#recipe')

// TO DO: How to hide apikey =========================================
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
                    <button id="addToFav-${recipe.id}" onclick="AddtoFavorites(${recipe.id})">Add to favorites</button>
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
                console.log(responseJson)
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
                console.log(responseJson)
            });
    }

