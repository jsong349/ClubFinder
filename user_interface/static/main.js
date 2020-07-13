// var button = document.getElementsByClassName("submit_button");
// button[0].addEventListener("click", getResults);


// function getResults(){
//     var degree = document.getElementById("degree").value;
//     var interests = document.getElementById("interests").value;
//     var skills = document.getElementById("skills").value;
//     console.log(degree, interests, skills);
// }

// const myForm = document.getElementById('myForm');
// console.log(myForm)
// myForm.addEventListener('submit', function (e) {
//     e.preventDefault();
//     const formData = new FormData(this);
//     fetch('info.php', {
//         method: 'post',
//         body: formData 
//     }).then(function (response) {
//          return response.text();
//     }).then(function (text) {
//         console.log(text)
//     }).catch(function (error) {
//         console.error(error);
//     })
// });

$(function() {
    $('a#process_input').bind('click', function() {
      $.getJSON('/background_process', {
        interests: $('input[name="interests"]').val(),
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });
