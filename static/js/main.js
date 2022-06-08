const FORWARD = 1;
const BACKWARD = -1;
const APP_NAMES = ['7-Zip', 'Miniconda']
const ROUTES_NAMES = {
    download_route: 'download',
    install_route: 'install'
};

// const templateFunc =
//     (route_name, app_name) => `/${route_name}?name=${app_name}`;

function get_status_bar() {
    return document.getElementsByClassName('determinate').item(0);
}

function get_status_bar_width() {
    return get_status_bar().style.width;
}

function change_status_bar(direction, amount) {
    let width = get_status_bar_width();
    let widthInt = parseInt(width.substring(0,2));

    get_status_bar().style.width = widthInt + direction * amount + "%";
}

const download = app_name => {
    let download_url = ROUTES_NAMES.download_route;

    $.ajax({
        url: download_url,
        type: "get", //Use "PUT" for HTTP PUT methods
        dataType: 'json',
        data: {
            name : app_name,
        }
    })
    .done (function(data, textStatus, jqXHR) {
        change_status_bar(FORWARD, 10);
        alert("Success: " + data.msg);
        console.log(data)
    })
    .fail (function(jqXHR, textStatus, errorThrown) {
        alert("Error: " + jqXHR.responseText);
    });
}


$("#starter").click(() => {
    download(APP_NAMES[0]);
})
// $("#starter").click(function() {
//     $.ajax({
//         url: "/stage1",
//         type: "get", //Use "PUT" for HTTP PUT methods
//         dataType: 'json',
//         data: {
//             key : "value",
//         }
//     })
//     .done (function(data, textStatus, jqXHR) {
//         change_status_bar(FORWARD, 10);
//         alert("Success: " + data.msg);
//         console.log(data)
//     })
//     .fail (function(jqXHR, textStatus, errorThrown) {
//         alert("Error: " + jqXHR.responseText);
//     })
//     .always (function(jqXHROrData, textStatus, jqXHROrErrorThrown) {
//         alert("complete");
//     });
// });

