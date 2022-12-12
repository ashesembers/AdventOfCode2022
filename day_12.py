INPUT_STR = """abaaacccccccccaaaaaaccccccccccccccccaacccccccccccaacaaaaaaaaaaaaaaaaaccaaaaacccaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaa
abaaacccccccccaaaaaacccccccccccccccaaaaccccccccccaaaaaaaacaaaaaaaaaaaccaaaaaaccaaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaa
abaaaccccccccccaaaaacccccccccccccccaaaacccccccccccaaaaacccaaaaaaaaaacccaaaaaacccaaccccccccccccccaaaaacccccccccccccccccccccccccccccccccccccaaaaaa
abccccaaccccccaaaaacccccccccaaaaaccaaaaccccccccccccaaaaacaaaaaaaaacccccaaaaaccccccccccccccccccccaaaaacccccccccccccccccaaaccccaaaccccccccccaaacaa
abcccaaaacccccaaaaacccccccccaaaaacccccccccccccccccaaacaaaaaaaaaacccccccaaaaacccccccccccccccccccaaaaaacccccccccccccccccaaaaccaaaaccccccccccccccaa
abcccaaaaacacccccccccccccccaaaaaaccccccccccccccccccaaccaaaaacaaaaccccccccccccccccccccccccccccccaaaaaaccccccccccccccccccaaaaaaaacccccccccccccccaa
abaaaaaaaaaacccccccccccccccaaaaaaccccccccccccccccccccccaaaacccaaaccccccccccccccccccccccccccccccaaaaaacccccccccccccccciiiiijaaaaccccccccccccccccc
abaaaaaaaaaacccccccccccccccaaaaaacccccccccccccccccccccccccccccaaacccccccccccccccccccccccccccccccaaaccccccccccccccccciiiiiijjjaccccccccaaaccccccc
abccaaaaaaccccccccccccccccccaaaccccccccccccccccccccccccccccccccacccccccccccaacccccccccccccccccccccccccccccccccccccciiiiioijjjjaaccccccaaaaaacccc
abccaaaaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccccccccciiinnooojjjjjaaccaaaaaaaacccc
abccaaaaaacccccccccccccccccccccccccccccccccccccaacccccaacccccccccccccccccaaaaaacccccccccccccccccccccccccccaaaccccciiinnnoooojjjjjjkkkaaaaaaacccc
abcaaaaaaaaccccccccccccccccccccccccccccccccccccaaaccaaaaaaccccaaacccccccccaaaacccccccccccccccccccccccccccccaaaaccciiinnnouooojjjjkkkkkaaaaaccccc
abccaccccccccccccccccccaaccccccaccccccccccccaaaaaaaaaaaaaacccaaaacccccccccaaaacccccccccccccccccccccccccccaaaaaacchhinnnttuuooooookkkkkkkaaaccccc
abccccccccccccccccccaacaaaccccaaaaaaaaccccccaaaaaaaacaaaaacccaaaacccccccccaccacccccccccccccccccccccccccccaaaaacchhhhnntttuuuooooppppkkkkcaaacccc
abccccccccaaacccccccaaaaaccccccaaaaaaccccccccaaaaaacaaaaaccccaaaaccccccccccccccccccccccccccccaccccccccccccaaaaahhhhnnntttxuuuooppppppkkkcccccccc
abccccccccaaaacccccccaaaaaaccccaaaaaaccaaacccaaaaaacaaaaaccccccccccccccaaccccccccccccccaaaaaaaacccccccccccaachhhhhnnnntttxxuuuuuuuupppkkkccccccc
abccccccccaaaacccccaaaaaaaacccaaaaaaaacaaacacaaaaaaccccccccccccccccccccaacccccccccccccccaaaaaacccccccccccccchhhhmnnnntttxxxxuuuuuuupppkkcccccccc
abacccccccaaaacccccaaaaacaaccaaaaaaaaaaaaaaaaaaccaacccccccccccccccccaaaaaaaaccccccccccccaaaaaaccccccccccccchhhhmmmntttttxxxxuyyyuvvpppklcccccccc
abacccccccccccccccccacaaaccaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccaaaaaaaacccccccccccaaaaaaaaccccccccccccgghmmmtttttxxxxxxyyyyvvvpplllcccccccc
abaccccccccaacccccccccaaaccaaaaaaaacaaaaaaaaaaccccccccccccccccccccccccaaaaccccccccccccaaaaaaaaaaccccccaccccgggmmmtttxxxxxxxyyyyyvvppplllcccccccc
SbaaaccccccaaacaaaccccccccaaaaaaaaacaaaaaaaaacccccccccccccccccccccccccaaaaacccccccccccaaaaaaaaaaaaacaaaccaagggmmmtttxxxEzzzzyyyvvppplllccccccccc
abaacccccccaaaaaaacccccccaaaaaaacaaccaaaaaaaccccccccccccccaaaccccccccaaaaaacccccccccccacacaaacccaaaaaaacaaagggmmmsssxxxxxyyyyyvvvqqqlllccccccccc
abaccccccccaaaaaaccacccaaaaaaaaacccccccaaaaaaccccccccccccaaaaccccccccaaccaacccccccccccccccaaaccccaaaaaaccaagggmmmssssxxwwyyyyyyvvqqqlllccccccccc
abaccccccaaaaaaaaccaacaaaccaaaaaacccccaaaaaaaccccccccccccaaaaccccccccccaacccccccccccccccccaacccccaaaaaaaaaaggggmmmssssswwyywyyyyvvqqlllccccccccc
abaccccccaaaaaaaaacaaaaacccaaaaaacccccaaacaaaccccccccccccaaaaccccccccaaaaaaccccccccccccaacccccccaaaaaaaaaaaaggggmmmossswwyywwyyvvvqqqllccccccccc
abcccccccaaaaaaaaaacaaaaaacaaccccccccaaacccccccccccccccccccccccccccccaaaaaaccccccccccccaaaaacccaaaaaaaaaaaaaaggggoooosswwywwwwvvvvqqqmlccccccccc
abccccccccccaaacaaaaaaaaaacccccccccccaaacaccccccccccccccccccccccccccccaaaaccccccccccccaaaaaccccaaacaaacccaaacagggfooosswwwwwrvvvvqqqqmmccccccccc
abccccccccccaaacccaaaaaaaacccccccccaacaaaaacccccccccccccccccccccccccccaaaaccccccccccccaaaaaacccccccaaacccaaccccfffooosswwwwrrrrrqqqqqmmccccccccc
abccccccccccaacccccccaaccccccccccccaaaaaaaacccccccccccccaaccccccccccccaccaccccccccccccccaaaacccccccaacccccccccccfffoossrwrrrrrrrqqqqmmmccccccccc
abccaaaccccccccccccccaacccccccccccccaaaaaccccccccccccaacaacccccccaaaaacccccccccccccccccaacccccccccccccccccccccccfffoossrrrrrnnnmqqmmmmmccccccccc
abcaaaaccccccccccccccccccccccccccccccaaaaacccccccccccaaaaacccccccaaaaacccaaaccccccccccccccccccccccccccccccccccccfffooorrrrrnnnnmmmmmmmccccaacccc
abcaaaacccccccccccccccccccccccccccccaaacaaccccacccccccaaaaaaccccaaaaaaccccaaaccacccccccccccccccccccccccccccccccccffoooonnnnnnnnmmmmmmccccaaacccc
abccaaacccccccccccccccccccccaaaaaccccaaccccaaaacccccaaaaaaaaccccaaaaaaccccaaaaaaaccccccccccccccccaccaccccccccccccfffooonnnnnnddddddddcccaaaccccc
abccccccccccccccccccccccccccaaaaaccccccccccaaaaaacccaaaaacaacccaaaaaaaccaaaaaaaacccccccccccccccccaaaaccccccccccccfffeonnnnneddddddddddcaaacccccc
abccccccccccaaaccccccccccccaaaaaacccccccccccaaaacccccacaaacccccaacaacccaaaaaaaaacccccccccccccccccaaaacccccccccccccffeeeeeeeeddddddddcccaaacccccc
abcccccccccaaaaccccacccccccaaaaaaccccccccccaaaaacccccccaaaacccaaacaccccaaaaaaaaaccccccccccccccccaaaaaaccccccccccccceeeeeeeeedacccccccccccccccccc
abaccccccccaaaaccccaaacaaacaaaaaaccccccccccaacaaccccccccaaaacaaaacaaacaaaaaaaaaacccccccccccccaacaaaaaacccccccccccccceeeeeeeaaacccccccccccccccaaa
abaaacccccccaaaccccaaaaaaaccaaaccccccccaaacccccccccccccccaaaaaaaacaaaaaaaaaaaaaaacacaaccaaacaaacccaacccccccccccccccccaacccaaaacccccccccccccccaaa
abaaaccccccccccccccaaaaaaccccccccccccccaaacccccccccccccccaaaaaaaccaaaaaaccaacccaccaaaaccaaaaaaaccccccccaaccccccccccccccccccaaacccccccccccccccaaa
abaaccccccccccccccaaaaaaacccccccccccaaaaaaaaccccccccccccccaaaaaaaaaaaaaacaaaccccccaaaaaccaaaaaaccccccaaaaccccccccccccccccccaaaccccccccccccaaaaaa
abaaaccccccccccccaaaaaaaaaacccccccccaaaaaaaacccccccccccaaaaaaaaaaaaaaaaaaacccccccaaaaaacaaaaaaaaaccccaaaaaacccccccccccccccccccccccccccccccaaaaaa"""
TEST_INPUT_STR = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

