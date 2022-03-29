import axios from 'axios'

export const state = () => ({
  grid: [],
  time: 0,
  win: false,
  wrong: false,
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
    console.log(state.lastCell)
    if (state.lastCell) {
      console.log('ok')
      state.commit('setWrong', false)
      await axios
        .post('/sudoku/check_sudoku', { sudoku: state.grid })
        .then((result) => {
          console.log(result)
          state.commit('setWin', true)
        })
        .catch((error) => {
          state.commit('setWin', false)
          state.commit('setWrong', true)
        })
    }
  },
  checkLastCell(state) {
    let good = true
    state.grid.forEach((row, i) => {
      row.forEach((cell, j) => {
        if (cell.value === 0) good = false
      })
    })
    state.lastCell = good
  },
  saveTime(state, value) {
    state.time = value
  },
  setWin(state, value) {
    state.win = value
  },
  setWrong(state, value) {
    state.wrong = value
  },
}
