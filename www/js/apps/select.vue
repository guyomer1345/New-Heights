<template>
  <div class="fixed-action-btn">
    <a class="btn-floating btn-large waves-green">
      <i class="large material-icons">check</i>
    </a>
    <ul>
      <li @click="set_selection('install')">
        <a class="btn-floating cyan darken-1"
          ><i class="material-icons">select_all</i></a
        >
      </li>
      <li @click="set_selection('remove')">
        <a class="btn-floating orange darken-1"
          ><i class="material-icons">clear_all</i></a
        >
      </li>
    </ul>
  </div>
  <div class="container">
    <div id="action-list">
      <div
        class="action"
        v-for="action in actions"
        :class="get_action_class(action)"
      >
        <div class="icon action-remove" @click="action.selected = 'remove'">
          <i class="fa-solid fa-circle-xmark"></i>
        </div>
        <div class="icon action-install" @click="action.selected = 'install'">
          <i class="fa-solid fa-circle-arrow-down"></i>
        </div>
        <div class="action-name">{{ action.id }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "select-app",
    template: "#select-app",
    emits: ['wait'],

    data() {
        return {
            minutes: 10,
            actions: [],

            loaded: false,
            is_changed: false,
        }
    },
    methods: {
        get_action_class(action){
            console.log(action)
            if (action.selected === 'install'){
                return 'remove'
            }
            if (action.selected === 'remove'){
                return 'install'
            }
            if (action.actions.includes('remove')){
                return 'remove'
            }
            if (action.actions.includes('install')){
                return 'install'
            }
            return ''
        },
        set_selection(value) {
            this.actions.forEach(action => action.selected = value);
        },
    },
    watch: {
        installers(val){
            if (this.loaded){
                this.is_changed = true;
            }
        }
    },
    mounted() {
        M.AutoInit();
        if (this.loaded) {
            return;
        }
        pywebview.api.resize(800);
        let result = pywebview.api.get_actions().then(actions => {
            actions.forEach(action => action.selected = "")
            this.actions = actions
            this.loaded = true;
        });
        this.$emit('wait', result);
    }
};
</script>

<style>

</style>
