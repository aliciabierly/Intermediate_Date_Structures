import glob, os, importlib, json, pprint
import lab1 as module


class BadInt(int):
    pass


class Lab1Tester():
    """ Simple testing class for lab 1 """

    def __init__(self):
        """ Constructor for the class"""
        self.unitTestResults = ""
        self.score = 0


    def open(self, opt):
        msg = " Unit Testing Results (Complex) "
        ln = (78 - len(msg)) // 2
        self.unitTestResults += "#=" + ("=" * ln) + msg + ("=" * ln) + "\n"

    def close(self):
        msg = " End of Testing "
        ln = (78 - len(msg)) // 2
        self.unitTestResults += "#=" + ("=" * ln) + msg + ("=" * ln) + "\n"
        self.unitTestResults += 'Total: {}/100.0'.format(self.score)

    def testP1(self, module):
        """ Runs the test on the students codes """
        returnValue = None
        self.open(True)

        self.test_P1ConstructorNode(module)

        # Queue tests
        x = self.score
        self.test_P1ConstructorQueue(module)
        y = self.score
        if y - x == 7.5:
            self.test_P1Enqueue(module)
            self.test_P1Dequeue(module)
            self.test_P1Front(module)
            self.test_isEmptyQueue(module)
            self.test_isFullQueue(module)

        y = self.score
        # Stack tests
        self.test_P1ConstructorStack(module)
        z = self.score

        if z - y == 7.5:
            self.test_P1Push(module)
            self.test_P1Pop(module)
            self.test_P1Peek(module)
            self.test_isEmptyStack(module)
            self.test_isFullStack(module)

        self.close()

    def test_P1ConstructorNode(self, module):
        """ Test-01: Constructor Validation """
        output = "# Test-01: Valid Constructor Implementation: Node - "
        error = ""
        N = None
        verdictN = True

        # ========================== Test the node ==============================
        if (verdictN):
            try:
                N = module.Node("data")
            except Exception as e:
                error += "#    ERROR: Crashed on a valid declaration of a new Node.\n"
                error += "#        " + str(e) + "\n"
                verdictN = False

        if (verdictN):
            try:
                assert N.next != "aarrg"
            except:
                error += "#    ERROR: <Node>.next does not exist\n"
                verdictN = False

        if (verdictN):
            try:
                assert N.data == "data"
            except:
                error += "#    ERROR: Either <Node>.data does not exist or not set to proper value.\n"
                verdictN = False

        if (verdictN):
            output += "PASS [10/10]\n"
            self.score += 10
            self.unitTestResults += output
        else:
            output += "FAIL [0/10]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1ConstructorQueue(self, module):
        """ Test-01: Constructor Validation """
        output = '##########################################################\n'
        output += "# Test-02: Valid Constructor Implementation: Queue - "
        error = ""
        Q = None
        verdictQ = True

        # ========================== Test the queue =============================
        if (verdictQ):
            try:
                Q = module.Queue(50)
            except Exception as e:
                error += "#    ERROR: Crashed on a valid declaration of a new queue.\n"
                error += "#        " + str(e) + "\n"
                verdictQ = False

        if (verdictQ):
            try:
                assert Q.currentSize == 0
            except:
                error += "#    ERROR: Either <Queue>.currentSize does"
                error += " not exist or not 0.\n"
                verdictQ = False

        if (verdictQ):
            try:
                assert Q.head != "Arrrggg Braaaaains! (fo.O)f"
            except:
                error += "#    ERROR: <Queue>.head does not exist\n"
                verdictQ = False

        if (verdictQ):
            try:
                assert Q.tail != "Arrrggg Braaaaains! (fo.O)f"
            except:
                error += "#    ERROR: <Queue>.tail does not exist\n"
                verdictQ = False

        if (verdictQ):
            try:
                assert Q.capacity == 50
            except:
                error += "#    ERROR: Either <Queue>.capacity does"
                error += " not exist or is not set correctly.\n"
                verdictQ = False

        if (verdictQ): 
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error


    def test_P1ConstructorStack(self, module):
        """ Test-01: Constructor Validation """
        output = '##########################################################\n'
        output += "# Test-08: Valid Constructor Implementation: Stack - "
        error = ""
        ST = None
        verdictST = True

        # ========================== Test the stack =============================
        if (verdictST):
            try:
                ST = module.Stack(50)
            except Exception as e:
                error += "#    ERROR: Crashed on a valid declaration of a new stack.\n"
                error += "#        " + str(e) + "\n"
                verdictST = False

        if (verdictST):
            try:
                assert ST.currentSize == 0
            except:
                error += "#    ERROR: Either <Stack>.currentSize does"
                error += " not exist or not 0.\n"
                verdictST = False

        if (verdictST):
            try:
                assert ST.head != "Arrrggg Braaaaains! (fo.O)f"
            except:
                error += "#    ERROR: <Stack>.head does not exist\n"
                verdictST = False

        if (verdictST):
            try:
                assert ST.capacity == 50
            except:
                error += "#    ERROR: Either <Stack>.capacity does"
                error += " not exist or is not set correctly.\n"
                verdictST = False


        if ( verdictST ):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1Enqueue(self, module):
        """ Test-02: Insert validation """
        output = "# Test-03: Valid Queue.enqueue() Implementation - "
        error = ""
        Q = None
        verdictQ = True
        N1 = module.Node(1)
        N2 = module.Node(2)
        N3 = module.Node(3)
        N4 = module.Node(4)
        N1.next = N2
        N2.next = N3
        N3.next = N4
        try:
            N2.prev = N1
            N3.prev = N2
            N4.prev = N3
        except:
            pass
        # ========================== Test the Queue =============================
        try:
            Q = module.Queue(5)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Queue"
            error += " with call Queue(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        # Test 1 enqueue on an empty queue
        try:
            ret = Q.enqueue(1)
        except Exception as e:
            error += "#    ERROR: Program crashed on valid call to enqueue.\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        if (verdictQ):
            try:
                assert ret == True
            except:
                error += "#    ERROR: <Queue>.enqueue(<data>) did not return True on a valid call to enqueue when the queue was empty.\n"
                verdictQ = False

            try:
                assert Q.head is Q.tail
            except:
                error += "#    ERROR: <Queue>.head and <Queue>.tail should point to the same thing after <Queue>.enqueue(<data>) called on an empty queue.\n"
                verdictQ = False

            try:
                assert Q.currentSize == 1
            except:
                error += "#    ERROR: <Queue>.currentSize should be 1 after enqueue called on an empty queue.\n"
                verdictQ = False

            try:
                assert type(Q.head) == module.Node
                assert type(Q.tail) == module.Node
            except:
                error += "#    ERROR: <Queue>.head should be a node after enqueue called on an empty queue.\n"
                verdictQ = False

            try:
                assert Q.head.data == 1
            except:
                error += "#    ERROR: The data in the Node was not properly set after <Queue>.enqueue(1). (i.e., <Queue>.head.data == 1)\n"
                verdictQ = False

        if (verdictQ):
            try:
                Q = module.Queue(6)
                Q.head = N1
                Q.tail = N4
                Q.currentSize = 4
            except:
                pass

            try:
                ret = Q.enqueue(5)
            except:
                error += "#    ERROR: Crashed on valid call to enqueue when the queue has nodes in it.\n"
                verdictQ = False

            if (verdictQ):
                try:
                    assert ret == True
                except:
                    error += "#    ERROR: <Queue>.enqueue(<data>) did not return True on a valid call to enqueue when the queue was not empty.\n"
                    verdictQ = False

                try:
                    assert Q.head is N1
                except:
                    error += "#    ERROR: <Queue>.head is not the node it should be after <Queue>.enqueue(<data>) called on an non-empty queue.\n"
                    verdictQ = False

                try:
                    assert Q.currentSize == 5
                except:
                    error += "#    ERROR: <Queue>.currentSize not updated after enqueue called on a non-empty queue.\n"
                    verdictQ = False

                try:
                    assert type(Q.head) == module.Node
                    assert type(Q.tail) == module.Node
                except:
                    error += "#    ERROR: <Queue>.head and <Queue>.tail should be a node after enqueue called on an empty queue.\n"
                    verdictQ = False

                try:
                    assert Q.head.data == 1
                    assert Q.tail.data == 5
                except:
                    error += "#    ERROR: The data in the Node was not properly set after <Queue>.enqueue(5). (i.e., <Queue>.head.data == 1 and <Queue>.tail.data == 5)\n"
                    verdictQ = False

                try:
                    assert N4.next.data == 5
                except:
                    error += "#    ERROR: Node not actually added to linked list. Did you not set the tail's next to point to a new node?\n"
                    verdictQ = False

        if (verdictQ):
            try:
                Q = module.Queue(6)
                inp = [1, 2, 3, 4, 5, 6]
                check = [1, 2, 3, 4, 5, 6]
                ret = []
                st1 = []
            except:
                pass

            for item in inp:
                try:
                    ret.append(Q.enqueue(item))
                except Exception as e:
                    error += "#    ERROR: Failed to enqueue item from FIFO test list.\n"
                    error += "#        Exception: " + str(repr(e)) + "\n"
                    verdictQ = False

            if (verdictQ):
                i = 0
                cur = Q.head
                while (i < 6):
                    st1.append(cur.data)
                    i += 1
                    cur = cur.next

                for i in range(len(check)):
                    try:
                        assert check[i] == st1[i]
                        assert ret[i] == True
                    except:
                        error += "#    ERROR: Failed FIFO test.\n"
                        error += f"#    Expected: {lst}\n"
                        error += f"#    Got: {st1}\n"
                        verdictST = False
                        break

        if (verdictQ): 
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1Push(self, module):
        """ Test-02: Insert validation """
        output = "# Test-09: Valid Stack.push() Implementation - "
        error = ""
        ST = None
        verdictST = True
        # ============================ Test the stack ===========================
        N1 = module.Node(1)
        N2 = module.Node(2)
        N3 = module.Node(3)
        N4 = module.Node(4)
        N4.next = N3
        N3.next = N2
        N2.next = N1
        try:
            N1.prev = N2
            N2.prev = N3
            N3.prev = N4
        except:
            pass

        try:
            ST = module.Stack(5)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Stack"
            error += " with call Stack(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictST = False

        # Test 1 enqueue on an empty queue
        try:
            ret = ST.push(1)
        except Exception as e:
            error += "#    ERROR: Program crashed on valid call to push.\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictST = False

        if (verdictST):
            try:
                assert ret == True
            except:
                error += "#    ERROR: <Stack>.push(<data>) did not return True on a valid call to push when the stack was empty.\n"
                verdictST = False

            try:
                assert ST.currentSize == 1
            except:
                error += "#    ERROR: <Stack>.currentSize should be 1 after push called on an empty stack.\n"
                verdictST = False

            try:
                assert type(ST.head) == module.Node
            except:
                error += "#    ERROR: <Stack>.head should be a node after push called on an empty stack.\n"
                verdictST = False

            try:
                assert ST.head.data == 1
            except:
                error += "#    ERROR: The data in the Node was not properly set after <Stack>.push(1). (i.e., <Stack>.head.data == 1)\n"
                verdictST = False

        if (verdictST):
            try:
                ST = module.Stack(6)
                ST.head = N4
                ST.currentSize = 4
            except:
                pass

            try:
                ret = ST.push(5)
            except:
                error += "#    ERROR: Crashed on valid call to push when the stack has nodes in it.\n"
                verdictST = False

            if (verdictST):
                try:
                    assert ret == True
                except:
                    error += "#    ERROR: <Stack>.push(<data>) did not return True on a valid call to push when the stack was not empty.\n"
                    verdictST = False

                try:
                    assert ST.currentSize == 5
                except:
                    error += "#    ERROR: <Stack>.currentSize not updated after push called on a non-empty stack.\n"
                    verdictST = False

                try:
                    assert type(ST.head) == module.Node
                except:
                    error += "#    ERROR: <Stack>.head should be a node after push called on an empty stack.\n"
                    verdictST = False

                try:
                    assert ST.head.data == 5
                except:
                    error += "#    ERROR: The data in the Node was not properly set after <Stack>.push(5). (i.e., <Stack>.head.data == 5)\n"
                    verdictST = False

                try:
                    assert ST.head.next is N4
                except:
                    error += "#    ERROR: Node not actually added to linked list. Did you not set the nodes's next to point to the head?\n"
                    verdictST = False

        if (verdictST):
            try:
                ST = module.Stack(6)
                inp = [1, 2, 3, 4, 5, 6]
                check = [6, 5, 4, 3, 2, 1]
                ret = []
                st1 = []
            except:
                pass

            for item in inp:
                try:
                    ret.append(ST.push(item))
                except Exception as e:
                    error += "#    ERROR: Failed to push item from LIFO test list.\n"
                    error += "#        Exception: " + str(repr(e)) + "\n"
                    verdictST = False

            if (verdictST):
                i = 0
                cur = ST.head
                while (i < 6):
                    st1.append(cur.data)
                    i += 1
                    cur = cur.next

                for i in range(len(check)):
                    try:
                        assert check[i] == st1[i]
                        assert ret[i] == True
                    except:
                        error += "#    ERROR: Failed LIFO test.\n"
                        error += f"#    Expected: {lst}\n"
                        error += f"#    Got: {st1}\n"
                        verdictST = False
                        break

        if (verdictST):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1Dequeue(self, module):
        """ Test-03: dequeue/pop validation test """
        output = "# Test-04: Valid Queue.dequeue() Implementation - "
        error = ""
        Q = None
        verdictQ = True

        # ======================= Test Queue ===================================
        try:
            Q = module.Queue(6)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Queue with call"
            error += " Queue(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        if (verdictQ):
            # test pop with 1 node in queue
            N1 = module.Node(1)
            Q.head = Q.tail = N1
            Q.currentSize = 1

            try:
                ret = Q.dequeue()
            except Exception as e:
                error += "#    ERROR: Crashed on valid call to dequeue when queue has 1 node\n"
                error += "#        Exception: " + str(repr(e)) + "\n"
                verdictQ = False

            if (verdictQ):
                try:
                    assert type(ret) == int
                    assert ret == 1
                except:
                    error += "#    ERROR: object returned by <Queue>.dequeue() when queue has 1 node was not what was expected: \n"
                    error += "#    Expected: <int> - 1\n"
                    error += f"#    Got: {type(ret)} - {ret}\n"
                    verdictQ = False

                try:
                    assert Q.head is not N1
                    assert Q.tail is not N1
                except:
                    error += "#    ERROR: The node was not actually removed from the list when <Queue>.dequeue() called on queue with 1 node.\n"
                    verdictQ = False

                try:
                    assert Q.currentSize == 0
                except:
                    error += "#    ERROR: <Queue>.currentSize should be 0 after <Queue>.dequeue() called on queue with 1 node.\n"
                    verdictQ = False

        if (verdictQ):
            # test pop with more than 1 node
            N1 = module.Node(1)
            N2 = module.Node(2)
            N3 = module.Node(3)
            N4 = module.Node(4)
            N1.next = N2
            N2.next = N3
            N3.next = N4
            try:
                N2.prev = N1
                N3.prev = N2
                N4.prev = N3
            except:
                pass

            Q.head = N1
            Q.tail = N4
            Q.currentSize = 4

            try:
                ret = Q.dequeue()
            except Exception as e:
                error += "#    ERROR: Crashed on valid call to dequeue when queue has more than 1 node\n"
                error += "#        Exception: " + str(repr(e)) + "\n"
                verdictQ = False

            if (verdictQ):
                try:
                    assert type(ret) == int
                    assert ret == 1
                except:
                    error += "#    ERROR: object returned by <Queue>.dequeue() when queue has more than 1 node was not what was expected: \n"
                    error += "#    Expected: <int> - 1\n"
                    error += f"#    Got: {type(ret)} - {ret}\n"
                    verdictQ = False

                try:
                    assert Q.head is N2
                    assert Q.tail is N4
                except:
                    error += "#    ERROR: The head/tail were not set to the proper nodes after <Queue>.dequeue() was called on a queue with more than 1 node.\n"
                    verdictQ = False

                try:
                    assert N1.next is not N2
                except:
                    error += "#    ERROR: The node was not actually removed from the linked list after valid call to <Queue>.dequeue()\n"
                    verdictQ = False

        if (verdictQ):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1Pop(self, module):
        """ Test-03: dequeue/pop validation test """
        output = "# Test-10: Valid Stack.pop() Implementation - "
        error = ""
        ST = None
        verdictST = True

        # ======================= Test Stack ===================================
        try:
            ST = module.Stack(6)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Stack with call"
            error += " Stack(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        if (verdictST):
            # test pop with 1 node in queue
            N1 = module.Node(1)
            ST.head = N1
            ST.currentSize = 1

            try:
                ret = ST.pop()
            except Exception as e:
                error += "#    ERROR: Crashed on valid call to pop when stack has 1 node\n"
                error += "#        Exception: " + str(repr(e)) + "\n"
                verdictST = False

            if (verdictST):
                try:
                    assert type(ret) == int
                    assert ret == 1
                except:
                    error += "#    ERROR: object returned by <Stack>.pop() when stack has 1 node was not what was expected: \n"
                    error += "#    Expected: <int> - 1\n"
                    error += f"#    Got: {type(ret)} - {ret}\n"
                    verdictST = False

                try:
                    assert ST.head is not N1
                except:
                    error += "#    ERROR: The node was not actually removed from the list when <Stack>.pop() called on stack with 1 node.\n"
                    verdictST = False

                try:
                    assert ST.currentSize == 0
                except:
                    error += "#    ERROR: <Stack>.currentSize should be 0 after <Stack>.pop() called on stack with 1 node.\n"
                    verdictST = False

        if (verdictST):
            # test pop with more than 1 node
            N1 = module.Node(1)
            N2 = module.Node(2)
            N3 = module.Node(3)
            N4 = module.Node(4)
            N1.next = N2
            N2.next = N3
            N3.next = N4
            try:
                N2.prev = N1
                N3.prev = N2
                N4.prev = N3
            except:
                pass

            ST.head = N1
            ST.currentSize = 4

            try:
                ret = ST.pop()
            except Exception as e:
                error += "#    ERROR: Crashed on valid call to pop when stack has more than 1 node\n"
                error += "#        Exception: " + str(repr(e)) + "\n"
                verdictST = False

            if (verdictST):
                try:
                    assert type(ret) == int
                    assert ret == 1
                except:
                    error += "#    ERROR: object returned by <Stack>.pop() when stack has more than 1 node was not what was expected: \n"
                    error += "#    Expected: <int> - 1\n"
                    error += f"#    Got: {type(ret)} - {ret}\n"
                    verdictST = False

                try:
                    assert ST.head is N2
                except:
                    error += "#    ERROR: The head was not set to the proper node after <Stack>.pop() was called on a stack with more than 1 node.\n"
                    verdictST = False

                try:
                    assert N1.next is not N2
                except:
                    error += "#    ERROR: The node was not actually removed from the linked list after valid call to <Stack>.pop()\n"
                    verdictST = False

        if (verdictST):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1Front(self, module):
        """ Test-06: Front validation """
        output = "# Test-05: Valid Queue.front() Implementation - "
        Q = None
        verdictQ = True
        error = ""

        # ======================= Test Queue ===================================
        try:
            Q = module.Queue(6)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Queue with call"
            error += " Queue(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        if (verdictQ):
            # test-01: call peekMax on empty queue
            try:
                res = Q.front()
            except Exception as e:
                verdictQ = False
                error += "#    ERROR: .front() crashed on valid call to front when queue is empty.\n"
                error += "#        Exception: " + str(repr(e)) + "\n"

            if (verdictQ):
                try:
                    assert res == False
                except:
                    verdictQ = False
                    error += "#    Error: <Queue>.front() returned either True or "
                    error += " non-bool on call when the queue was empty.\n"
                    if (type(res) != type(True)):
                        error += "#        Returned object of type: "
                        error += str(type(res)) + "\n"
                    else:
                        error += "#        Returned: " + str(res) + "\n"

            if (verdictQ):
                N1 = module.Node(1)
                N2 = module.Node(2)
                N1.next = N2
                try:
                    N2.prev = N1
                except:
                    pass
                Q.head = N1
                Q.tail = N2
                Q.currentSize = 2
                if (verdictQ):
                    # find max ticket and return id
                    try:
                        res = Q.front()
                    except Exception as e:
                        verdictQ = False
                        error += "#    ERROR: <Queue>.front() crashed on valid call"
                        error += " when the queue had elements.\n"
                        error += "#        Exception: " + str(repr(e)) + "\n"

                # output from peek should be ticket with highest id, check it.
                if (verdictQ):
                    try:
                        assert res == 1
                    except:
                        error += "#    ERROR: <Queue>.front() returned either <False> or the wrong item on valid call.\n"
                        error += f"#        Expected: 1 - Got: {res} - return type: {type(res)}"
                        verdictQ = False

        if (verdictQ):
            output += "PASS [7.5/7.5]" + "\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]" + "\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_P1Peek(self, module):
        """ Test-06: Front validation """
        output = "# Test-11: Valid Stack.peek() Implementation - "
        ST = None
        verdictST = True
        error = ""

        # ======================= Test Stack ===================================
        try:
            ST = module.Stack(6)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make stack with call"
            error += " Stack(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictST = False

        if (verdictST):
            # test-01: call peekMax on empty queue
            try:
                res = ST.peek()
            except Exception as e:
                verdictST = False
                error += "#    ERROR: <Stack>.peek() crashed on valid call to peek when stack is empty.\n"
                error += "#        Exception: " + str(repr(e)) + "\n"

            if (verdictST):
                try:
                    assert res == False
                except:
                    verdictST = False
                    error += "#    Error: <Stack>.peek() returned either True or "
                    error += " non-bool on call when the stack was empty.\n"
                    if (type(res) != type(True)):
                        error += "#        Returned object of type: "
                        error += str(type(res)) + "\n"
                    else:
                        error += "#        Returned: " + str(res) + "\n"

            if (verdictST):
                N1 = module.Node(1)
                N2 = module.Node(2)
                N1.next = N2
                try:
                    N2.prev = N1
                except:
                    pass
                ST.head = N1
                ST.tail = N2
                ST.currentSize = 2
                if (verdictST):
                    # find max ticket and return id
                    try:
                        res = ST.peek()
                    except Exception as e:
                        verdictST = False
                        error += "#    ERROR: <Stack>.peek() crashed on valid call"
                        error += " when the stack had elements.\n"
                        error += "#        Exception: " + str(repr(e)) + "\n"

                # output from peek should be ticket with highest id, check it.
                if (verdictST):
                    try:
                        assert res == 1
                    except:
                        error += "#    ERROR: <Stack>.peek() returned either <False> or the wrong item on valid call.\n"
                        error += f"#        Expected: 1 - Got: {res} - return type: {type(res)}"
                        verdictST = False

        if (verdictST):
            output += "PASS [7.5/7.5]" + "\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]" + "\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_isEmptyQueue(self, module):
        """ Test-04: empty """
        output = "# Test-06: Valid Queue.isEmpty() Implementation - "
        Q = None
        verdictQ = True
        error = ""

        # ======================= Test Queue ===================================
        try:
            Q = module.Queue(1)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Queue with call"
            error += " Queue(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        if (verdictQ):
            # step-01: test isEmpty
            try:
                res = Q.isEmpty()
            except Exception as e:
                verdictQ = False
                error += "#    ERROR: <Queue>.isEmpty() crashed on valid call.\n"
                error += "#        Exception: " + str(repr(e)) + "\n"

            if (verdictQ):
                try:
                    assert res == True
                except:
                    verdictQ = False
                    error += "#    Error: <Queue>.isEmpty() returned either False or"
                    error += " non-bool on call when the queue was empty.\n"
                    error += f"#        Expected: True - Got: {res} - Type: {type(res)}\n"

            if (verdictQ):
                N1 = module.Node(1)
                Q.head = N1
                Q.tail = N1
                Q.currentSize = 1
                try:
                    res = Q.isEmpty()
                except Exception as e:
                    verdictQ = False
                    error += "#    ERROR: <Queue>.isEmpty() crashed on valid call when"
                    error += " queue was not empty.\n"
                    error += "#        Exception: " + str(repr(e)) + " \n"

                if (verdictQ):
                    try:
                        assert res == False
                    except:
                        verdictQ = False
                        error += "#    Error: <Queue>.isEmpty() returned either True or "
                        error += " non-bool on call when the queue was not empty.\n"
                        error += f"#        Expected: False - Got: {res} - Type: {type(res)}\n"


        if (verdictQ):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_isEmptyStack(self, module):
        """ Test-04: empty """
        output = "# Test-12: Valid Stack.isEmpty() Implementation - "
        ST = None
        verdictST = True
        error = ""

        # ======================= Test Stack ===================================
        try:
            ST = module.Stack(1)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make stack with call"
            error += " Stack(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictST = False

        if (verdictST):
            # step-01: test isEmpty
            try:
                res = ST.isEmpty()
            except Exception as e:
                verdictST = False
                error += "#    ERROR: <Stack>.isEmpty() crashed on valid call.\n"
                error += "#        Exception: " + str(repr(e)) + "\n"

            if (verdictST):
                try:
                    assert res == True
                except:
                    verdictST = False
                    error += "#    Error: <Stack>.isEmpty() returned either False or"
                    error += " non-bool on call when the stack was empty.\n"
                    error += f"#        Expected: True - Got: {res} - Type: {type(res)}\n"

            if (verdictST):
                N1 = module.Node(1)
                ST.head = N1
                ST.tail = N1
                ST.currentSize = 1
                try:
                    res = ST.isEmpty()
                except Exception as e:
                    verdictST = False
                    error += "#    ERROR: <Stack>.isEmpty() crashed on valid call when"
                    error += " stack was not empty.\n"
                    error += "#        Exception: " + str(repr(e)) + " \n"

                if (verdictST):
                    try:
                        assert res == False
                    except:
                        verdictST = False
                        error += "#    Error: <Stack>.isEmpty() returned either True or "
                        error += " non-bool on call when the stack was not empty.\n"
                        error += f"#        Expected: False - Got: {res} - Type: {type(res)}\n"

        if (verdictST):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_isFullQueue(self, module):
        """ Test-04: empty """
        output = "# Test-07: Valid Queue.isFull() Implementation - "
        Q = None
        verdictQ = True
        error = ""

        # ======================= Test Queue ===================================
        try:
            Q = module.Queue(1)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make Queue with call"
            error += " Queue(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictQ = False

        if (verdictQ):
            # step-01: test isEmpty
            try:
                res = Q.isFull()
            except Exception as e:
                verdictQ = False
                error += "#    ERROR: <Queue>.isEmpty() crashed on valid call.\n"
                error += "#        Exception: " + str(repr(e)) + "\n"

            if (verdictQ):
                try:
                    assert res == False
                except:
                    verdictQ = False
                    error += "#    Error: <Queue>.isEmpty() returned either False or"
                    error += " non-bool on call when the queue was empty.\n"
                    error += f"#        Expected: False - Got: {res} - Type: {type(res)}\n"

            if (verdictQ):
                N1 = module.Node(1)
                Q.head = N1
                Q.tail = N1
                Q.currentSize = 1
                try:
                    res = Q.isFull()
                except Exception as e:
                    verdictQ = False
                    error += "#    ERROR: <Queue>.isEmpty() crashed on valid call when"
                    error += " queue was not empty.\n"
                    error += "#        Exception: " + str(repr(e)) + " \n"

                if (verdictQ):
                    try:
                        assert res == True
                    except:
                        verdictQ = False
                        error += "#    Error: <Queue>.isEmpty() returned either True or "
                        error += " non-bool on call when the queue was not empty.\n"
                        error += f"#        Expected: True - Got: {res} - Type: {type(res)}\n"

        if (verdictQ):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_isFullStack(self, module):
        """ Test-04: empty """
        output = "# Test-13: Valid Stack.isFull() Implementation - "
        ST = None
        verdictST = True
        error = ""

        # ======================= Test Stack ===================================
        try:
            ST = module.Stack(1)
        except Exception as e:
            error += "#    FATAL ERROR: Unable to make stack with call"
            error += " Stack(capacity).\n"
            error += "#        Exception: " + str(repr(e)) + "\n"
            verdictST = False

        if (verdictST):
            # step-01: test isEmpty
            try:
                res = ST.isFull()
            except Exception as e:
                verdictST = False
                error += "#    ERROR: <Stack>.isFull() crashed on valid call.\n"
                error += "#        Exception: " + str(repr(e)) + "\n"

            if (verdictST):
                try:
                    assert res == False
                except:
                    verdictST = False
                    error += "#    Error: <Stack>.isFull() returned either False or"
                    error += " non-bool on call when the stack was empty.\n"
                    error += f"#        Expected: False - Got: {res} - Type: {type(res)}\n"

            if (verdictST):
                N1 = module.Node(1)
                ST.head = N1
                ST.tail = N1
                ST.currentSize = 1
                try:
                    res = ST.isFull()
                except Exception as e:
                    verdictST = False
                    error += "#    ERROR: <Stack>.isFull() crashed on valid call when"
                    error += " stack was not empty.\n"
                    error += "#        Exception: " + str(repr(e)) + " \n"

                if (verdictST):
                    try:
                        assert res == True
                    except:
                        verdictST = False
                        error += "#    Error: <Stack>.isEmpty() returned either True or "
                        error += " non-bool on call when the stack was not empty.\n"
                        error += f"#        Expected: True - Got: {res} - Type: {type(res)}\n"

        if (verdictST):
            output += "PASS [7.5/7.5]\n"
            self.score += 7.5
            self.unitTestResults += output
        else:
            output += "FAIL [0/7.5]\n"
            self.unitTestResults += output
            self.unitTestResults += error



if __name__ == "__main__":
    test = Lab1Tester()
    test.testP1(module)
    print(test.unitTestResults)
