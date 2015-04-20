$('#search').on('input', function() {
  var text = $("#search").val();
  if(text != "") {
    $.ajax({
		  url: "http://127.0.0.1:8000/search/" + text,
		  crossDomain:true,
		  method: "GET",
		  dataType: 'json',
		  success: function(data) { add(data); }
	  });
  }
  else {
    $("#result").empty();
  }
});

function add(data) {
  //alert("Response received");
  console.log(data);
  var result = $("#result");
  result.empty();
  for(var i=0; i<data.length; i++) {
    result.append('<a href="#" onClick="openDocument('+data[i][0]+');return false;">' + data[i][1] + '</a><br>');
    result.append('<span class="insight">' + data[i][2] + '</span><br>');
    //result.append("Lol<br>");
  }
}

function search() {
  var text = $("#search").val();
  //alert("Let's search " + text);
  $.ajax({
		url: "http://127.0.0.1:8000/search/" + text,
		crossDomain:true,
		method: "GET",
		dataType: 'json',
		success: function(data) { add(data); }
	});
}

function openDocument(id) {
  window.open('http://127.0.0.1:8000/document/' + id, id, 'width=300, height=300, scrollbars=1');
  //window.open('test.txt', 'newwindow', 'width=300, height=300, scrollbars=1');
}
