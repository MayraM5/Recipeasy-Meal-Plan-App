
// SEARCH RECIPES => TITLE + IMAGE
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let mealList = document.querySelector('#meal')

// TO DO: How to hide apikey =========================================
search_btn.addEventListener("click", () => {
   // console.log(search_box.value)
    fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_box.value}`)  
    .then((response) => response.json())
    .then((data) => {

        let html = "";
        if (data.results) {
            data.results.forEach(meal => {
                html += `
                <div class = "meal_name">
                    <h3>${meal.title}</h3>
                
                <div class = "meal_img">
                    <img src = ${meal.image}>
                </div>
                <div id="meal_id" value= "${meal.id}">
                    <button id="addToFav-${meal.id}" onclick="AddtoFavorites(${meal.id})">Add to Favorites</button>
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
