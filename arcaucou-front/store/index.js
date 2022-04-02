import axios from 'axios'

export const state = () => ({
  grid: [],
  time: 0,
  win: false,
  wrong: false,
  lastCell: false,
  cellSelected: { x: -1, y: -1 },
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
    if (!state.win) {
      state.grid[state.selectCell.x][state.selectCell.y].value = number
      this.commit('checkLastCell')
      if (state.lastCell) {
        this.commit('setWrong', false)
        const sudoku = state.grid.map((block) => {
          return block.map((cell) => {
            return cell.value
          })
        })
        this.dispatch('CHECK_SUDOKU', sudoku)
      }
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
    //Axios save time
  },
  setWrong(state, value) {
    state.wrong = value
  },
  setSelectedCell(state, value) {
    state.selectCell = value
  },
}

export const actions = {
  async CHECK_SUDOKU(state, sudoku) {
    await axios
      .post('https://arcaucou.srvz-webapp.he-arc.ch/api/sudoku/check_sudoku/', {
        sudoku: sudoku,
      })
      .then((result) => {
        if (result.data.result) {
          this.commit('setWin', true)
        } else {
          this.commit('setWin', false)
          this.commit('setWrong', true)
        }
      })
      .catch((error) => {
        this.commit('setWin', false)
        this.commit('setWrong', true)
      })
  },
}
