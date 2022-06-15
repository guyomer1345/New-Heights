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

const {createApp} = Vue

const select_app = {
    name: "select-app",
    template: "#select-app",
    emits: ['wait'],

    data() {
        return {
            minutes: 10,
            actions: [],

            loaded: false,
            is_changed: false,
        }
    },
    methods: {
        set_selection(value) {
            // this.installers.forEach(element => element.is_installed = value);
        },
    },
    watch: {
        installers(val){
            console.log(val)
            if (this.loaded){
                console.log(val)
                this.is_changed = true;
            }
        }
    },
    mounted() {
        M.AutoInit();
        if (this.loaded) {
            return;
        }
        pywebview.api.resize(500);
        let result = pywebview.api.get_actions().then(actions => {
            this.actions = actions
            this.loaded = true;
        });
        this.$emit('wait', result);
    }
}

const load_app = {
    name: "load-app",
    template: "#load-app",
    created() {
        setTimeout(() => {
            this.$router.push("/select");
        }, 1000)
    }
}

const main_app = {
    name: "App",
    data() {
        return {
            is_loading: true,
        };
    },
    mounted() {
        M.AutoInit();
        console.log(this)
        console.log("App")
        this.$router.push("/");
    },
    methods: {
        close() {
            pywebview.api.close()
        },
        wait_for_promise(promise) {
            console.log("@wait='wait_for_promise'")
            this.is_loading = true;
            promise.then(() => {
                this.is_loading = false;
            })
        },
    }
}

$(document).ready(function () {
    window.addEventListener('pywebviewready', () => {
        const routes = [
            {path: "/", component: select_app},
        ];

        const router = VueRouter.createRouter({
            history: VueRouter.createWebHashHistory(),
            routes,
        });

        const app = createApp(main_app);
        app.use(router);
        app.mount("#app");
    })
});