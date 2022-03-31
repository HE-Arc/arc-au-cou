import axios from 'axios'

export const state = () => ({
  grid: [],
  time: 0,
  win: false,
  wrong: false,
  lastCell: false,
  cellSelected: { x: -1, y: -1 },
})

export const getters = {
  getTime(state) {
    return state.time
  },
}

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
  moveSelectCell(state, direction) {
    let newSelected = { x: state.selectCell.x, y: state.selectCell.y }
    switch (direction) {
      case 'right':
        if (newSelected.y === 2 || newSelected.y === 5 || newSelected.y === 8) {
          newSelected.x += 1
          newSelected.y -= 2
        } else {
          newSelected.y += 1
        }
        break
      case 'left':
        if (newSelected.y === 0 || newSelected.y === 3 || newSelected.y === 6) {
          newSelected.x -= 1
          newSelected.y += 2
        } else {
          newSelected.y -= 1
        }
        break
      case 'up':
        if (newSelected.y === 0 || newSelected.y === 1 || newSelected.y === 2) {
          newSelected.x -= 3
          newSelected.y += 6
        } else {
          newSelected.y -= 3
        }
        break
      case 'down':
        if (newSelected.y === 6 || newSelected.y === 7 || newSelected.y === 8) {
          newSelected.x += 3
          newSelected.y -= 6
        } else {
          newSelected.y += 3
        }
    }
    this.commit('selectCell', newSelected)
  },
  async changeValue(state, number) {
    state.grid[state.selectCell.x][state.selectCell.y].value = number
    this.commit('checkLastCell')
    if (state.lastCell) {
      console.log('ok')
      this.commit('setWrong', false)
      await axios
        .post('api/sudoku/check_sudoku/', { sudoku: state.grid })
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
    /*this.$cookies.set('sudoku-time', value, {
      path: '/',
      maxAge: age,
    })*/
  },
  setWin(state, value) {
    state.win = value
    //Axios save time
  },
  setWrong(state, value) {
    state.wrong = value
  },
  setSelectedCell(state, value) {
    state.selectCell = value
  },
}
