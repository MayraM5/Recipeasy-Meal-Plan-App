// testing api
let search_btn = document.querySelector("#searchbtn")
let search_box = document.querySelector("#search")
let show_recipe = document.querySelector("#search_result")

search_btn.addEventListener("click", () => {
    console.log(search_box.value)
    fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_box.value}&number=1`)
    .then((response) => response.json())
    .then((responseRecipe) => {
    console.log(responseRecipe.results[0].title)
    show_recipe.innerHTML = responseRecipe.results[0].title
    }) 

})


