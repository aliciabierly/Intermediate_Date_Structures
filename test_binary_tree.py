from lab3 import BinarySearchTree 

def it_check(bst):
    elements = []
    _it_check(bst.root, elements)
    return elements

def _it_check(current, elements):
    if current is not None:
        _it_check(current.left, elements)
        elements.append(current.value)
        _it_check(current.right, elements)

def test_insert(bst):
    # Test case 1: Insert into empty BST
    bst.insert(10)
    assert it_check(bst) == [10], "Test case 1 failed"

    # Test case 2: Insert smaller element
    bst.insert(5)
    assert it_check(bst) == [5, 10], "Test case 2 failed"

    # Test case 3: Insert larger element
    bst.insert(20)
    assert it_check(bst) == [5, 10, 20], "Test case 3 failed"
    

def test_delete(bst):
    # Setup
    bst.insert(15)  # Ensure tree is correct for delete tests

    # Test case 1: Delete leaf node
    bst.delete(20)
    assert it_check(bst) == [5, 10, 15], "Test case 1 failed"

    # Test case 2: Delete node with one child
    bst.delete(15)
    assert it_check(bst) == [5, 10], "Test case 2 failed"

    # Test case 3: Delete node with two children
    bst.insert(15)
    bst.insert(20)
    bst.delete(10)
    assert it_check(bst) == [5, 15, 20], "Test case 3 failed"

def test_find(bst):
    # Test case 1: Find existing value
    assert bst.find(5) == True, "Test case 1 failed"

    # Test case 2: Find non-existing value
    assert bst.find(99) == False, "Test case 2 failed"

    # Test case 3: Find value after deletion
    bst.delete(5)  # Adjust setup for this specific test
    assert bst.find(5) == False, "Test case 3 failed"
    

def test_inorder_traversal(bst):
    # Reset BST for traversal tests
    bst.root = None
    bst.insert(10)

    # Test case 1: Empty tree
    bst.root = None  # Reset tree to empty
    assert bst.inorder_traversal() == [], "Test case 1 failed"

    # Test case 2: Tree with one element
    bst.insert(10)
    assert bst.inorder_traversal() == [10], "Test case 2 failed"

    # Test case 3: Tree with multiple elements
    bst.insert(5)
    bst.insert(20)
    assert bst.inorder_traversal() == [5, 10, 20], "Test case 3 failed"
    

# Main function to run all tests
def run_tests():
    total_score = 0
    print('=' * 80)
    try:
        bst = BinarySearchTree()
        assert bst.root is None
        print('Test-01: Constructor Implementation - PASSED [5/5]')
        total_score += 5
    except:
        print('Test-01: Constructor Implementation - FAILED [0/5]')

    try:
        test_insert(bst)
        total_score += 30
        print('Test-02: Insert Implementation - PASSED [30/30]')
    except:
        print('Test-02: Insert Implementation - FAILED [0/30]')
    
    try:
        test_delete(bst)
        total_score += 30
        print('Test-03: Delete Implementation - PASSED [30/30]')
    except:
        print('Test-03: Delete Implementation - FAILED [0/30]')


    try:
        test_find(bst)
        total_score += 20
        print('Test-04: Find Implementation - PASSED [20/20]')
    except:
        print('Test-04: Find Implementation - FAILED [0/20]')

    try:
        test_inorder_traversal(bst)
        total_score += 15
        print('Test-05: Inorder Traversal Implementation - PASSED [15/15]')
    except:
        print('Test-05: Inorder Traversal Implementation - FAILED [0/15]')

    print('=' * 80)
    print('Total: {}/100'.format(total_score))
   

if __name__ == '__main__':
    run_tests()
