import axios from 'axios'

export const state = () => ({
  grid: [],
  time: 0,
  win: false,
  wrong: false,
  lastCell: false,
  cellSelected: {x: -1, y:-1}
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
          this.commit('setSelectedCell', { x: i, y: j })
        } else {
          cell.isSelected = false
        }
      })
    })
  },
  async changeValue(state, number) {
    state.grid[state.selectCell.x][state.selectCell.y].value = number
    this.commit('checkLastCell')
    if (state.lastCell) {
      console.log('ok')
      this.commit('setWrong', false)
      await axios
        .post('/sudoku/check_sudoku', { sudoku: state.grid })
        .then((result) => {
          console.log(result)
          this.commit('setWin', true)
        })
        .catch((error) => {
          this.commit('setWin', false)
          this.commit('setWrong', true)
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
  setSelectedCell(state, value) {
    state.selectCell = value;
  }
}
