from IO.Parser import Parser
from UCS import UCS

parse_matrix = Parser("graf")
parse_matrix.openAndParse()
matrix = parse_matrix.getMap()

UCS_path = UCS(matrix, 0) # Start Node: 1
UCS_path.find_path_UCS(7) # Goal Node: 8
UCS_path.printPathResult()
print(UCS_path.getDistance())