
// SEARCH RECIPES => TITLE + IMAGE
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let mealList = document.querySelector('#meal')

// TO DO: How to hide apikey =========================================
search_btn.addEventListener("click", () => {
   // console.log(search_box.value)
    fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=${spoonacularApiKey}&query=${search_box.value}`)  
    .then((response) => response.json())
    .then((data) => {

        let html = "";
        if (data.results) {
            data.results.forEach(meal => {
                html += `
                <div class = "meal_name">
                    <h3><a href="/recipe-details-${meal.id}">${meal.title}</a></h3>
                
                <div class = "meal_img">
                    <a href="/recipe-details-${meal.id}"><img src = ${meal.image}></a>
                </div>
                <div id="meal_id" value= "${meal.id}">
                    <button id="addToFav-${meal.id}" onclick="AddtoFavorites(${meal.id})">Add to favorites</button>
                    <button id="addToMealPlan-${meal.id}" onclick="AddtoMealPlan(${meal.id})">Add to Meal Plan</button>
                </div>
                `;
            });
            mealList.classList.remove('notFound');
        } else{
            html = "Sorry, we didn't find any meals! Try again!";
            mealList.classList.add('notFound');
        }

        mealList.innerHTML = html;
    });
    })

    ///ADD ID TO FAV ======= Click fav button => SENDING ID to server
    function AddtoFavorites(mealId) { 
        console.log("clickButton")
        console.log(mealId)
        const body = {meal_Id: mealId,}

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
    function AddtoMealPlan(mealplanId) { 
        console.log("clickButton")
        console.log(mealplanId)
        const body = {meal_plan_Id: mealplanId,}

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

    // //SEND RECIPE ID TO DISPLAY DETAILS:
    // function SeeRecipe(recipeId) { 
    //     console.log("clickButton")
    //     console.log(recipeId)
    //     const body = {recipe_Id: recipeId,}

    //     fetch("/recipe-details", {
    //         // method: 'POST',
    //         method: 'GET',
    //         // body: JSON.stringify(body),
    //         // headers: {
    //         //     "Content-Type": "application/json",
    //         // },
    //     })
    //         .then((response) => response.json())
    //         .then((recipIdJson) => {
    //             console.log(recipIdJson)
    //         });
    // }
