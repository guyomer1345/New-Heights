<template>
    <span>
        <span class="brackets" :class="{ active: isActive, animate: currentState == 'installing' }">
            <div class="content" :class="{ active: currentState == 'path' }">
                <!-- <div class="btn" @click="select_path">select</div> -->
                <div id="file_select" @click="select_path">
                    {{ path || "SELECT INSTALLATION PATH" }}
                </div>
                <div class="install-btn" :class="{ active: path }" @click="changeState('installing')"></div>
            </div>
            <div class="content" :class="{ active: currentState == 'installing' }">
                <h1 style="width: 100%">Installing...</h1>
            </div>
        </span>
    </span>
</template>
<script>
const State = {
    Path: "path",
    Installing: "installing",
};
export default {
    emits: ["wait"],
    data() {
        return {
            path: "",
            isActive: true,
            currentState: State.Path,
        };
    },
    methods: {
        select_path() {
            let result = pywebview.api.select_dir().then((path) => {
                this.path = path;
            });
            this.$emit("wait", result);
        },
        sleep(x) {
            return new Promise((r) => setTimeout(r, x));
        },
        install() {
            if (path) {
                changeState(State.Installing);
            }
        },
        async changeState(state) {
            this.isActive = false;
            await this.sleep(1000); // Wait for the animation of the closing to finish
            this.currentState = state;
            await this.sleep(1000); // This works. just liek this "W-O-R-K-S"
            this.isActive = true;
        },
    },
    mounted() {
        this.isActive = true;
        this.currentState = State.Installing;
        this.currentState = State.Path;

        // setInterval(() => {
        //     if (this.currentState === State.Path) {
        //         this.changeState(State.Installing);
        //     } else {
        //         this.changeState(State.Path);
        //     }
        // }, 4000);
    },
};
</script>
<style lang="">
@keyframes thiner {
    from {
        width: 20%;
    }
    to {
        width: 0%;
    }
}
.brackets > * {
    display: inline-block;
    position: relative;
}
.brackets {
    display: inline-block;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 70%;
    height: 200px;
}
.brackets * {
    font-family: "Courier New", Courier, monospace;
}
.brackets .content {
    width: 0%;
    overflow: hidden;
    text-align: center;
    align-items: center;
    position: absolute;
    white-space: nowrap;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.5s;
    /* height: 100%; */
}
.install-btn {
    background: white;
    display: inline-block;
    margin: 40px auto;
    position: relative;
}

.install-btn::before {
    content: "\00a0<btn>\00a0\00a0\00a0\00a0\00a0\00a0\00a0<\\btn>";
    white-space: nowrap;
    font-size: 30px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    opacity: 0;
    transition: 0.3s opacity;
    color: blueviolet;
    font-weight: bold;
}
.install-btn.active::before {
    opacity: 1;
}
.install-btn::after {
    content: "INSTALL";
    font-size: 30px;
    animation: randomize 1s linear 0s infinite;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    cursor: default;
}
.install-btn.active::after {
    animation: none;
    cursor: pointer;
    text-decoration: underline;
    color: blue;
}

#file_select {
    width: 60%;
    overflow: hidden;

    text-overflow: ellipsis;
    white-space: nowrap;

    height: 40px;
    background: none;
    color: var(--darkColor);
    text-align: center;
    font-size: 20px;
    margin: 10px auto;
    padding: 1px 5px;
    border-bottom: 5px solid black;

    cursor: pointer;
}
.brackets.active .content.active {
    width: 100%;
    transition: width 0.5s 0.5s;
}

.brackets:before,
.brackets:after {
    color: rgb(30, 20, 10);
    font-family: Roboto, Consolas, Menlo, Monaco, monospace;
    font-size: 200px;
    opacity: 0.8;
    display: inline-block;
    position: absolute;
    top: 50%;
    transition: transform 1s, left 1s, right 1s;
}
.brackets:before {
    content: "{";
    left: 50%;
    transform: translateX(-100%) translateY(-50%);
}
.brackets:after {
    content: "}";
    right: 50%;
    transform: translateX(100%) translateY(-50%);
}

.brackets.active:before {
    left: 0;
    transform: translateY(-50%);
}
.brackets.active:after {
    right: 0;
    transform: translateY(-50%);
}

.brackets.animate.active:before {
    animation: pulse 0.4s 0.5s alternate infinite ease-in-out;
}
.brackets.animate.active:after {
    animation: pulse 0.4s 0.8s alternate infinite ease-in-out;
}
@keyframes pulse {
    to {
        /* transform: translateY(-50%) scale(0.9); */
        opacity: 0.2;
    }
}
@keyframes randomize {
    0% {
        content: "ZGMZSUH";
    }
    5% {
        content: "LSIMIYB";
    }
    10% {
        content: "ORWFAUA";
    }
    15% {
        content: "ZQSCUPD";
    }
    20% {
        content: "NKFMNJM";
    }
    25% {
        content: "UIPYXUN";
    }
    30% {
        content: "XJZZILX";
    }
    35% {
        content: "QTJSPVF";
    }
    40% {
        content: "BANCYHW";
    }
    45% {
        content: "HQNLNLF";
    }
    50% {
        content: "UGAWEKG";
    }
    55% {
        content: "RDWDTPT";
    }
    60% {
        content: "NYSAHXS";
    }
    65% {
        content: "GYBIXSE";
    }
    70% {
        content: "SHWUJQD";
    }
    75% {
        content: "OYNODTK";
    }
    80% {
        content: "PWIPLXQ";
    }
    85% {
        content: "PMMQVVH";
    }
    90% {
        content: "MRPQUFP";
    }
    95% {
        content: "SVJORNR";
    }
    100% {
        content: "INSTALL";
    }
}
</style>
