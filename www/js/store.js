const { createStore } = Vuex;

const store = createStore({
  state () {
    return {
      actions: []
    }
  },
  mutations: {
    setActions (state, payload) {
      state.actions = payload.actions
    }
  }
})
