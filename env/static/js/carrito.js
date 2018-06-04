function mostrar( obj ){
    var container = document.getElementById("describe") ;
    container.innerHTML = "valor del envio : " + obj[ obj.selectedIndex ].value ;
}