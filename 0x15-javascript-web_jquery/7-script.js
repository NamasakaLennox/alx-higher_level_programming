$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (person) {
      $('DIV#character').text(person.name);
    }
  });
});
