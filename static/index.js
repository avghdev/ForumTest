function send(endpoint) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', endpoint);

    xhr.onreadystatechange = () => {
        if (xhr.status == 200 && xhr.readyState == 4) {
            $("html").html(xhr.response);
        }
    }

    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "name": $("#name").val(),
        "subject": $("#subject").val(),
        "post": $("#para").val()
    }));
}