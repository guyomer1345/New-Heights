<template>
    <loading-screen ref="load"></loading-screen>
    <router-view @wait="wait_for_promise"></router-view>
</template>
<script>
export default {
    name: "App",
    components: {
        "loading-screen": Vue.defineAsyncComponent(() => loadModule("./js/apps/load.vue", options)),
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
</script>
<style lang="">
    
</style>