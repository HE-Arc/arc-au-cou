export const state = () => ({
  grid: [],
  time: 0,
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
    state.grid[data.x][data.y].value = data.number
    state.win = true
  },
  saveTime(state, value) {
    state.time = value
  },
}
