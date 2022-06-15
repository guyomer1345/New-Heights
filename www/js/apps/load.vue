<template>
    <div class="container" id="loading" v-if="is_loading">
        <div class="progress">
            <div class="indeterminate"></div>
        </div>
    </div>
    <div id="loading-bg"></div>
</template>

<script>
export default {
    name: "load-app",
    template: "#load-app",
    data() {
        return {
            is_loading: false,
        };
    }
};
</script>

<style>
#loading {
    z-index: 100;
}
#loading-bg{
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    position: absolute;
    z-index: 99;
    background: rgba(255, 255, 255, 0.5);
}
</style>
