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

function GetElementInsideContainer(containerID, childID) {
  var elm = document.getElementById(childID);
  var parent = elm ? elm.parentNode : {};
  return (parent.id && parent.id === containerID) ? elm : {};
}

function duplicate(desc, img, link, title) {
  var clone = original.cloneNode(true); // "deep" clone
  // clone.id = "duplicater" + ++i;
  var id = "duplicater" + ++i;
  clone.id = id;
  var desc =  
  original.parentNode.appendChild(clone);
}
$(function() {
    $('a#process_input').bind('click', function() {
      $.getJSON('/background_process', {
        interests: $('input[name="interests"]').val(),
      }, function(data) {

        var result_div = document.getElementById("results"); 
        var template = document.getElementById("template");
        console.log(data.result)
        for (j = 0; j < data.result.length; j++){
          var clone = template.cloneNode(true);
          id = 'result' + j;
          clone.id = id;
          clone.classList.remove('template');
          result_div.appendChild(clone)
          console.log(document.getElementsByClassName('desc')[1])
          document.getElementsByClassName('desc')[1].id = 'desc' + j
          document.getElementsByClassName('link')[1].id = 'link' + j
          document.getElementsByClassName('img')[1].id = 'img' + j
          document.getElementsByClassName('title')[1].id = 'title' + j
          document.getElementsByClassName('desc')[1].classList.remove('desc')
          document.getElementsByClassName('link')[1].classList.remove('link')
          document.getElementsByClassName('img')[1].classList.remove('img')
          document.getElementsByClassName('title')[1].classList.remove('title')
          $("#desc" + j).text(data.result[j][0]);
          $("#link" + j).prop('href', data.result[j][2])
          $("#img" + j).prop('src', data.result[j][1])
          $("#title" + j).text(data.result[j][3])
        }
      });
      return false;
    });
  });
