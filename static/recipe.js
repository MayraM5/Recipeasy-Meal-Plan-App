// testing api
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let mealList = document.querySelector('#meal')
// TO DO: How to hide apikey 
search_btn.addEventListener("click", () => {
    console.log(search_box.value)
    fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_box.value}`)  
    .then((response) => response.json())
    .then((data) => {

        let html = "";
        if (data.results) {
            data.results.forEach(meal => {
                html += `
                <div class = "meal_item" data_id = "${meal.id}">
                
                <div class = "meal_img">
                    <img src = ${meal.image}>
                </div>

                <div class = "meal_name">
                    <h3>${meal.title}</h3>
                    <a href= "/recipe/${meal.id}" class = "save_btn">Add to Favorite</a>

                    <a href= "#PENDING" class = "save_btn">Add to Meal plan</a></div>
                </div>
                `;
            });
            mealList.classList.remove('notFound');
        } else{
            html = "Sorry, we didn't find any meal! Try again!";
            mealList.classList.add('notFound');
        }

        mealList.innerHTML = html;
    });
    })
                
    // console.log(data.results[0].title)
    // show_recipe.innerHTML = data.results[0].title


// need to figure out how to click on add fav or MP and save into db 
// need to add see recipe when click on title or img ==> see recipe
