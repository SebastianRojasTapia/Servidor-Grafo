function Init(){
  cambiar();
  validar();
}

function cambiar(){
  var pdrs = document.getElementById('file-upload').files[0].name;
  document.getElementById('info').innerHTML = pdrs;
}

function validar(){
  var archivo =  document.getElementById('file-upload');
  var archivoRuta = archivo.value;
  var extPermitidas = /(.csv|.json|.xls)$/i;
  if(!extPermitidas.exec(archivoRuta)){
    alert('Solo acepta Archivos (CSV - JSON - XLS).')
    archivo.value='';
    return false;
  }
}