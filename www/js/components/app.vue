<template>
    <Loading ref="load"></Loading>
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
    mounted() {
        M.AutoInit();
        this.$router.push("/");
        this.$router.push("/action_progress");
    },
    methods: {
        wait_for_promise(promise) {
            if (typeof this.$refs.load === "undefined") {
                return;
            }
            this.$refs.load.is_loading = true;
            promise.finally(() => {
                this.$refs.load.is_loading = false;
            });
        },
    },
};
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
