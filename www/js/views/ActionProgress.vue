<template lang="">
    <div id="action-contianer">
        <span v-for="action in actions">
            <div class="action" :class="action.status">
                <span class="text">
                    {{ action.id }}
                </span>
                <span class="icon"></span>
            </div>
        </span>
    </div>
</template>
<script>
const Status = {
    Waiting: "wait",
    InProgress: "in-progress",
    Done: "done",
    Error: "error",
};
const Action = {
    Install: "install",
    Remove: "remove",
    Update: "update",
    None: "",
};
export default {
    data() {
        return {
            actions: [
                {
                    id: "python",
                    selected: "install",
                    status: Status.Waiting,
                },
                {
                    id: "7Zip",
                    selected: "install",
                    status: Status.InProgress,
                },
                {
                    id: "Miniconda",
                    selected: "install",
                    status: Status.Done,
                },
                {
                    id: "Python2",
                    selected: "install",
                    status: Status.Error,
                },
            ],
        };
    },
    methods: {
        async doActions() {
            for (const action of this.actions) {
                action.status = Status.InProgress;
                await pywebview.api.execute_action(action.id, action.selected);
                action.status = Status.Done;
            }
        },
    },
    mounted() {
        // this.actions = this.$store.state.actions;
        this.actions = this.actions.filter((action) => action.selected !== "");
        this.actions.map((action) => (action.status = Status.Waiting));
        this.doActions();
    },
};
</script>
<style lang="" scoped>
#action-contianer {
    margin: 1rem auto;
    width: 60%;
    --padding-size: 20px;
}

@keyframes slide {
    0% {
        left: 0;
        transform: translateX(-100%);
    }
    60%,
    100% {
        left: 100%;
        transform: translateX(0);
    }
}
@keyframes spin {
    0% {
        transform: translateY(-50%) rotate(0deg);
    }
    100% {
        transform: translateY(-50%) rotate(1turn);
    }
}

.action {
    position: relative;
    border-radius: 50px;
    height: 50px;
    margin: auto;
    color: black;
    padding: 10px var(--padding-size);
    overflow: hidden;
    margin: 2px 0;
    font-size: 20px;
}
.action span.text {
    top: 50%;
    left: var(--padding-size);
    transform: translateY(-50%);
}
.action .icon {
    box-sizing: content-box;
    position: absolute;
    right: var(--padding-size);
    top: 50%;
    transform: translateY(-50%);
}
.action .icon:before {
    font-family: FontAwesome;
}
.action.done .icon:before {
    content: "\f058";
}
.action.error .icon:before {
    content: "\f06a";
}
.action.in-progress .icon:before,
.action.wait .icon:before {
    content: "\f110";
}
.action.in-progress .icon,
.action.wait .icon {
    animation: spin 1s infinite steps(8);
}
.action.done,
.action.error {
    color: white;
    opacity: 0.4;
}
.action.in-progress {
    border: 1px solid var(--updateColor);
}
.action:after {
    content: "";
    z-index: -100;
    position: absolute;
    background: rgba(0, 0, 0, 0);
    left: 0;
    top: 0;
}
.action.in-progress:after {
    height: 100%;
    width: 80%;
    background: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, var(--updateColor) 100%);
    animation: slide 4s ease-in infinite;
    opacity: 0.5;
}
.action.done:after,
.action.error:after {
    width: 100%;
    height: 100%;
    background: var(--green);
}
.action.error:after {
    background: var(--red);
}
</style>
