// Load the Visualization API and the corechart package.
/*google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);
google.charts.setOnLoadCallback(proyecciones);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

  // Create the data table.
  var data = new google.visualization.DataTable();

  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Administradores', 1],
    ['Clientes', {{ ventar_por_clientes }}],
    ['Vendedores', {{ ventar_por_vendedores }}]
  ]);

  // Set chart options
  var options = {'title':'Reporte de Ventas',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
  chart.draw(data, options);

  var options = {'title':'Reporte de Ventas',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.BarChart(document.getElementById('chart'));
  chart.draw(data, options);

  
}
function proyecciones() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Clientes', 1],
    ['Administradores', 1],
    ['Vendedor', 5]
  ]);

  // Set chart options
  var options = {'title':'Ventas a lo largo del tiempo',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('ventas_por_mes'));
  chart.draw(data, options);

  var options = {'title':'Productos Estrella',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.BarChart(document.getElementById('productos_por_mes'));
  chart.draw(data, options);

  
}*/