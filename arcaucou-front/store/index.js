import Vue from 'vue'

export const state = () => ({
  grid: [],
  time: null,
  win: false,
})

export const mutations = {
  initGrid(state, gridStart) {
    state.grid = gridStart.map((arr) => {
      return arr.slice()
    })
  },
  changeValue(state, data) {
    console.log(data)
    state.grid[data.x][data.y] = data.number
    state.win = true;
  },
}
