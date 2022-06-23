const { reactive, ref, createApp } = Vue;
const { createStore } = Vuex;
const { loadModule, version } = window["vue3-sfc-loader"];

const options = {
    moduleCache: {
        vue: Vue,
    },
    async getFile(url) {
        const res = await fetch(url);
        if (!res.ok) throw Object.assign(new Error(res.statusText + " " + url), { res });
        return {
            getContentData: (asBinary) => (asBinary ? res.arrayBuffer() : res.text()),
        };
    },
    compiledCache: {
        set(key, str) {
            for (;;) {
                try {
                    window.localStorage.setItem(key, str);
                    break;
                } catch (ex) {
                    window.localStorage.removeItem(window.localStorage.key(0));
                }
            }
        },
        get(key) {
            return window.localStorage.getItem(key);
        },
    },
    addStyle(textContent) {
        const style = Object.assign(document.createElement("style"), { textContent });
        const ref = document.head.getElementsByTagName("style")[0] || null;
        document.head.insertBefore(style, ref);
    },
};

function import_component(path) {
    return Vue.defineAsyncComponent(() => loadModule(path, options));
}
function import_app(path) {
    return () => loadModule(path, options);
}

const _modules = [
    Install,
    Welcome,
    Select,

    App,
    Load,
    NavBar,
    Navigation,
] = [
    import_app("./js/views/install.vue"),
    import_app("./js/views/welcome.vue"),
    import_app("./js/views/select.vue"),
    
    import_component("./js/components/app.vue"),
    import_component("./js/components/load.vue"),
    import_component("./js/components/NavBar.vue"),
    import_component("./js/components/Navigation.vue"),
];

const load_comonents = Promise.all([_modules]);

const load_document = new Promise((resolve) => {
    $(document).ready(() => resolve());
});

const load_pywebviw = new Promise((resolve) => {
    window.addEventListener("pywebviewready", () => resolve());
});

Promise.all([load_comonents, load_document, load_pywebviw]).then(() => {
    const routes = [
        { path: "/", component: Welcome},
        { path: "/select", component: Select },
        { path: "/install", component: Install },
    ];
    const router = VueRouter.createRouter({
        history: VueRouter.createWebHashHistory(),
        routes,
    });

    const app = createApp(App);
    const navbar = createApp(NavBar);

    app.component("Navigation", Navigation)
    app.component("Loading", Load)
    app.use(router);
    app.mount("#app");
    navbar.mount("#navbar");
});
