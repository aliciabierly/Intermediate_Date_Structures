from lab4 import RedBlackTree, TreeNode
import sys

if len(sys.argv) >= 2:
    tmp = sys.argv[1]
    if tmp == 'debug':
        DEBUG = True
else:
    DEBUG = False


def it_check(bst):
    elements = []
    _it_check(bst.root, elements)
    return elements

def _it_check(current, elements):
    if current is not None and current.key is not None:
        _it_check(current.left, elements)
        elements.append(current.key)
        _it_check(current.right, elements)

class TestRedBlackTree:
    def __init__(self):
        self.score = 0
    
    def search(self, tree, k):
        x = tree.root
        while x and x.key is not None:
            if x.key == k:
                return True
            elif k < x.key:
                x = x.left
            else:
                x = x.right
        return False
    
    def run(self):
        if DEBUG:
            #self.test_insert_and_validate_properties()
            self.test_delete_and_validate_properties()
        else:
            try:
                self.test_insert_and_validate_properties()
                print('Test-01: INSERT Implementation - PASSED [50/50]')
                self.score += 50
            except:
                print('Test-01: INSERT Implementation - FAILED [0/50]')
                
            try:
                self.test_delete_and_validate_properties()
                print('Test-02: DELETE Implementation - PASSED [50/50]')
                self.score += 50
            except:
                print('Test-02: DELETE Implementation - FAILED [0/50]')
            
            print('=' * 50)
            print('Total: {}/100'.format(self.score))

    def assertIsNotNone(self, node):
        assert node is not None

    def assertEqual(self, key1, key2):
        assert key1 == key2

    def assertIn(self, x, tlist):
        assert x in tlist

    def setUp(self):
        self.tree = RedBlackTree()
        assert self.tree.NIL is not None
        assert self.tree.NIL.color == 'black'
        assert self.tree.NIL.left is None
        assert self.tree.NIL.right is None
        assert self.tree.root == self.tree.NIL

    def test_insert_and_validate_properties(self):
        self.setUp()
        keys = [20, 15, 25, 10, 17, 22, 27]
        for key in keys:
            self.tree.insert(key)

        for key in keys:
            result = self.search(self.tree, key)
            assert result is True

        self.validate_rb_tree_properties(self.tree)

        elements = it_check(self.tree)
        assert elements == [10, 15, 17, 20, 22, 25, 27], 'wrong order: {}'.format(elements)

    def create_manual_tree(self, nodes_info):
        """
        Manually creates a tree based on a dictionary of nodes information.
        The dictionary keys are node keys, and values are tuples containing
        the parent key, left child key, right child key, and color.
        Use None for missing parents or children and 'b' or 'r' for colors.
        """
        nodes = {}
        for key, (parent_key, left_key, right_key, color) in nodes_info.items():
            node = TreeNode(key)
            node.color = 'black' if color == 'b' else 'red'
            nodes[key] = node

        for key, (parent_key, left_key, right_key, color) in nodes_info.items():
            node = nodes[key]
            node.p = nodes.get(parent_key, self.tree.NIL)
            node.left = nodes.get(left_key, self.tree.NIL)
            node.right = nodes.get(right_key, self.tree.NIL)

        # Finding root
        for node in nodes.values():
            if node.p == self.tree.NIL:
                self.tree.root = node
                break


    def test_delete_and_validate_properties(self):
        self.setUp()
        keys = [20, 15, 25, 10, 17, 22, 27]

        nodes_info = {
            20: (None, 15, 25, 'b'),
            15: (20, 10, 17, 'r'),
            25: (20, 22, 27, 'r'),
            10: (15, None, None, 'b'),
            17: (15, None, None, 'b'),
            22: (25, None, None, 'b'),
            27: (25, None, None, 'b')
        }
        self.create_manual_tree(nodes_info)

        result = self.tree.delete(15)
        assert result == True, 'deletion is not successful'
        self.validate_rb_tree_properties(self.tree)

        elements = it_check(self.tree)
        assert elements == [10, 17, 20, 22, 25, 27], 'wrong order: {}'.format(elements)

        result = self.tree.delete(22)
        assert result == True, 'deletion is not successful'
        self.validate_rb_tree_properties(self.tree)

        elements = it_check(self.tree)
        assert elements == [10, 17, 20, 25, 27], 'wrong order: {}'.format(elements)

        result = self.tree.delete(100)
        self.assertEqual(result, False)

        assert elements == [10, 17, 20, 25, 27], 'wrong order: {}'.format(elements)


    def validate_rb_tree_properties(self, tree):
        self.validate_property_1(tree.root)
        self.validate_property_2(tree.root)
        self.validate_property_4(tree)
        black_count_path = [0]
        self.validate_property_5(tree.root, 0, black_count_path)

    def validate_property_1(self, node):
        # Every node is either red or black
        if node is not None:
            self.assertIn(node.color, ["red", "black"])
            self.validate_property_1(node.left)
            self.validate_property_1(node.right)

    def validate_property_2(self, node):
        # The root is always black
        self.assertEqual(self.tree.root.color, "black")

    def validate_property_4(self, tree):
        # get all red nodes
        red_nodes = []
        stack = [tree.root]
        visited = set()
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited and current is not None:
                visited.add(current)

                if current.color == 'red':
                    red_nodes.append(current)

                if current.left is not None:
                    stack.append(current.left)
                if current.right is not None:
                    stack.append(current.right)

        # Red nodes cannot have red children
        for node in red_nodes:
            if node.left is not None:
                self.assertEqual(node.left.color, "black")
            if node.right is not None:
                self.assertEqual(node.right.color, "black")

    def validate_property_5(self, node, current_count, path_counts):
        # All paths from a node to its NIL descendants contain the same number of black nodes
        if node.color == "black":
            current_count += 1

        if node is None or node == self.tree.NIL:
            if path_counts[0] == 0:
                path_counts[0] = current_count
            else:
                self.assertEqual(path_counts[0], current_count)
            return

        self.validate_property_5(node.left, current_count, path_counts)
        self.validate_property_5(node.right, current_count, path_counts)

if __name__ == "__main__":
    tester = TestRedBlackTree()
    tester.run()
