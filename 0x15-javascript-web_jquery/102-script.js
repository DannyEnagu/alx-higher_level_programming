$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
  const param = $('INPUT#language_code').val();
  $('INPUT#btn_translate').click(function () {
    $.get(url + param, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
