import cv2
import numpy as np
import matplotlib.pyplot as plt
from heapq import heappush, heappop

def find_path(image, start, end):
    rows, cols = image.shape[0], image.shape[1]
    distances = np.full((rows, cols), float('inf')) # shortest dist from st to every pt
    distances[start[1], start[0]] = 0 # start[1] for row and start[0] for column
    parents = np.full((rows, cols, 2), -1)
    
    # Priority queue entries: (distance, (x, y))
    pq = [(0, start)]
    visited = set()
    
    # Possible movements: up, down, right, left
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    

    # For each point:

    #     1. Skip if already visited
    #     2. add to visited if not
    #     3. Break if end point reached

    #     4. For each neighbor:

    #         Check if within bounds and unvisited
    #         Calculate new distance based on pixel differences
    #         Update distance and parent if shorter path found
    #         Add to priority queue


    while pq:
        dist, (x, y) = heappop(pq)
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        
        if (x, y) == end:
            break
            
        # Check all neighbors
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < cols and 0 <= new_y < rows and (new_x, new_y) not in visited: # should be inside image and unexplored
                # Calculate new distance cost based on pixel difference
                # this part will make agent avoid walls
                pixel_diff = np.sum((image[new_y, new_x] - image[y, x]) ** 2)
                new_dist = dist + pixel_diff + 0.1
                
                # this checks if we have  found a better path to new_x and new_y 
                '''
                Example
                We find a path to (2,3) with distance 10:
                new_dist = 10
                # Since 10 < infinity:
                distances[3,2] = 10  # Update with shorter distance
                parents[3,2] = [1,3]  # assume we came from point (1,3)
                heappush(pq, (10, (2,3)))  # Add to priority queue for exploration
                '''
                if new_dist < distances[new_y, new_x]:
                    distances[new_y, new_x] = new_dist
                    parents[new_y, new_x] = [x, y]
                    heappush(pq, (new_dist, (new_x, new_y)))
    
    # Reconstruct path
    path = []
    current = end
    while current != start:
        path.append(current)
        parent_x, parent_y = parents[current[1], current[0]]
        if parent_x == -1:  # No path found as -1 was initialized at first
            return []
        current = (parent_x, parent_y)
    path.append(start)
    return path[::-1]

def draw_path(image, path, color=(0, 255, 0), thickness=1):
    img_copy = image.copy()
    for i in range(len(path) - 1):
        cv2.line(img_copy, path[i], path[i + 1], color, thickness)
    return img_copy

def solve_maze(image_path, start_point, end_point):
    # Read and mark the image
    img = cv2.imread(image_path)
    cv2.circle(img, start_point, 2, (0, 0, 255), -1)  # takes (image, (co-ord), radius,color,thickness)
    cv2.circle(img, end_point, 2, (255, 0, 0), -1)   
    
    # Find and draw path
    path = find_path(img, start_point, end_point)
    if path:
        img = draw_path(img, path)
        
    return img

if __name__ == "__main__":
    maze_path = 'maze.png'
    start = (192, 5)
    end = (210, 403)
    
    result = solve_maze(maze_path, start, end)
    
    plt.figure(figsize=(7, 7))
    plt.imshow(result)
    plt.show()