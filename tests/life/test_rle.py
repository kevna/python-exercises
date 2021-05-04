import pytest

from life.generation import Generation
from life.rle import GenerationReader, GenerationWriter


class TestGenerationReader:
    @pytest.mark.parametrize('text, expected', (
        (
            'x = 3, y = 3\n'
            'bo$2bo$3o!',
            Generation([
                [False, True , False],
                [False, False, True ],
                [True , True , True ],
            ]),
        ),
        (
            'x = 36, y = 9\n'
            '24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$2o8bo3bob2o4b\n'
            'obo$10bo5bo7bo$11bo3bo$12b2o!',
            Generation([
                [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, False, True , True , False, False, False, False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True ],
                [False, False, False, False, False, False, False, False, False, False, False, True , False, False, False, True , False, False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True ],
                [True , True , False, False, False, False, False, False, False, False, True , False, False, False, False, False, True , False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                [True , True , False, False, False, False, False, False, False, False, True , False, False, False, True , False, True , True , False, False, False, False, True , False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, True , False, False, False, False, False, True , False, False, False, False, False, False, False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, True , False, False, False, True , False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            ]),
        ),
    ))
    def test_from_rle(self, text, expected):
        actual = GenerationReader().read(text)
        assert actual == expected._grid


class TestGenerationWriter:
    @pytest.mark.parametrize('grid, expected', (
        (
            [
                [False, True , False],
                [False, False, True ],
                [True , True , True ],
            ],
            'bo$2bo$3o!',
        ),
        (
            [
                [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, False, True , True , False, False, False, False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True ],
                [False, False, False, False, False, False, False, False, False, False, False, True , False, False, False, True , False, False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True ],
                [True , True , False, False, False, False, False, False, False, False, True , False, False, False, False, False, True , False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                [True , True , False, False, False, False, False, False, False, False, True , False, False, False, True , False, True , True , False, False, False, False, True , False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, True , False, False, False, False, False, True , False, False, False, False, False, False, False, True , False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, True , False, False, False, True , False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False, False, False, False, True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            ],
            '24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$2o8bo3bob2o4b\n'
            'obo$10bo5bo7bo$11bo3bo$12b2o!',
        ),
    ))
    def test_to_rle(self, grid, expected):
        actual = GenerationWriter().write(grid)
        assert actual == expected

