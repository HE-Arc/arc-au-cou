import datetime
from arcaucouapp.models import Sudoku


def generate_sudoku():
    """
    Every day at midnight, generate the new sudoku
    """
    sudoku = None
    if Sudoku.objects.filter(pk=1).count():
        sudoku = Sudoku.objects.create(
            start_sudoku="", end_sudoku="", date=datetime.datetime.now())
    else:
        sudoku = Sudoku.objects.get(pk=1)
    sudoku.generate()
    sudoku.save()
