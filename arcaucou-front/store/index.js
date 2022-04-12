import axios from 'axios'

export const state = () => ({
  grid: [], //The current grid
  time: 0, //Time in seconds
  win: false, //If the player has won
  wrong: false, //If the player has made a mistake
  lastCell: false, //If the player has to fill the last cell
  cellSelected: { x: -1, y: -1 }, //The cell selected by the player
})

export const mutations = {
  /**
   * Init the grid
   */
  initGrid(state, gridStart) {
    state.grid = gridStart.map((arr) => {
      return arr.slice()
    })
  },
  /**
   * Change the selected cell
   */
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
  /**
   * Move the selected cell
   */
  moveSelectCell(state, direction) {
    let newSelected = { x: state.selectCell.x, y: state.selectCell.y }
    switch (direction) {
      case 'right':
        if (newSelected.y === 2 || newSelected.y === 5 || newSelected.y === 8) {
          if (
            newSelected.x === 2 ||
            newSelected.x === 5 ||
            newSelected.x === 8
          ) {
            newSelected.x -= 2
            newSelected.y -= 2
          } else {
            newSelected.x += 1
            newSelected.y -= 2
          }
        } else {
          newSelected.y += 1
        }
        break
      case 'left':
        if (newSelected.y === 0 || newSelected.y === 3 || newSelected.y === 6) {
          if (
            newSelected.x === 0 ||
            newSelected.x === 3 ||
            newSelected.x === 6
          ) {
            newSelected.x += 2
            newSelected.y += 2
          } else {
            newSelected.x -= 1
            newSelected.y += 2
          }
        } else {
          newSelected.y -= 1
        }
        break
      case 'up':
        if (newSelected.y === 0 || newSelected.y === 1 || newSelected.y === 2) {
          if (
            newSelected.x === 0 ||
            newSelected.x === 1 ||
            newSelected.x === 2
          ) {
            newSelected.x += 6
            newSelected.y += 6
          } else {
            newSelected.x -= 3
            newSelected.y += 6
          }
        } else {
          newSelected.y -= 3
        }
        break
      case 'down':
        if (newSelected.y === 6 || newSelected.y === 7 || newSelected.y === 8) {
          if (
            newSelected.x === 6 ||
            newSelected.x === 7 ||
            newSelected.x === 8
          ) {
            newSelected.x -= 6
            newSelected.y -= 6
          } else {
            newSelected.x += 3
            newSelected.y -= 6
          }
        } else {
          newSelected.y += 3
        }
    }
    this.commit('selectCell', newSelected)
  },
  /**
   * Change the value of the selected cell
   */
  async changeValue(state, number) {
    if (
      !state.win &&
      !state.grid[state.selectCell.x][state.selectCell.y].isLocked
    ) {
      state.grid[state.selectCell.x][state.selectCell.y].value = number
      this.commit('checkLastCell')
      if (state.lastCell) {
        //If is the last cell check the validity of the grid
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
  /**
   * Check if this is the last cell to fill
   */
  checkLastCell(state) {
    let good = true
    state.grid.forEach((row, i) => {
      row.forEach((cell, j) => {
        if (cell.value === 0) good = false
      })
    })
    state.lastCell = good
  },
  /**
   * Save the time
   */
  saveTime(state, value) {
    state.time = value
  },
  /**
   * Set the win state
   */
  setWin(state, value) {
    state.win = value
  },
  /**
   * Set the wrong state
   */
  setWrong(state, value) {
    state.wrong = value
  },
  /**
   * Set the selected cell state
   */
  setSelectedCell(state, value) {
    state.selectCell = value
  },
}

export const actions = {
  /**
   * Check the validity of the grid
   */
  async CHECK_SUDOKU(state, sudoku) {
    await axios
      .post('http://localhost:8000/api/sudoku/check_sudoku/', {
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
