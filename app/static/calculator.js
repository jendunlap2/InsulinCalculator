//********** Insulin Calculator ********** //

console.log('Insulin Calculator')

function calculateTotal()
{
    carbCount = document.getElementById("carbCount").value
    currentBG = document.getElementById("currentBG").value

    var e = document.getElementById("meal");
    var meal_id = e.value;

    var breakfast_insulin = document.getElementById("bfastInsulin").value
    var breakfast_carb = document.getElementById("bfastCarb").value

    var lunch_insulin = document.getElementById("lunchInsulin").value
    var lunch_carb = document.getElementById("lunchCarb").value

    var dinner_insulin = document.getElementById("dinnerInsulin").value
    var dinner_carb = document.getElementById("dinnerCarb").value

    var c_150_199 = document.getElementById("c_150_199").value
    var c_200_249 = document.getElementById("c_200_249").value
    var c_250_299 = document.getElementById("c_250_299").value
    var c_300_349 = document.getElementById("c_300_349").value
    var c_350_399 = document.getElementById("c_350_399").value
    var c_400 = document.getElementById("c_400").value
    

    // Find number of insulin units based on carbCount and user ratio 
    if (meal_id == 1){
        meal_insulinDose = carbCount / (breakfast_carb / breakfast_insulin);
    } else if (meal_id == 2){
        meal_insulinDose = carbCount / (lunch_carb / lunch_insulin);
    } else if (meal_id == 3){
        meal_insulinDose = carbCount / (dinner_carb / dinner_insulin);
    }

    var insulinDose = meal_insulinDose

    // Check user current BG for 150 or over, and add corresponding correction factor to insulin dose total
    if ((currentBG >= 150) && (currentBG <= 199)){
        insulinDose = +meal_insulinDose + +c_150_199;
    }
    else if ((currentBG >= 200) && (currentBG <= 249)){
        insulinDose = +meal_insulinDose + +c_200_249;
    }
    else if ((currentBG >= 250) && (currentBG <= 299)){
        insulinDose = +meal_insulinDose + +c_250_299;
    }
    else if ((currentBG >= 300) && (currentBG <= 349)){
        insulinDose = +meal_insulinDose + +c_300_349;
    }
    else if ((currentBG >= 350) && (currentBG <= 399)){
        insulinDose = +meal_insulinDose + +c_350_399;
    }
    else if (currentBG >= 400){
        insulinDose = +meal_insulinDose + +c_400;
    }
    
    insulinDoseDislay = insulinDose.toFixed(1);
    
    // *** DISPLAY RESULTS *** //
    document.getElementById('insulinTotal').innerHTML = `${insulinDoseDislay} total units insulin`;
    // document.getElementById('mealInsulinTotal').innerHTML = `(${meal_id} units for meal + ${breakfast_carb} units for correction)`;


}

 
    

//     // Print Results using Bootstrap Card class
//     document.getElementById("insulinCard").innerHTML = "";

//     let insulinCard = document.querySelector('#insulinCard');
    
//     insulinCard.classList.add('card')
//     insulinCard.style.width = '18rem'

//     let cardBody = document.createElement('div')
//     cardBody.classList.add('card-body')
//     insulinCard.append(cardBody);

//     let resultHeading = document.createElement('h5')
//     resultHeading.classList.add('card-title')
//     resultHeading.innerText = `${insulinDose} units insulin`
//     cardBody.append(resultHeading)
    
//     let cardText = document.createElement('p')
//     cardText.classList.add('card-text')
//     cardText.innerText = `Takes account of carbs and any correction if needed`
//     cardBody.append(cardText)



// }

// insulinForm.addEventListener('submit', async (e) => {
//     e.preventDefault();
//     let carbCount = e.target.carbCount.value;
//     console.log(carbCount);
//     let currentBG = e.target.currentBG.value;
//     console.log(currentBG);
//     let meal = e.target.meal.value;
//     console.log(meal);

//     let results = await getQuantities(carbCount, currentBG, meal);
//     console.log(results);
//     generateResults(forecast)
// })