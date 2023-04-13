import heapq
import pygame
import sys
# Set up Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Optimizing Routes with Pygame')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255) 

# Font
font = pygame.font.SysFont(None, 24)
def draw_graph():
    for node, edges in graph.items():
        node_x, node_y = positions[node]
        pygame.draw.circle(screen, GREEN, (node_x, node_y), 20)
        text = font.render(node, True, BLACK)
        text_rect = text.get_rect(center=(node_x, node_y))
        screen.blit(text, text_rect)
        for neighbor, cost in edges.items():
            neighbor_x, neighbor_y = positions[neighbor]
            pygame.draw.line(screen, BLUE, (node_x, node_y), (neighbor_x, neighbor_y), 2)
            text = font.render(str(cost), True, WHITE)
            text_rect = text.get_rect(center=((node_x + neighbor_x) / 2, (node_y + neighbor_y) / 2))
            screen.blit(text, text_rect)

# def dijkstra(graph, start, end):
#     heap = [(0, start)]
#     visited = set()
#     while heap:
#         (cost, node) = heapq.heappop(heap)
#         if node not in visited:
#             visited.add(node)
#             if node == end:
#                 return cost
#             for (neighbor, c) in graph[node].items():
#                 if neighbor not in visited:
#                     heapq.heappush(heap, (cost + c, neighbor))
#     return -1
# Dijkstra's algorithm
def dijkstra(graph, start, end):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return (cost, path)
            for neighbor, neighbor_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + neighbor_cost, neighbor, path))
    return None

graph = {
    'A': {'B': 2, 'C': 4, 'D': 1, 'E': 3, 'F': 7},
    'B': {'A': 2, 'C': 1, 'E': 3, 'G': 6},
    'C': {'A': 4, 'B': 1, 'D': 2, 'E': 5},
    'D': {'A': 1, 'C': 2, 'E': 1, 'H': 4},
    'E': {'A': 3, 'B': 3, 'C': 5, 'D': 1, 'G': 2, 'I': 4},
    'F': {'A': 7, 'G': 1, 'J': 2},
    'G': {'B': 6, 'E': 2, 'F': 1, 'H': 3, 'J': 4},
    'H': {'D': 4, 'G': 3, 'I': 2},
    'I': {'E': 4, 'H': 2, 'J': 1},
    'J': {'F': 2, 'G': 4, 'I': 1}
}
positions = {
    'A': (100, 100),
    'B': (400, 100),
    'C': (250, 150),
    'D': (100, 400),
    'E': (400, 400),
    'F': (50, 250),
    'G': (600, 200),
    'H': (600, 500),
    'I': (750, 250),
    'J': (700, 50)
}

start = input("Enter start node: ")
end = input("Enter end node: ")
intermediate_nodes = input("Enter intermediate nodes separated by space: ").split()

prev_node = start
total_cost = 0
for node in intermediate_nodes:
    cost,path = dijkstra(graph, prev_node, node)
    if cost == -1:
        print(f"No path found between {prev_node} and {node}")
        break
    total_cost += cost
    prev_node = node

cost,path = dijkstra(graph, prev_node, end)
if cost == -1:
    print(f"No path found between {prev_node} and {end}")
else:
    total_cost += cost
    print(f"Shortest path from {start} to {end} with intermediate nodes {intermediate_nodes}: {total_cost}")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw graph
    screen.fill(BLACK)
    draw_graph()

    # Draw shortest path
    if cost is not None:
        for i in range(len(path) - 1):
            start_x, start_y = positions[path[i]]
            end_x, end_y = positions[path[i+1]]
            pygame.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 5)

    pygame.display.update()