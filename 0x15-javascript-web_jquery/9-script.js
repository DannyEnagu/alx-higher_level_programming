$(function ()
  {
    url = 'https://fourtonfish.com/hellosalut/?lang=fr'
    $.get(url,
      function (data, textStatus) {
        console.log(data)
        $('DIV#hello').text(data);
      }
    );
  }
);
