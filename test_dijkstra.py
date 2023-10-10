import unittest
import dijkstra

class TestDijkstra(unittest.TestCase):

        # EDGES IN FORMAT [u, v, w] 
        # u is the source vertex 
        # v is the destination vertex
        # w is the weight of the edge

    def test_instance(self):

        n=3
        edges=[[0,1,4]]
        src=0
        self.assertNotIsInstance(dijkstra.dijkstra(n, edges, src), list)
        self.assertIsInstance(dijkstra.dijkstra(n, edges, src), dict)
    
    def test_values(self):

        n=3
        edges=[[0,1,4]]
        src=0
        self.assertEqual(dijkstra.dijkstra(n, edges, src), {0: 0, 1: 4, 2: -1})

        n=5
        edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]]
        src=0
        self.assertEqual(dijkstra.dijkstra(n, edges, src), {0: 0, 1: 7, 2: 3, 3: 11, 4: 5})

        n=4
        edges=[[0,1,3],[1,2,8],[2,3,4],[3,0,2]]
        src=0
        self.assertEqual(dijkstra.dijkstra(n, edges, src), {0: 0, 1: 3, 2: 11, 3: 15})

        n=5
        edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]]
        src=4
        self.assertEqual(dijkstra.dijkstra(n, edges, src), {0: -1, 1: -1, 2: -1, 3: -1, 4: 0})



if __name__ == '__main__':
    unittest.main()