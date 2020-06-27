var button = document.getElementsByClassName("button");
button[0].addEventListener("click", getResults);


function getResults(){
    var degree = document.getElementById("degree").value;
    var interests = document.getElementById("interests").value;
    var skills = document.getElementById("skills").value;
    console.log(degree, interests, skills);
}