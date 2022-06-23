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

function import_module(path) {
    return Vue.defineAsyncComponent(() => loadModule(path, options));
}

const _modules = ([
    App,
    Install,
    Load,
    Nav,
    Select,
    Navigation,
    Welcome
] = [
    import_module("./js/apps/app.vue"),
    import_module("./js/apps/install.vue"),
    import_module("./js/apps/load.vue"),
    import_module("./js/apps/nav.vue"),
    import_module("./js/apps/select.vue"),
    import_module("./js/apps/Navigation.vue"),
    import_module("./js/apps/welcome.vue"),
]);

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
    const navbar = createApp(Nav);

    app.component("Navigation", Navigation)
    app.component("Loading", Load)
    app.use(router);
    app.mount("#app");
    navbar.mount("#navbar");
});
