function addRow() {
    const table = document.getElementById('ingredients-table');
    const row = table.insertRow();
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    const cell3 = row.insertCell(2);
    const cell4 = row.insertCell(3);
    const cell5 = row.insertCell(4);
    cell1.innerHTML = '<input type="text" name="ingredient">';
    cell2.innerHTML = '<select name="unit"><option value="tsp">teaspoon</option><option value="tbsp">tablespoon</option>\
                      <option value="cup">cup</option><option value="oz">ounce</option><option value="lb">pound</option>\
                      <option value="container">container</option><option value="other">unit</option></select>';
    cell3.innerHTML = '<input type="number" name="quantity">';
    cell4.innerHTML = '<select name="category"><option value="Oil, Vinegar, Salad Dressing">Oil, Vinegar, Salad Dressing</option>\
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
  
// //Get data from form

// const form = document.getElementById('recipe-form');
// form.addEventListener('submit', function(event) {
//   event.preventDefault();

//   const ingredients = [];
//   const inputs = document.querySelectorAll('#ingredients-table input');
//   // const inputs = form.getElementsByTagName('input');
//   for (let i = 0; i < inputs.length; i += 3) {
//     const ingredient = inputs[i].value;
//   if (inputs.length > i + 1) {
//     const unit = inputs[i + 1].value;
//     // const unit = inputs[i + 1].value;
//     const quantity = inputs[i + 2].value;
//     ingredients.push({ ingredient, unit, quantity });
//   }
// }

//   // create a new Cloudinary instance
//   const cl = cloudinary.Cloudinary.new({ cloud_name: 'dhyrymmf4' });

//   // upload the selected image file to Cloudinary
//   const fileInput = document.getElementById('image');
//   cl.uploader.upload(fileInput.files[0], function(error, result) {
//     if (error) {
//       console.error(error);
//     } else {
//       // the image was uploaded successfully, and the result object
//       // contains information about the uploaded image
//       console.log(result);

//       // get the URL of the uploaded image
//       const imageUrl = result.url;
//     }

//   const name = form.elements.name.value;
//   const instructions = form.elements.instructions.value;

//   const data = { name, imageUrl, instructions, ingredients };

//   // send the data to the Flask app using an AJAX request
//   const xhr = new XMLHttpRequest();
//   xhr.open('POST', '/save-recipe');
//   xhr.setRequestHeader('Content-Type', 'application/json');
//   xhr.send(JSON.stringify(data));
// });
// });