from arcaucouapp.models import Sudoku


def generate_sudoku():
    """
    Every day at midnight, generate the new sudoku
    """
    sudoku = Sudoku.objects.get(pk=1)
    sudoku.generate()
    sudoku.save()
