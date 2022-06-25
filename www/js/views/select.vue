<template>
    <Navigation nextPage="/action_progress" :isReady="is_ready()"></Navigation>

    <div class="container">
        <div class="action-item" @click="install_all()">
            <i class="icon fa-solid fa-square-check"></i>
            Select All
        </div>
        <div id="action-list">
            <div class="action" v-for="action in actions" :class="get_action_class(action)">
                <div class="icon action-remove" @click="set_action(action, 'remove')">
                    <i class="fa-solid fa-circle-xmark"></i>
                </div>
                <div
                    class="icon action-update"
                    v-if="action.actions.includes('update')"
                    @click="set_action(action, 'update')"
                >
                    <i class="fa-solid fa-circle-arrow-down"></i>
                </div>
                <div class="icon action-install" v-else @click="set_action(action, 'install')">
                    <i class="fa-solid fa-circle-plus"></i>
                </div>
                <div class="action-name">{{ action.id }}</div>
            </div>
        </div>
    </div>
</template>

<script>
const Action = {
    Install: "install",
    Remove: "remove",
    Update: "update",
    None: "",
};

export default {
    name: "select-app",
    emits: ["wait"],

    data() {
        return {
            actions: [],
        };
    },
    methods: {
        set_action(action, selected_action) {
            if (!action.actions.includes(selected_action)) {
                selected_action = Action.None;
            }
            action.selected = selected_action;
            this.$store.commit("setActions", { actions: this.actions });
        },
        install_all() {
            this.actions.forEach((action) => {
                if (action.actions.includes(Action.Install)) {
                    action.selected = Action.Install;
                } else if (action.actions.includes(Action.Update)) {
                    action.selected = Action.Update;
                } else {
                    action.selected = Action.None;
                }
            });
            this.$store.commit("setActions", { actions: this.actions });
        },
        get_action_class(action) {
            if (action.selected) {
                return action.selected;
            }

            if (action.actions.includes(Action.Remove)) {
                if (action.actions.includes(Action.Update)) {
                    return Action.Update;
                }
                return Action.Install;
            }
            if (action.actions.includes(Action.Install)) {
                return Action.Remove;
            }
            return Action.None;
        },
        set_selection(value) {
            this.actions.forEach((action) => (action.selected = value));
        },
        is_ready() {
            return this.actions.some((action) => action.selected !== Action.None);
        },
    },

    mounted() {
        M.AutoInit();

        pywebview.api.resize(600);
        if (this.$store.state.actions.length) {
            this.actions = this.$store.state.actions;
            return;
        }
        let result = pywebview.api.get_actions().then((actions) => {
            actions.forEach((action) => {
                action.selected = Action.None;
                if (action.actions.includes(Action.Update)) {
                    action.selected = Action.Update;
                }
            });
            this.actions = actions;
            this.$store.commit("setActions", { actions: this.actions });
        });
        this.$emit("wait", result);
    },
};
</script>

<style scoped>
.action-item {
    position: relative;
    width: 40%;
    height: 50px;
    background: None;
    color: var(--green);
    border-radius: 10px;
    border: 3px solid var(--green);
    margin: 1rem auto;
    font-size: 30px;
    text-align: center;
    transition: 0.1s background-color, 0.1s color;
    cursor: pointer;
}

.action-item .icon {
    position: absolute;
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
}

.action-item:hover {
    color: white;
    background-color: var(--green);
}
</style>
