$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (films) {
      $.each(films.results, function (i, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
