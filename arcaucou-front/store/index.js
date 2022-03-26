import axios from 'axios'

export const state = () => ({
  grid: [],
  time: 0,
  win: false,
  userToken: null,
  lastCell: false,
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
  async changeValue(state, data) {
    state.grid[data.x][data.y].value = data.number
    this.commit('checkLastCell')
    if (state.lastCell) {
      await axios
        .post('/sudoku/check_sudoku', { sudoku: state.grid })
        .then((result) => {
          console.log(result)
          state.win = true
        })
        .catch((error) => {
          state.win = false
        })
    }
  },
  checkLastCell(state) {
    state.grid.forEach((row, i) => {
      row.forEach((cell, j) => {
        if (cell.value === 0) return
      })
    })
    state.lastCell = true
  },
  saveTime(state, value) {
    state.time = value
  },
  saveToken(state, token) {
    state.token = 'Token ' + token
  },
}
