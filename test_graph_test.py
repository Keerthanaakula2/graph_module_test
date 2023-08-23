import pytest
from graph_module import Graph

# Create a fixture for the graph instance
@pytest.fixture
def graph_instance():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)
    return graph

# Test shortest_path function
def test_shortest_path_existing_path(graph_instance):
    shortest_path = graph_instance.shortest_path(1, 3)
    assert shortest_path == [1, 2, 3]

def test_shortest_path_no_path(graph_instance):
    shortest_path = graph_instance.shortest_path(1, 5)
    assert shortest_path is None

def test_shortest_path_same_vertex(graph_instance):
    shortest_path = graph_instance.shortest_path(1, 1)
    assert shortest_path == [1]

# Run the tests
if __name__ == '__main__':
    pytest.main()
