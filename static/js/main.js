const FORWARD = 1;
const BACKWARD = -1;
const APP_NAMES = ['7-Zip', 'Miniconda']
const ROUTES_NAMES = {
    download_route: 'download',
    install_route: 'install'
};

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
        get_action_class(action){
            console.log(action)
            if (action.selected === 'install'){
                return 'remove'
            }
            if (action.selected === 'remove'){
                return 'install'
            }
            if (action.actions.includes('remove')){
                return 'remove'
            }
            if (action.actions.includes('install')){
                return 'install'
            }
            return ''
        },
        set_selection(value) {
            this.actions.forEach(action => action.selected = value);
        },
    },
    watch: {
        installers(val){
            if (this.loaded){
                this.is_changed = true;
            }
        }
    },
    mounted() {
        M.AutoInit();
        if (this.loaded) {
            return;
        }
        pywebview.api.resize(800);
        let result = pywebview.api.get_actions().then(actions => {
            actions.forEach(action => action.selected = "")
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
        this.$router.push("/");
    },
    methods: {
        close() {
            pywebview.api.close()
        },
        wait_for_promise(promise) {
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