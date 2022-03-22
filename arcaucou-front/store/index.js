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
  selectCell(state, data) {
    state.grid.forEach((row, i) => {
      row.forEach((cell, j) => {
        if (i === data.x && j === data.y) {
          cell.isSelected = true
        } else {
          cell.isSelected = false
        }
      })
    })
  },
  changeValue(state, data) {
    console.log(data.number)
    state.grid[data.x][data.y].value = data.number
    state.win = true
  },
}
