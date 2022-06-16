const { createApp } = Vue;
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
    addStyle(textContent) {
        const style = Object.assign(document.createElement("style"), { textContent });
        const ref = document.head.getElementsByTagName("style")[0] || null;
        document.head.insertBefore(style, ref);
    },
};

$(document).ready(() => {
    window.addEventListener("pywebviewready", () => {
        const routes = [
            { path: "/select", component: () => loadModule("./js/apps/select.vue", options) },
            { path: "/install", component: () => loadModule("./js/apps/install.vue", options) },
        ];
        const router = VueRouter.createRouter({
            history: VueRouter.createWebHashHistory(),
            routes,
        });

        const app = createApp(Vue.defineAsyncComponent(() => loadModule("./js/apps/app.vue", options)));
        const navbar = createApp(Vue.defineAsyncComponent(() => loadModule("./js/apps/nav.vue", options)));
        app.use(router);
        navbar.mount("#navbar")
        app.mount("#app");
    });
});
