// // testing api
// SEARCH RECIPES => TITLE + IMAGE
let search_btn = document.querySelector("#search_btn")
let search_box = document.querySelector("#search_input")
let show_recipe = document.querySelector("#search_result")
let mealList = document.querySelector('#meal')
// TO DO: How to hide apikey 
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
            html = "Sorry, we didn't find any meal! Try again!";
            mealList.classList.add('notFound');
        }

        mealList.innerHTML = html;
    });
    })
    ///ADDING ID TO FAV ======= Click fav button => SENDING ID to server
    function AddtoFavorites(mealId) { 
        console.log("clickButton")
        console.log(mealId)
        const body = {meal_Id: mealId,}

        fetch("/api/recipe", {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((responseJson) => {
                console.log(responseJson)
                // alert(responseJson.status);
            });
    }

    // document.querySelector("#addToFav").addEventListener("click", (event) => {
    //     event.preventDefault();

    //     const mealId = document.querySelector('#meal_id')
    //     console.log(mealId)

    //     fetch("/api/recipe", {
    //         method: 'POST',
    //         body: JSON.stringify(mealId),
    //         headers: {
    //             "Content-Type": "application/json",
    //         },
    //     })
    //         .then((response) => response.json())
    //         .then((responseJson) => {
    //             alert(responseJson.status);
    //         });
    // });


//     //////////////////////
                
    // console.log(data.results[0].title)
    // show_recipe.innerHTML = data.results[0].title


// need to figure out how to click on add fav or MP and save into db 
// need to add see recipe when click on title or img ==> see recipe

//////////////////////////////TRYING SOMETHING SIMILAR BUT HIDING APIKEY
//sending info to back end to search 
// let search_btn = document.querySelector("#search_btn")
// let searchInput = document.querySelector('#search_input')

// search_btn.addEventListener("click", async e => {
//     e.preventDefault()   

//     let cuisineName = searchInput.value
//     let response = fetch('/api/users', {
//         method: 'POST',
//         headers: {
//             contentType: 'application/json'
//         },
//         body: JSON.stringify({
//             cuisineName,
//         })
//     })

//     let data = await response.json
//     console.log(data)

////////////////////////////////////////////////////////////////////////////////



    // let cuisineName = searchInput.value
    // let response = fetch('/api/users', {
    //     method: 'POST',
    //     headers: {
    //         contentType: 'application/json'
    //     },
    //     body: JSON.stringify({
    //         cuisineName,
    //     })
    // })

    // let data = await response.json
    // console.log(data)

//     fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_box.value}`)  
// //     .then((response) => response.json())
//     .then((data) => {

// console.log(searchInput)