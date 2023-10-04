const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();

    $.getJSON(url + language, function (res) {
      $('#hello').text(res.hello);
    });
  });
});
