import re

from life.generation import Grid


class GenerationReader:
    def safe_int(self, n: str) -> int:
        try:
            return int(n)
        except ValueError:
            return 1

    def read(self, text: str) -> Grid:
        header, text = text.split('\n', 1)
        headers = {}
        for row in header.split(','):
            name, value = row.split('=')
            headers[name.strip()] = self.safe_int(value.strip())
        new_grid = []
        new_row: list[bool] = []
        segment = 1
        while text:
            cell = text[:segment]
            count = self.safe_int(cell[:-1])
            if cell in ('$', '!'):
                new_row += [False] * (headers['x']-len(new_row))
                new_grid.append(new_row)
                new_row = []
            elif cell.endswith('b'):
                new_row += [False] * count
            elif cell.endswith('o'):
                new_row += [True] * count
            elif cell != '\n':
                segment += 1
                continue
            text = text[segment:]
            segment = 1
        return new_grid

class GenerationWriter:
    def write(self, grid: Grid) -> str:
        lines = []
        for row in grid:
            line = []
            count = 0
            last = None
            for cell in row:
                if cell is last:
                    count += 1
                else:
                    if count > 1:
                        line.append(f'{count}')
                    if last:
                        line.append('o')
                    elif last is not None:
                        line.append('b')
                    count = 1
                    last = cell
            if last:
                if count > 1:
                    line.append(f'{count}')
                line.append('o')
            lines.append(''.join(line))
        result = '$'.join(lines) + '!'
        return '\n'.join(result[70*i:70*(i+1)] for i in range((len(result)//70)+1))