z_map = {"a": 1,
         "b": 2,
         "c": 3,
         "d": 4,
         "e": 5,
         "f": 6,
         "g": 7,
         "h": 8,
         "i": 9,
         "j": 10,
         "k": 11,
         "l": 12,
         "m": 13,
         "n": 14,
         "o": 15,
         "p": 16,
         "q": 17,
         "r": 18,
         "s": 19,
         "t": 20,
         "u": 21,
         "v": 22,
         "w": 23,
         "x": 24,
         "y": 25,
         "z": 26,
         "S": 1,
         "E": 26,
         }


class Point:
    def __init__(self, x_value, y_value, z_value, north, south, east, west, is_start, is_end):
        self.x_value = x_value
        self.y_value = y_value
        self.z_value = z_value
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.is_start = is_start
        self.is_end = is_end

    def distance_to_point(self, p):
        """heuristic"""
        return (abs(self.x_value - p.x_value) + abs(self.y_value - p.y_value))

    def print_neighbours(self):
        print(", ".join([f"{p.x_value}|{p.y_value}" for p in [self.north, self.south, self.east, self.west] if p]))

    def to_string(self):
        return f"{self.x_value}|{self.y_value} "


def parse_map(input_str):
    start = []
    end = None
    data = []
    y_count = 0
    for line in input_str.split("\n"):
        row = []
        x_count = 0
        for char in line:
            z_value = z_map.get(char)
            p = Point(x_count, y_count, z_value, False, False, False, False, False, False)
            row.append(p)
            if char == "S" or char == "a":  # TODO comment out [or char == "a"] for part 1 answer
                p.is_start = True
                start.append((x_count, y_count))
            elif char == "E":
                p.is_end = True
                end = (x_count, y_count)
            x_count += 1
        y_count += 1
        data.append(row)

    # Link em up
    for i in range(len(data)):
        for j in range(len(data[i])):
            point = data[i][j]
            if j > 0 and data[i][j - 1].z_value <= point.z_value + 1:
                point.west = data[i][j - 1]
            try:
                if data[i][j + 1].z_value <= point.z_value + 1:
                    point.east = data[i][j + 1]
            except IndexError:
                print("")
            if i > 0 and data[i - 1][j].z_value <= point.z_value + 1:
                point.north = data[i - 1][j]
            try:
                if data[i + 1][j].z_value <= point.z_value + 1:
                    point.south = data[i + 1][j]
            except IndexError:
                print("")

    return data, start, end


def les_gooooo(input_str):
    data, start, end = parse_map(input_str)
    print(start)
    print(end)
    end_point = data[end[1]][end[0]]

    # A-star baybeeeee
    to_visit = []
    seen = {}
    best_path = []
    for x, y in start:
        to_visit.append([data[y][x]])

    while to_visit:
        to_visit.sort(key=lambda x: len(x) + x[-1].distance_to_point(end_point))
        current_path = to_visit.pop(0)
        current = current_path[-1]

        if current in seen and seen[current] <= len(current_path):
            continue
        seen[current] = len(current_path)

        if current == end_point:
            if not best_path:
                best_path = current_path
            elif len(best_path) > len(current_path):
                best_path = current_path
            continue

        children = [x for x in [current.north, current.south, current.east, current.west] if x]
        for child in children:
            new_search_path = current_path.copy()
            new_search_path.append(child)
            to_visit.append(new_search_path)
    print("best_path")
    print(", ".join([f"{p.x_value}|{p.y_value}" for p in best_path]))
    return f"Found the end {len(best_path) - 1}"


if __name__ == "__main__":
    data, start, end = parse_map(TEST_INPUT_STR)
    print(les_gooooo(INPUT_STR))
