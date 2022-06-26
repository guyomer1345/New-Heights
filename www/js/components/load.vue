<template>
    <div v-if="is_loading">
        <!-- <div class="container" id="loading"> -->
        <!-- <div class="progress"> -->
        <!-- <div class="indeterminate"></div> -->
        <!-- </div> -->
        <!-- </div> -->
        <div id="loading-bg">
            <span class="loader"></span>
        </div>
    </div>
</template>

<script>
export default {
    name: "load_app",
    data() {
        return {
            is_loading: false,
        };
    },
    mounted() {},
};
</script>

<style>
#loading {
    z-index: 10000;
}

#loading-bg {
    --yellow: #ffee58;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    position: absolute;
    z-index: 99;
    background: rgba(0, 0, 0, 0.5);
}
.loader {
    width: 32px;
    height: 32px;
    position: absolute;
    top: 50%;
    left: 50%;
    border-radius: 50%;
    color: var(--yellow);
    animation: fill 1s ease-in infinite alternate;
}
.loader::before,
.loader::after {
    content: "";
    position: absolute;
    height: 100%;
    width: 100%;
    border-radius: 50%;
    left: 48px;
    top: 0;
    animation: fill 0.9s ease-in infinite alternate;
}

.loader::after {
    left: auto;
    right: 48px;
    animation-duration: 1.1s;
}

@keyframes fill {
    0% {
        box-shadow: 0 0 0 2px inset;
    }
    100% {
        box-shadow: 0 0 0 20px inset;
    }
}
</style>
