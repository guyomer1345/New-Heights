<template>
    <div class="btn" @click="select_path">
        select
    </div>
    <div>
        {{ path }}
    </div>
</template>
<script>
export default {
    emits: ['wait'],
    data() {
        return {
            path: "Not selected"
        }
    },
    methods: {
        select_path() {
            let result = pywebview.api.select_dir().then((path) => { 
                this.path = path
                });
            this.$emit('wait', result);
        }
    }
}
</script>
<style lang="">
    
</style>