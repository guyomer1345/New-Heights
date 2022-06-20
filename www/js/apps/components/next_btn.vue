<template>
    <div class="fixed-action-btn">
        <a 
        @click="this.$emit('next')"
        class="btn-floating btn-large waves-green">
            <i class="large material-icons">navigate_next</i>
        </a>
        <ul>
            <li @click="set_selection('install')">
                <a class="btn-floating cyan darken-1"><i class="material-icons">select_all</i></a>
            </li>
            <li @click="set_selection('remove')">
                <a class="btn-floating orange darken-1"><i class="material-icons">clear_all</i></a>
            </li>
        </ul>
    </div>
</template>
<script>
export default {
    emit:[
        "next",
        "previous",
        "wait",
    ],
    mounted() {
        M.AutoInit();
    },
}
</script>
<style lang="">
    
</style>