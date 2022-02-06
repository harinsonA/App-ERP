function messages_error(object) {
    let html = '<ul>';
    if (typeof(object) === 'object') {
        $.each(object, function (key, value) {
            html += '<li>'+key+': '+ value +'</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>'+object+'</p>'
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error',
    })
}