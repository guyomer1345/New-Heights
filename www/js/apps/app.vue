<template>
    <loading-screen @mounted="load_mounted" ref="load">
    </loading-screen>
    <next-btn @next="next"></next-btn>
    <router-view @wait="wait_for_promise" v-slot="{ Component }">
        <component ref="current_app" :is="Component" />
    </router-view>
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
            console.log("next ", this.$refs);
            console.log("Current app", this.$router)
        },
        wait_for_promise(promise) {
            console.log("wait_for_promise", this.load_promise);
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
<style lang="">
    
</style>
