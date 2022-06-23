<template>
    <div class="fixed-action-btn">
        <a @click="next" class="btn-floating btn-large darken-1" :class="[isReady ? 'green' : 'grey' ]">
            <i class="large material-icons">navigate_next</i>
        </a>
        <ul>
            <li @click="previous">
                <a class="btn-floating orange darken-1">
                    <i class="material-icons">navigate_before</i>
                </a>
            </li>
        </ul>
    </div>
</template>
<script>
export default {
    props: {
        nextPage: String,
        isReady: {
            default: true,
            type: Boolean
        }
    },
    mounted() {
        M.AutoInit();
    },
    methods: {
        previous() {
            this.$router.back();
        },
        next() {
            if (this.$props.isReady) {
                this.$router.push(this.$props.nextPage)
            }
        }
    },
}
</script>
<style lang="">
    
</style>