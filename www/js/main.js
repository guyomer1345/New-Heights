const FORWARD = 1;
const BACKWARD = -1;
const APP_NAMES = ['7-Zip', 'Miniconda']
const ROUTES_NAMES = {
    download_route: 'download',
    install_route: 'install'
};

const {createApp} = Vue

const main_app = {
    name: "App",
    components: {
        "loading-screen": Vue.defineAsyncComponent(() => loadModule("./js/apps/load.vue", options)),
        "navigation-bar": Vue.defineAsyncComponent(() => loadModule("./js/apps/nav.vue", options))
    },
    mounted() {
        M.AutoInit();
        this.$router.push("/install");
    },
    methods: {
        close() {
            pywebview.api.close()
        },
        wait_for_promise(promise) {
            this.$refs.load.is_loading = true;
            promise.finally(() => {
                this.$refs.load.is_loading = false;
            })
        },
    }
}
const { loadModule, version } = window["vue3-sfc-loader"];
const options = {
    moduleCache: {
      vue: Vue
    },
    async getFile(url) {
      
      const res = await fetch(url);
      if ( !res.ok )
        throw Object.assign(new Error(res.statusText + ' ' + url), { res });
      return {
        getContentData: asBinary => asBinary ? res.arrayBuffer() : res.text(),
      }
    },
    addStyle(textContent) {

      const style = Object.assign(document.createElement('style'), { textContent });
      const ref = document.head.getElementsByTagName('style')[0] || null;
      document.head.insertBefore(style, ref);
    },
  }
  
$(document).ready(function () {
    window.addEventListener('pywebviewready', () => {
        const routes = [
            {path: "/select", component: () => loadModule("./js/apps/select.vue", options)},
            {path: "/install", component: () => loadModule("./js/apps/install.vue", options)},
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