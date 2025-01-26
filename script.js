async function predictDiabetes() {
            
    const formData = {
        pregnancies: parseFloat(document.getElementById('pregnancies').value),
        glucoseLevel: parseFloat(document.getElementById('glucose').value),
        bloodPressure: parseFloat(document.getElementById('bloodPressure').value),
        skinthickness: parseFloat(document.getElementById('skinThickness').value),
        insulin: parseFloat(document.getElementById('insulin').value),
        bmi: parseFloat(document.getElementById('bmi').value),
        diaPedigreeFunc: parseFloat(document.getElementById('diabetesPedigreeFunction').value),
        age: parseFloat(document.getElementById('age').value)
    };
    const url = "http://127.0.0.1:5000/predict" ;

    try{
        const res = await fetch(url, {method: "POST",headers: {"Content-Type": "application/json",},body: JSON.stringify(formData),});
        const result = await res.json();
        if (res.ok){
            if (result.isDiabetic == 1){
                // alert("Person is diabetic");
                document.getElementById("result").style.backgroundColor = "#f44336";
                document.getElementById("text").innerHTML = "Person is diabetic";
            }else{
                // alert("Person is not diabetic")
                document.getElementById("result").style.backgroundColor = "#4caf50";
                document.getElementById("text").innerHTML = "Person is not diabetic";
            }
        }else{
            alert(`Something went wrong ${result.msg}`)
        }
        
    }catch (err){
        alert(`Something went wrong ${err}`)
    }

}


