<template>
    <loading-screen @mounted="load_mounted" ref="load">
    </loading-screen>
    <next-btn @next="next"></next-btn>
    <div id="app-contianer">
        <router-view @wait="wait_for_promise" v-slot="{ Component }">
            <component ref="current_app" :is="Component" />
        </router-view>
    </div>
</template>
<script>
// import laod_app from loadModule("./js/apps/components/next_btn.vue", options);
export default {
    name: "App",
    components: {
        "next-btn": Vue.defineAsyncComponent(() => loadModule("./js/apps/components/next_btn.vue", options)),
        "loading-screen": Vue.defineAsyncComponent(() => loadModule("./js/apps/load.vue", options)),
    },
    mounted() {
        M.AutoInit();
        loadModule("./js/apps/load.vue", options).then((a) => console.log("load.vue", a));
        this.$router.push("/select");
    },
    data() {
        return {
            load_promise: new Promise((res) => {
                this.__load_promise_resolve = res
            }),
        }
    },
    methods: {
        load_mounted() {
            this.__load_promise_resolve()
        },
        close() {
            pywebview.api.close()
        },
        next() {
            console.log("/select", this.$refs.current_app);
            this.$router.push("/install");
            console.log("/install", this.$refs.current_app);
        },
        wait_for_promise(promise) {
            this.load_promise.then(() => {
                console.log(this.$refs);
                this.$refs.load.is_loading = true;
                promise.finally(() => {
                    this.$refs.load.is_loading = false;
                })
            })
        },
    }
}
</script>
<style scoped>
#app-contianer {
    width: 100%;
    height: calc(100vh - 70px);
    overflow-y: scroll;
    
}
/* ===== Scrollbar CSS ===== */
  /* Firefox */
  * {
    scrollbar-width: auto;
    scrollbar-color: #3f3f3f #ffffff;
  }

  /* Chrome, Edge, and Safari */
  *::-webkit-scrollbar {
    width: 16px;
  }

  *::-webkit-scrollbar-track {
    background: #ffffff;
  }

  *::-webkit-scrollbar-thumb {
    background-color: #3f3f3f;
    border-radius: 10px;
    border: 3px solid #ffffff;
  }
</style>
