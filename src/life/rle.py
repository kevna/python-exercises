import re

from life.generation import Grid


class GenerationReader:
    def safe_int(self, n: str) -> int:
        try:
            return int(n)
        except ValueError:
            return 1

    def parse_headers(self, header: str) -> dict:
        headers = {}
        for row in header.split(','):
            name, value = row.split('=')
            headers[name.strip()] = self.safe_int(value.strip())
        return headers

    def parse_rows(self, headers: dict, text: str) -> Grid:
        new_row: list[bool] = []
        segment = 1
        while text:
            cell = text[:segment]
            count = self.safe_int(cell[:-1])
            if cell in ('$', '!'):
                new_row += [False] * (headers['x'] - len(new_row))
                yield new_row
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

    def read(self, text: str) -> Grid:
        header, text = text.split('\n', 1)
        headers = self.parse_headers(header)
        return list(self.parse_rows(headers, text))


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
        return '\n'.join(self.segment_string('$'.join(lines) + '!'))

    def segment_string(self, string: str, length: int = 70):
        segments = len(string) // 70
        for i in range(segments + 1):
            yield string[length*i:length*(i+1)]
