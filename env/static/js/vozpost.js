if (annyang) {
  // Let's define our first command. First the text we expect, and then the function it should call
  var commands = {
    'Buscar *nombre': function(nombre) {
      document.getElementById('publicacion').value = nombre;
      document.getElementById('search_form').submit();
    }
  };

  // Add our commands to annyang
  annyang.addCommands(commands);

  //add our lenguage

  annyang.setLanguage('es-MX')

  // Start listening. You can call this here, or attach this call to an event, button, etc.
  annyang.start();
}
