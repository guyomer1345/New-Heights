<template>
    <div v-if="is_loading">
        <div class="container" id="loading">
            <div class="progress">
                <div class="indeterminate"></div>
            </div>
        </div>
        <div id="loading-bg"></div>
    </div>
</template>

<script>
export default {
    name: "load_app",
    emits:[
        "mounted"
    ],
    data() {
        return {
            is_loading: false,
        };
    },
    mounted() {
        console.log("Loading screen is mounted");
        this.$emit('mounted')
    },
};
</script>

<style>
#loading {
    z-index: 100;
}

#loading-bg {
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    position: absolute;
    z-index: 99;
    background: rgba(255, 255, 255, 0.5);
}
</style>
