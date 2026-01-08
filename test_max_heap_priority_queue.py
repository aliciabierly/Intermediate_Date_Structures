import glob, os, importlib, json, pprint
import random

class BadInt(int):
    pass

def toSTR(heap, start):
    root = heap[start]
    N1 = heap[1+start]
    N2 = heap[2+start]
    N3 = heap[3+start]
    N4 = heap[4+start]
    N5 = heap[5+start]
    N6 = heap[6+start] if((6+start) < len(heap)) else ""
    Rep =  f"#                       {root}                        \n"
    Rep += f"#         {N1}                 {N2}         \n"
    Rep += f"#  {N3}  {N4}   {N5}  {N6}  \n"
    return Rep

def heapValidator(heap):
    """
    Description: This method validates the heap.
    Usage:  heapValidator(PQ._heap)
    Returns: tuple. (bool, str)
    Format: (True/False, reason)
    """

    returnValue = (True, "PASSED")
    #Step-01: Varifies that the heap contains tuples of the correct format.
    if(type(heap) != list):
        returnValue = (False, "FAILED: heap must be a list.")
    elif(len(heap) == 0):
        pass
    else:
        start = 1 if(type(heap[0]) != tuple) else 0
        for i in range(start, len(heap), 1):
            if(type(heap[i]) != tuple):
                returnValue = (False, "FAILED: Heap must consist of tuples")
            elif(type(heap[i][0]) != int or heap[i][0] <= 0):
                returnValue = (False, "FAILED: each tuple in the heap must "+\
                "have a positive int as the priority")
            else:
                try:
                    heap[i][1]
                except:
                    returnValue = (False, "FAILED: Incorrectly formatted "+\
                    "tuple. Must have an item to queue")

    #step-02: Validate the heap. (e.g., make sure all nodes obey heap rules)
    #print("\n====================================================================\n")
    #print(f"Current heap: {heap}\n")
    if(returnValue[0] and len(heap) != 0):
        start = 1 if(type(heap[0]) != tuple) else 0
        #print(f"Starting position: {start}\n")
        #print("Heap representation: \n", toSTR(heap, start))
        if(len(heap) > start):
            parentIndex = start
            for i in range(start, len(heap), 1):
                if(i == start):
                    parentIndex = start
                else:
                    if(start == 0):
                        parentIndex = ((i-2)//2) if(i%2==0) else ((i-1)//2)
                    else:
                        parentIndex = ((i)//2) if(i%2==0) else ((i-1)//2)
                if(heap[i][0] > heap[parentIndex][0]):
                    returnValue = (False, f"Invalid heap detected: Child-{i}"+\
                    f" {heap[i]} > parent-{parentIndex} {heap[parentIndex]}")
                    break
    #print("\n====================================================================\n")

    return returnValue

class Lab2Tester():
    """ Simple testing class for lab 2 """

    def __init__(self):
        """ Constructor for the class"""
        self.unitTestResults = ''
        self.score = 0

    def testP1(self, module):
        """ Runs the test on the students codes """
        returnValue = None
        ret = self.test_P2Constructor(module)
        self.test_isEmpty(module, ret[1])
        self.test_isFull(module, ret[1])

        self.test_getParent(module, ret[1])
        self.test_getLeftChild(module, ret[1])
        self.test_getRightChild(module, ret[1])
        self.test_swap(module, ret[1])
        self.test_heapify(module, ret[1])

        self.test_P2Insert(module, ret[1])

        self.test_P2ExtractMax(module, ret[1])

        self.test_P2peekMax(module, ret[1])

        returnValue = True

        self.unitTestResults += '========================================\n'
        self.unitTestResults += 'Total: {}/100'.format(self.score)
        return returnValue

    def test_P2Constructor(self, module):
        """ Test-01: Constructor Validation """
        output = "# Test-01: Valid Constructor Implementation - "
        error = ""
        PQ = None
        hFlag = True
        heap = None
        verdictPQ = True

        try:
            #========================== Test the queue =============================
            if(verdictPQ):
                try:
                    PQ = module.PriorityQueue(50)
                except Exception as e:
                    error += "#    ERROR: Crashed on a valid declaration of a new queue.\n"
                    error += "#        "+str(e)+"\n"
                    verdictPQ = False

            if(verdictPQ):
                try:
                    assert PQ.capacity == 50
                except:
                    error += "#    ERROR: Either <PriorityQueue>.capacity does"
                    error += " not exist or is not set correctly.\n"
                    verdictQ = False

            if(verdictPQ):
                try:
                    assert PQ.currentSize == 0
                except:
                    error += "#    ERROR: Either <PriorityQueue>.currentSize does"
                    error += " not exist or not 0.\n"
                    verdictQ = False

            if(verdictPQ):
                try:
                    heap = PQ._heap
                except:
                    error += "#    ERROR: Required instance variable <PriorityQueue>._heap does not exist\n"
                    hFlag = False
                    try:
                        heap = PQ.heap
                    except:
                        error += "#    ...Tried looking for <PriorityQueue>.heap (most obvious incorrect solution) but couldn't find it."
                        verdictPQ = False

            if(verdictPQ):
                try:
                    assert type(heap) == list
                except:
                    error += "#    ERROR: <PriorityQueue>._heap either does not exist or not a list\n"
                    verdictPQ = False

            if(verdictPQ):
                try:
                    assert len(heap) in [0,1]
                except:
                    error += "#    ERROR: <PriorityQueue>._heap was not properly initialized. (Should be initialized as [<sentinal element>] or [])\n"
                    verdictPQ = False
        except NotImplementedError as e:
            error = '      ERROR: Test failed!\n'

        if(verdictPQ and hFlag):
            output += "PASS [5/5]\n"
            self.unitTestResults += output
            self.score += 5
        else:
            output += "FAIL [0/5]\n"
            self.unitTestResults += output
            self.unitTestResults += error
        return (verdictPQ, hFlag)

    def test_P2Insert(self, module, hFlag):
        """ Test-02: Insert validation """
        output = "# Test-09: Valid insert() Implementation - "
        error = ""
        PQ = None
        _heap = None
        start = None
        verdictPQ = True
        val = "data"
        _heapA = [(30,val), (10, val), (20, val), (5, val), (7, val), (15, val)]
        _heapB = [None, (30,val), (10, val), (20, val), (5, val), (7, val), (15, val)]
        T1 = (25, val)

        #========================== Test the Queue =============================
        try:
            PQ = module.PriorityQueue(10)
            _heap = PQ._heap if(hFlag) else PQ.heap
            start = 0 if(len(_heap) == 0) else 1
        except Exception as e:
            error += "#    FATAL ERROR(1): Unable to make PQ"
            error += " with call PriorityQueue(capacity).\n"
            error += "#        Exception: "+str(repr(e))+"\n"
            verdictPQ = False

        #Test 1 insert on an empty queue
        if(verdictPQ):
            try:
                ret = PQ.insert(T1)
            except Exception as e:
                error += "#    ERROR: Program crashed on valid call to <PriorityQueue>.insert(<tuple>).\n"
                error += "#        Exception: "+str(repr(e))+"\n"
                verdictPQ = False

            if(verdictPQ):
                _heap = PQ._heap if(hFlag) else PQ.heap
                try:
                    assert ret == True
                except:
                    error += "#    ERROR: <PriorityQueue>.insert(<tuple>) did not return True on a valid call to insert when the queue was empty.\n"
                    verdictPQ = False

                try:
                    assert T1 in _heap
                except:
                    error += "#    ERROR: Could not find the recently inserted tuple in heap after <PriorityQueue>.insert(<tuple>).\n"
                    verdictPQ = False

                try:
                    assert PQ.currentSize == 1
                except:
                    error += "#    ERROR: <PriorityQueue>.currentSize should be 1 after insert called on an empty PQ.\n"
                    verdictPQ = False

                try:
                    assert len(_heap) == (1+start)
                except:
                    error += "#    ERROR: Duplicates detected after call to <PriorityQueue>.insert(<tuple>) on an empty queue.\n"
                    verdictPQ = False

        if(verdictPQ):
            try:
                PQ = module.PriorityQueue(10)
                if(hFlag):
                    PQ._heap = _heapA if start == 0 else _heapB
                else:
                    PQ.heap = _heapA if start == 0 else _heapB
                PQ.currentSize = 6
            except Exception as e:
                error += "#    FATAL ERROR(2): Unable to make PQ"
                error += " with call PriorityQueue(capacity).\n"
                error += "#        Exception: "+str(repr(e))+"\n"
                verdictPQ = False

            if(verdictPQ):
                try:
                    ret = PQ.insert(T1)
                    _heap = PQ._heap if(hFlag) else PQ.heap
                except Exception as e:
                    error += "#    ERROR: Crashed on valid call to <PriorityQueue>.insert(<tuple>) when the PQ has nodes in it.\n"
                    error += "#        Exception: "+str(repr(e))+"\n"
                    verdictPQ = False

            if(verdictPQ):
                try:
                    assert ret == True
                except:
                    error += "#    ERROR: <PriorityQueue>.insert(<tuple>) did not return True on a valid call to insert when the queue was not empty.\n"
                    verdictPQ = False

                try:
                    assert T1 in _heap
                except:
                    error += "#    ERROR: Could not find the inserted tuple in the heap after valid call to <PriorityQueue>.insert(<tuple>) on non-empty PQ.\n"
                    verdictPQ = False

                try:
                    assert PQ.currentSize == 7
                except:
                    error += "#    ERROR: <PriorityQueue>.currentSize not updated after insert called on a non-empty queue.\n"
                    verdictPQ = False


                ret = heapValidator(_heap)
                try:
                    assert ret[0], ret[1]
                except:
                    error += f"#    ERROR: Failed heap validation - {ret}.\n"
                    error += toSTR(_heap, start)
                    verdictPQ = False


        if(verdictPQ):
            output += "PASS [20/20]\n"
            self.unitTestResults += output
            self.score += 20
        else:
            output+= "FAIL [0/20]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P2ExtractMax(self, module, hFlag):
        """ Test-03: extractMax validation test """
        output = "# Test-10: Valid extractMax() Implementation - "
        error = ""
        PQ = None
        _heap = None
        start = None
        verdictPQ = True
        val = "data"
        _heapA = [(30,val), (10, val), (20, val), (5, val), (7, val), (15, val), (18, val)]
        _heapB = [None, (30,val), (10, val), (20, val), (5, val), (7, val), (15, val), (18, val)]

        #======================= Test Queue ===================================
        try:
            PQ = module.PriorityQueue(10)
            _heap = PQ._heap if(hFlag) else PQ.heap
            start = 1 if(len(_heap) == 1) else 0
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make PQ"
            error += " with call PriorityQueue(capacity).\n"
            error += "#        Exception: "+str(repr(e))+"\n"
            verdictPQ = False

        if(verdictPQ):
            #test pop with 1 node in queue
            try:
                if(hFlag):
                    PQ._heap = [(30, val)] if start == 0 else [None, (30, val)]
                else:
                    PQ.heap = [(30, val)] if start == 0 else [None, (30, val)]
                PQ.currentSize = 1
            except:
                pass

            try:
                ret = PQ.extractMax()
                _heap = PQ._heap if(hFlag) else PQ.heap
            except Exception as e:
                error += "#    ERROR: Crashed on valid call to <PriorityQueue>.extractMax() when PQ has 1 node\n"
                error += "#        Exception: "+str(repr(e))+"\n"
                verdictPQ = False

            if(verdictPQ):
                try:
                    assert type(ret) == tuple
                    assert ret[0] == 30
                except:
                    error += "#    ERROR: object returned by <PriorityQueue>.extractMax() when queue has 1 node was not what was expected: \n"
                    error += "#    Expected: <tuple> - (30, 'data')\n"
                    error += f"#    Got: {type(ret)} - {ret}\n"
                    verdictPQ = False

                try:
                    assert len(_heap) == start
                except:
                    error += "#    ERROR: The node was not actually removed from the list when <PriorityQueue>.extractMax() called on PQ with 1 node.\n"
                    error += f"#    Current heap: {_heap}"
                    verdictPQ = False

                try:
                    assert PQ.currentSize == 0
                except:
                    error += "#    ERROR: <PriorityQueue>.currentSize should be 0 after <PriorityQueue>.extractMax() called on PQ with 1 node.\n"
                    verdictPQ = False

        if(verdictPQ):
            #test pop with more than 1 node
            if(hFlag):
                PQ._heap = _heapA if start == 0 else _heapB
            else:
                PQ.heap = _heapA if start == 0 else _heapB
            PQ.currentSize = 7

            try:
                ret = PQ.extractMax()
            except Exception as e:
                error += "#    ERROR: Crashed on valid call to extractMax when PQ has more than 1 node\n"
                error += "#        Exception: "+str(repr(e))+"\n"
                verdictPQ = False

            if(verdictPQ):
                _heap = PQ._heap if(hFlag) else PQ.heap
                try:
                    assert type(ret) == tuple
                    assert ret[0] == 30
                except:
                    error += "#    ERROR: object returned by <PriorityQueue>.extractMax() when PQ has 1 node was not what was expected: \n"
                    error += "#    Expected: <tuple> - (30, 'data')\n"
                    error += f"#    Got: {type(ret)} - {ret}\n"
                    verdictPQ = False

                try:
                    assert ret not in _heap
                except:
                    error += "#    ERROR: Max tuple still in the heap after valid call to <PriorityQueue>.extractMax(<tuple>) on non-empty PQ.\n"
                    verdictPQ = False

                try:
                    assert PQ.currentSize == 6
                except:
                    error += "#    ERROR: <PriorityQueue>.currentSize not updated after extractMax called on a non-empty PQ.\n"
                    verdictPQ = False

                try:
                    ret = heapValidator(_heap)
                    assert ret[0], ret[1]
                except:
                    error += f"#    ERROR: Failed heap validation - {ret[1]}.\n"
                    error += toSTR(_heap, start)
                    verdictPQ = False

        if(verdictPQ):
            output += "PASS [20/20]\n"
            self.unitTestResults += output
            self.score += 20
        else:
            output+= "FAIL [0/20]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P2peekMax(self, module, hFlag):
        """ Test-06: Front validation """
        output = "# Test-11: Valid peekMax() Implementation - "
        error = ""
        PQ = None
        _heap = None
        start = None
        res = None
        verdictPQ = True
        val = "data"
        _heapA = [(30,val), (10, val), (20, val), (5, val), (7, val), (15, val), (18, val)]
        _heapB = [None, (30,val), (10, val), (20, val), (5, val), (7, val), (15, val), (18, val)]


        #======================= Test Queue ===================================
        try:
            PQ = module.PriorityQueue(10)
            _heap = PQ._heap if(hFlag) else PQ.heap
            start = 0 if(len(_heap) == 0) else 1
        except Exception as e:
            error += "#    FATAL ERROR(1): Unable to make PQ"
            error += " with call PriorityQueue(capacity).\n"
            error += "#        Exception: "+str(repr(e))+"\n"
            verdictPQ = False

        if(verdictPQ):
            #test-01: call peekMax on empty queue
            try:
                res = PQ.peekMax()
            except Exception as e:
                verdictPQ = False
                error += "#    ERROR: <PriorityQueue>.peekMax() crashed on valid call when PQ is empty.\n"
                error += "#        Exception: "+str(repr(e))+"\n"

            if(verdictPQ):
                try:
                    assert res == False
                except:
                    verdictPQ = False
                    error += "#    Error: <PriorityQueue>.peekMax() returned either True or "
                    error += " non-bool on call when the PQ was empty.\n"
                    if(type(res) != type(True)):
                        error += "#        Returned object of type: "
                        error += str(type(res))+"\n"
                    else:
                        error += "#        Returned: "+str(res)+"\n"

            if(verdictPQ):
                if(hFlag):
                    PQ._heap = _heapA if start == 0 else _heapB
                else:
                    PQ.heap = _heapA if start == 0 else _heapB
                PQ.currentSize = 7

                #find max ticket and return id
                try:
                    res = PQ.peekMax()
                except Exception as e:
                    verdictQ = False
                    error += "#    ERROR: <PriorityQueue>.peekMax() crashed on valid call"
                    error += " when the PQ had elements.\n"
                    error += "#        Exception: "+str(repr(e))+"\n"

                #output from peek should be ticket with highest id, check it.
                if(verdictPQ):
                    _heap = PQ._heap if(hFlag) else PQ.heap
                    try:
                        assert res[0] == 30
                    except:
                        error += "#    ERROR: <PriorityQueue>.peekMax() returned either <False> or the wrong item on valid call.\n"
                        error += f"#        Expected: (30, 'data') - Got: {res} - return type: {type(res)}\n"
                        verdictPQ = False

                if(verdictPQ):
                    try:
                        assert len(_heap) == 7
                        assert PQ.currentSize == 7
                    except:
                        error += "#    ERROR: The size of the heap changed when it shouldn't have after valid call to <PriorityQueue>.peekMax()\n"
                        verdictPQ = False

                if(verdictPQ):
                    try:
                        crtl = _heapA if start == 0 else _heapB
                        for i in range(len(crtl)):
                            assert crtl[i][0] == _heap[i][0]
                    except:
                        error += "#    ERROR: The shape of the heap should not have changed after call to <PriorityQueue>.peekMax()"

        if(verdictPQ):
            output += "PASS [5/5]"+"\n"
            self.unitTestResults += output
            self.score += 5
        else:
            output+= "FAIL [0/5]"+"\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_getParent(self, module, hFlag):
        output = "# Test-04: Valid getParent() Implementation - "
        error = ''
        try:
            PQ = module.PriorityQueue(1000)
            for i in range(100):
                gold_parent = i
                left_child = 2 * i + 1
                right_child = 2 * i + 2

                pred_parent_l = PQ.getParent(left_child)
                pred_parent_r = PQ.getParent(right_child)

                if pred_parent_l != gold_parent:
                    error += '      ERROR: {} is not the correct parent for child {}'.format(pred_parent_l, left_child) + '\n'
                    break

                if pred_parent_r != gold_parent:
                    error += '      ERROR: {} is not the correct parent for child {}'.format(pred_parent_r, right_child) + '\n'
                    break
        except Exception as e:
            error = '      ERROR: Test failed!\n'

        if len(error) == 0:
            output += 'PASS [5/5]\n'
            self.unitTestResults += output
            self.score += 5
        else:
            output += 'Fail [0/5]\n'
            self.unitTestResults += output
            self.unitTestResults += error


    def test_getLeftChild(self, module, hFlag):
        output = "# Test-05: Valid getLeftChild() Implementation - "
        error = ''
        try:
            PQ = module.PriorityQueue(1000)
            for i in range(100):
                gold_parent = i
                left_child = 2 * i + 1

                pred_left_child = PQ.getLeftChild(gold_parent)

                if pred_left_child != left_child:
                    error += '      ERROR: {} is not the correct left child for parent {}'.format(pred_left_child, gold_parent) + '\n'
                    break

        except Exception as e:
            error = '      ERROR: Test failed!\n'

        if len(error) == 0:
            output += 'PASS [5/5]\n'
            self.unitTestResults += output
            self.score += 5
        else:
            output += 'Fail [0/5]\n'
            self.unitTestResults += output
            self.unitTestResults += error
                
    def test_getRightChild(self, module, hFlag):
        output = "# Test-06: Valid getRightChild() Implementation - "
        error = ''
        try:
            PQ = module.PriorityQueue(1000)
            for i in range(100):
                gold_parent = i
                right_child = 2 * i + 2

                pred_right_child = PQ.getRightChild(gold_parent)

                if pred_right_child != right_child:
                    error += '      ERROR: {} is not the correct right child for parent {}'.format(pred_right_child, gold_parent) + '\n'
                    break
        except Exception as e:
            error = '      ERROR: Test failed!\n'


        if len(error) == 0:
            output += 'PASS [5/5]\n'
            self.unitTestResults += output
            self.score += 5
        else:
            output += 'Fail [0/5]\n'
            self.unitTestResults += output
            self.unitTestResults += error

    def test_heapify(self, module, hFlag):
        output = "# Test-08: Valid heapify() Implementation - "
        error = ''

        try:
            PQ = module.PriorityQueue(1000)
            items = list(range(20))

            PQ._heap = [[19, '19'], [18, '18'], [17, '17'], [13, '13'], [15, '15'], [14, '14'], [16, '16'], [10, '10'], [9, '9'], [8, '8'], [3, '3'], [2, '2'], [4, '4'], [11, '11'], [12, '12'], [0, '0'], [6, '6'], [7, '7'], [5, '5'], [1, '1']]
            PQ.currentSize = len(PQ._heap)

            # extract max 
            lastLeafPos = PQ.currentSize - 1
            PQ._heap[0] = PQ._heap[lastLeafPos]
            PQ._heap.pop()
            PQ.currentSize -= 1
            PQ.heapify(0)

            gold_heap = [[18, '18'], [15, '15'], [17, '17'], [13, '13'], [8, '8'], [14, '14'], [16, '16'], [10, '10'], [9, '9'], [1, '1'], [3, '3'], [2, '2'], [4, '4'], [11, '11'], [12, '12'], [0, '0'], [6, '6'], [7, '7'], [5, '5']]

            if not heapValidator(PQ._heap):
                error += '      ERROR: Test failed!'
            else:
                # extract max
                lastLeafPos = PQ.currentSize - 1
                PQ._heap[0] = PQ._heap[lastLeafPos]
                PQ._heap.pop()
                PQ.currentSize -= 1
                PQ.heapify(0)

                gold_heap = [[17, '17'], [15, '15'], [16, '16'], [13, '13'], [8, '8'], [14, '14'], [12, '12'], [10, '10'], [9, '9'], [1, '1'], [3, '3'], [2, '2'], [4, '4'], [11, '11'], [7, '7'], [0, '0'], [6, '6'], [7, '7']]

                if not heapValidator(PQ._heap):
                    error += '      ERROR: Test failed!'
        except Exception as e:
            error = '      ERROR: Test failed!\n'

        if len(error) == 0:
            output += 'PASS [15/15]\n'
            self.unitTestResults += output
            self.score += 15
        else:
            output += 'Fail [0/15]\n'
            self.unitTestResults += output
            self.unitTestResults += error


    def test_swap(self, module, hFlag):
        output = "# Test-07: Valid swap() Implementation - "
        error = ''

        try:
            PQ = module.PriorityQueue(1000)
            for _ in range(100):
                PQ._heap = [(x, x + 1) for x in list(range(100))]

                random.shuffle(PQ._heap)

                i = random.choices(list(range(100)))[0]
                j = random.choices(list(range(100)))[0]

                old_h_i = PQ._heap[i]
                old_h_j = PQ._heap[j]

                PQ.swap(i, j)

                if not (PQ._heap[i] == old_h_j and PQ._heap[j] == old_h_i):
                    error += '      ERROR: Swapping values between positions {} and {} failed:\n'.format(i, j)
                    error += '             - Old values:       heap[{}] = {}, heap[{}] = {}\n'.format(i, old_h_i, j, old_h_j)
                    error += '             - New values:       heap[{}] = {}, heap[{}] = {}\n'.format(i, PQ._heap[i], j, PQ._heap[j])
                    error += '             - Expected values:  heap[{}] = {}, heap[{}] = {}\n'.format(i, old_h_j, j, old_h_i) 
                    break
        except Exception as e:
            error = '      ERROR: Test failed!\n'


        if len(error) == 0:
            output += 'PASS [10/10]\n'
            self.unitTestResults += output
            self.score += 10
        else:
            output += 'Fail [0/10]\n'
            self.unitTestResults += output
            self.unitTestResults += error

    def test_isEmpty(self, module, hFlag):
        output = "# Test-02: Valid isEmpty() Implementation - "
        PQ = None
        verdictPQ = True
        T1 = (30, "data")
        error = ""
        res = None

        #======================= Test Queue ===================================
        try:
            PQ = module.PriorityQueue(10)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make PriorityQueue with call"
            error += " PriorityQueue(capacity).\n"
            error += "#        Exception: "+str(repr(e))+"\n"
            verdictPQ = False

        if(verdictPQ):
            #step-01: test isEmpty
            try:
                res = PQ.isEmpty()
            except Exception as e:
                verdictPQ = False
                error += "#    ERROR: <PriorityQueue>.isEmpty() crashed on valid call.\n"
                error += "#        Exception: "+str(repr(e))+"\n"

            if(verdictPQ):
                try:
                    assert res == True
                except:
                    verdictPQ = False
                    error += "#    Error: <PriorityQueue>.isEmpty() returned either False or"
                    error += " non-bool on call when the PQ was empty.\n"
                    error += f"#        Expected: True - Got: {res} - Type: {type(res)}\n"

            if(verdictPQ):
                if(hFlag):
                    PQ._heap.append(T1)
                else:
                    PQ.heap.append(T1)
                PQ.currentSize = 1
                try:
                    res = PQ.isEmpty()
                except Exception as e:
                    verdictPQ = False
                    error += "#    ERROR: <PriorityQueue>.isEmpty() crashed on valid call when"
                    error += " queue was not empty.\n"
                    error += "#        Exception: "+str(repr(e)) +" \n"

                if(verdictPQ):
                    try:
                        assert res == False
                    except:
                        verdictPQ = False
                        error += "#    Error: <PriorityQueue>.isEmpty() returned either True or "
                        error += " non-bool on call when the PQ was not empty.\n"
                        error += f"#        Expected: False - Got: {res} - Type: {type(res)}\n"


        if(verdictPQ):
            output += "PASS [5/5]\n"
            self.unitTestResults += output
            self.score += 5
        else:
            output+= "FAIL [0/5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_isFull(self, module, hFlag):
        output = "# Test-03: Valid isFull() Implementation - "
        PQ = None
        verdictPQ = True
        T1 = (30, "data")
        error = ""
        res = None

        #======================= Test Queue ===================================
        try:
            PQ = module.PriorityQueue(1)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make PriorityQueue with call"
            error += " PriorityQueue(capacity).\n"
            error += "#        Exception: "+str(repr(e))+"\n"
            verdictPQ = False

        if(verdictPQ):
            #step-01: test isEmpty
            try:
                res = PQ.isFull()
            except Exception as e:
                verdictPQ = False
                error += "#    ERROR: <PriorityQueue>.isFull() crashed on valid call when PQ was not full.\n"
                error += "#        Exception: "+str(repr(e))+"\n"

            if(verdictPQ):
                try:
                    assert res == False
                except:
                    verdictPQ = False
                    error += "#    Error: <PriorityQueue>.isFull() returned either True or"
                    error += " non-bool on call when the PQ was not full.\n"
                    error += f"#        Expected: False - Got: {res} - Type: {type(res)}\n"

            if(verdictPQ):
                if(hFlag):
                    PQ._heap.append(T1)
                else:
                    PQ.heap.append(T1)
                PQ.currentSize = 1
                try:
                    res = PQ.isFull()
                except Exception as e:
                    verdictPQ = False
                    error += "#    ERROR: <PriorityQueue>.isFull() crashed on valid call when"
                    error += " queue was full.\n"
                    error += "#        Exception: "+str(repr(e)) +" \n"

                if(verdictPQ):
                    try:
                        assert res == True
                    except:
                        verdictPQ = False
                        error += "#    Error: <PriorityQueue>.isFull() returned either False or "
                        error += " non-bool on call when the PQ was not empty.\n"
                        error += f"#        Expected: True - Got: {res} - Type: {type(res)}\n"

        if(verdictPQ):
            output += "PASS [5/5]\n"
            self.unitTestResults += output
            self.score += 5
        else:
            output+= "FAIL [0/5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P2ExtraCredit(self, module, hFlag):
        """ Extra Credit test """
        output = "#\n# Section-3 (Extra Credit): Sorted Array (heap_sort) - "
        error = ""
        PQ = None
        verdict = True

        try:
            PQ = module.PriorityQueue(20)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make PQ with call"
            error += " PriorityQueue(capacity).\n"
            error += "#        Exception: "+str(repr(e))+"\n"
            PQ = False

        if(PQ != False):
            v = "data"
            lst = [(2, v), (30, v), (27, v), (18, v), (1, v), (19, v), (36, v), (9, v), (12, v), (22, v)]
            crtl = sorted(lst, key=lambda item: item[0], reverse=True)
            crt2 = sorted(lst, key=lambda item: item[0], reverse=False)
            res = None
            res1 = None

            try:
                HS = PQ.heapSort
            except Exception as e:
                error += "#    ERROR: <PriorityQueue>.heapSort(self, array) not implemented.\n"
                error += "#        Exception: "+repr(e)+"\n"
                verdict = False

            if(verdict):
                try:
                    module.HeapSortInputError
                except:
                    error += "#    ERROR: Could not find required exception - HeapSortInputError\n"
                    verdict = False

            if(verdict):
                try:
                    res1 = PQ.heapSort(None)
                except module.HeapSortInputError:
                    pass
                except Exception as e:
                    error += "#    ERROR: Crashed on call to <PriorityQueue>.heapSort(<invalid input>). Either:\n"
                    error += "#        A) You don't validate input.\n"
                    error += "#        B) Some other reason (See exception below)\n"
                    error += "#        Exception: "+repr(e)+"\n"
                    verdict = False

        if(verdict):
            try:
                res = PQ.heapSort(lst)
                assert type(res) == list
            except:
                error += "#    ERROR: <PriorityQueue>.heapSort() ether crashed on valid input"
                error += " or returned false when it shouldn't.\n"
                error += "#    returned: "+str(res)+"\n"
                verdict = False

        if(verdict):
            try:
                for i in range(len(lst)):
                    assert (res[i] == crtl[i]) or (res[i] == crt2[i])
            except:
                error += "#    ERROR: Array not properly sorted (see lists below):\n"
                error += f"#    Your array:          {res}\n"
                error += f"#    Sorted (Ascending):  {crtl}\n"
                error += f"#    Sorted (Descending): {crt2}\n"
                verdict = False

        if(verdict):
            output += "PASS"+"\n"
            self.unitTestResults += output
        else:
            output+= "FAIL"+"\n"
            self.unitTestResults += output
            self.unitTestResults += error

if __name__ == "__main__":
    test = Lab2Tester()
    import lab2 as module
    test.testP1(module)
    print(test.unitTestResults)
