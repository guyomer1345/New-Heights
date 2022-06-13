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
    let widthInt = parseInt(width.substring(0, 2));

    get_status_bar().style.width = widthInt + direction * amount + "%";
}

const download = app_name => {
    let download_url = ROUTES_NAMES.download_route;

    $.ajax({
        url: download_url,
        type: "get", //Use "PUT" for HTTP PUT methods
        dataType: 'json',
        data: {
            name: app_name,
        }
    })
        .done(function (data, textStatus, jqXHR) {
            change_status_bar(FORWARD, 10);
            alert("Success: " + data.msg);
            console.log(data)
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
            alert("Error: " + jqXHR.responseText);
        });
}

const install = app_name => {
    let install_url = ROUTES_NAMES.install_route;

    $.ajax({
        url: install_url,
        type: "get", //Use "PUT" for HTTP PUT methods
        dataType: 'json',
        data: {
            name: app_name,
        }
    })
        .done(function (data, textStatus, jqXHR) {
            change_status_bar(FORWARD, 10);
            alert("Success: " + data.msg);
            console.log(data)
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
            alert("Error: " + jqXHR.responseText);
        });
}

const {createApp, Vue} = Vue

const selection_app = createApp({
    data() {
        return {
            is_active: false,
            minutes: 10,
            installers: []
        }
    },
    mounted() {
        pywebview.api.get_status().then(installers => {
            console.log(installers)
            this.installers = installers
        });
    }
})

const loading_app = createApp({
    data() {
        return {
            is_active: true,
        }
    },
    mounted() {
        setTimeout(() => {
            selection_app.is_active = true;
            this.is_active = false;
        }, 1000)
    }
})

$(document).ready(function () {
    window.addEventListener('pywebviewready', function () {
        new Vue({
            el: "main",
            component:{
                'selection-app': selection_app,
                'loader-app': loading_app,
            }
        })
        // loading_app.mount('#loading')
        // selection_app.mount('#selection')
    })
});
//
// $("#starter").click(() => {
//     pywebview.api.close()
//     download(APP_NAMES[1]);
//     install(APP_NAMES[1]);
// })
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

