$(document).ready(function () {
  $.ajax({
    method: 'GET',
    referrerPolicy: 'strict-origin-when-cross-origin',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (res) {
      $('DIV#hello').text(res.hello);
    }
  });
});
