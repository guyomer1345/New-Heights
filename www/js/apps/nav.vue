<template>
    <div class="navbar-fixed">
        <nav class="yellow lighten-1">
            <div class="nav-wrapper">
                <img src="logo.png" style="height: 100%" class="brand-logo left">
                <ul class="right">
                    <li><a href="#" @click="close"><i class="material-icons black-text">close</i></a></li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    mounted() {
        M.AutoInit();
    },
    methods: {
        close() {
            pywebview.api.close()
        }
    }
}
</script>
<style lang="">
    
</style>