class Graph:
    """A simple graph class using an adjacency list."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a new vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def get_neighbors(self, vertex):
        """Get the neighbors of a vertex."""
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

    def shortest_path(self, start_vertex, end_vertex):
        """
        Find the shortest path between two vertices using BFS.

        Args:
            start_vertex (any): The starting vertex.
            end_vertex (any): The ending vertex.

        Returns:
            list or None: The shortest path as a list of vertices, or None if no path is found.
        """
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None

        visited = set()
        queue = [(start_vertex, [start_vertex])]

        while queue:
            current_vertex, path = queue.pop(0)

            if current_vertex == end_vertex:
                return path

            if current_vertex not in visited:
                visited.add(current_vertex)

                for neighbor in self.graph[current_vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None
