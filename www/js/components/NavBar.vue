<template>
    <div class="navbar-fixed">
        <nav class="yellow lighten-1">
            <div class="nav-wrapper">
                <div id="logo" class="left"></div>
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
<style scoped>
    #logo{
        height: 60px;
        width: 60px;
        background-image: url("logo.png");
        background-size: cover;
    }
</style>