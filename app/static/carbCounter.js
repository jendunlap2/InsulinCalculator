

console.log("Carb Counter")


const getFoodAPI = async function(foodInput){
    let response = await fetch(`https://api.nal.usda.gov/fdc/v1/foods/search?api_key=LRMO7vMHZXvFDOBGxRjjPHRQJCgnebL4Tka5Te5T&query=${foodInput}`);
    let data = await response();
    console.log(data)
    return await data
}

const foodForm = document.getElementById('foodForm');

function addToFoodTable(food){
    let foodTable = document.querySelector("#FoodTable");
    let liEl = document.createElement('li');
    liEl.innerText = `${food.data} Test`
    foodTable.append(liEl);
}

foodForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    let foodInput = e.target.foodInput.foods.description;
    console.log(foodInput);
    let food = await getFoodAPI(foodInput);
    console.log(results);
    addToFoodTable(food)
})