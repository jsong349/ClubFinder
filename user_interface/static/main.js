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

console.log("Startin")
$(function() {
    $('a#process_input').bind('click', function() {
      $.getJSON('/background_process', {
        interests: $('input[name="interests"]').val(),
      }, function(data) {
        var desc = data.result[0][0]
        var link = data.result[0][2]
        var img = data.result[0][1]
        $("#desc").text(desc);
        $("#link").prop('href', link)
        console.log(img)
        $("#img").prop('src', img)
        // console.log(link)
        // console.log(title)
        // console.log(desc)
      });
      return false;
    });
  });
