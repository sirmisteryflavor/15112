#################################################
# Hw1
#################################################

import cs112_f17_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Hw1 problems
#################################################

def hotdogPurchase(numHotdogs):
    """

    Goal:
    figure out purchase

    Input:
    numHotdogs

    Output:
    number of frank packages, number of bun packages

    Method:
    Use modulo to check for remainders. If so, do integer division of numHotdogs
    and increase the package by 1. Division will always produce 1 package less
    since integer division rounds down

    """

    if (numHotdogs % 10) == 0:
        frank_pkg = numHotdogs/10

    else:
        frank_pkg = (numHotdogs//10) + 1

    if (numHotdogs % 8) == 0:
        bun_pkg = numHotdogs/8

    else:
        bun_pkg = (numHotdogs//8) + 1

    return int(frank_pkg), int(bun_pkg)


def hotdogExcess(numHotdogs):
    """

    Goal:
    Find excess dogs and buns

    Input:
    numHotdogs

    Output:
    excess_franks, excess_buns

    Method:
    1. Find out how much packages of each need to be purchased using
        hotdogPurcahse
    2. Figure out how much is in those packages
    3. Subtract how much hotdogs we plan on making
    4. Return the remainder

    """

    franks_pkg, bun_pkg = hotdogPurchase(numHotdogs)

    excess_franks = ((franks_pkg * 10) - numHotdogs) % 10

    excess_buns = ((bun_pkg * 8) - numHotdogs) % 8

    return excess_franks, excess_buns

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    """

    Goal:
    Determine if the triangle is a right triangle (or can have the pythagorean
    theorem applicable)

    Input:
    Three (x, y) coordinates

    Output:
    True or False

    Method:
    1. Find lengths a,b,c
    2. Check if condition a**2 + b**2 = c**2 applies
    3. Check if condition a**2 + c**2 = b**2 applies
    4. Check if condition c**2 + b**2 = a**2 applies

    Pitfalls:
    If the points provided form a line, not a triangle, it needs to be
    recognized as such and return False

    """
    a = distance(x1, y1, x2, y2)
    b = distance(x1, y1, x3, y3)
    c = distance(x2, y2, x3, y3)

    if a == 0 or b == 0 or c == 0:
        print("Distance cannot be 0!")
        return(False)

    print("a: ", a)
    print("b: ", b)
    print("c: ", c)

    print("")
    print("")
    print("")

    print("Test 1")
    print("a**2 + b**2: ", (a**2 + b**2))
    print("c**2:        ", c**2)

    if almostEqual((a**2 + b**2), c**2):
        return(True)

    print("")
    print("")
    print("")

    print("Test 2")
    print("a**2 + c**2: ", (a**2 + c**2))
    print("b**2:        ", b**2)

    if almostEqual((a**2 + c**2), b**2):
        return(True)

    print("")
    print("")
    print("")

    print("Test 3")
    print("c**2 + b**2: ", (c**2 + b**2))
    print("a**2:        ", a**2)

    if almostEqual((b**2 + c**2), a**2):
        return(True)

    print("")
    print("")
    print("")
    print("All conditions failed")
    return(False)

def distance(x1, y1, x2, y2):
    """

    Goal:
    Find distance between two points

    Input:
    Two (x, y) coordinates

    Output:
    Euclidean distance

    Method:
    Distance between two points (x1, y1) and (x2, y2) can be found using the
    pythagorean theorem as follows: dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

    """

    dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return dist

def lineIntersection(m1, b1, m2, b2):
    """

    Goal:
    Find the point at which two lines intersect

    Input:
    Two slopes, two intercepts

    Output:
    (x, y) coordinate

    Method:
    Use algebra to set two linear equations equal to each other as such -

        y1 = m1 * x + b1
        y2 = m2 * x + b2

        let's just call x as a for now

        m1 * a + b1 = m2 * a + b2
        (m1 - m2) * x = (b2 - b1)
        a = (b2 - b1) / (m1 - m2)

        plug in a to make sure to check y1 = y2 when x = a

        return (y1, a) or (y2, a)

        if point of intersection is same for all three lines, return fail
    """

    if almostEqual(m1, m2) and almostEqual(b1, b2):
        print("Infinite solution: identical lines")
        return(None)

    elif  almostEqual(m1, m2):
        print("Parallel lines")
        return(None)

    a = (b2 - b1) / (m1 - m2)

    y1 = m1 * a + b1
    y2 = m2 * a + b2

    if almostEqual(y1, y2):
        print("Intersection found!")
    else:
        return(None)

    print("Point of intersection is ", "(", a,", ", y1, ")")
    return a, y1

def triangleArea(s1, s2, s3):
    """

    Goal:
    Calculate area of triange

    Input:
    Three lengths for each side of a triangle

    Output:
    Triangle area

    Method:
    You can use multiple options here (Pythagorean theorem, Heron's formula,
    etc.) I'm going to choose the laziest one and use Heron's formula

    1. Calculate distance between three coordinates
    2. Use Heron's formula A = sqrt(s(s-a)(s-b)(s-c)) where s = (a + b + c)/2

    """

    p = (s1 + s2 + s3)/2
    Area = (p*(p - s1)*(p - s2)*(p - s3))**(1/2)

    return Area

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    """

    Goal:
    Calculate area of triange formed by three linear equations

    Input:
    Three sets of slope and intercepts

    Output:
    Area

    Method:

    1. Get a set of three coordinates using 'lineIntersection'
    2. Calculate lengths of all sides of triangle using 'distance'
    3. Calculate triangle area using 'triangleArea'

    """

    x1, y1 = lineIntersection(m1, b1, m2, b2)
    x2, y2 = lineIntersection(m2, b2, m3, b3)
    x3, y3 = lineIntersection(m1, b1, m3, b3)

    side_a = distance(x1, y1, x2, y2)
    side_b = distance(x2, y2, x3, y3)
    side_c = distance(x1, y1, x3, y3)

    final_area = triangleArea(side_a, side_b, side_c)
    print(final_area)
    return final_area

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Hw1 Test Functions
#################################################

def testHotdogPurchase():
    print('Testing hotdogPurchase()... ', end='')
    assert(hotdogPurchase(0) == (0,0))
    assert(hotdogPurchase(13) == (2,2))
    assert(hotdogPurchase(26) == (3,4))
    assert(hotdogPurchase(39) == (4,5))
    assert(hotdogPurchase(50) == (5,7))
    assert(hotdogPurchase(61) == (7,8))
    assert(hotdogPurchase(80) == (8,10))
    assert(hotdogPurchase(88) == (9,11))
    print('Passed.')

def testHotdogExcess():
    print('Testing hotdogExcess()... ', end='')
    assert(hotdogExcess(0) == (0,0))
    assert(hotdogExcess(13) == (7,3))
    assert(hotdogExcess(26) == (4,6))
    assert(hotdogExcess(39) == (1,1))
    assert(hotdogExcess(50) == (0,6))
    assert(hotdogExcess(61) == (9,3))
    assert(hotdogExcess(80) == (0,0))
    assert(hotdogExcess(88) == (2,0))
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    # assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    # assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def testAll():
    testHotdogPurchase()
    testHotdogExcess()
    testIsRightTriangle()
    testDistance()
    testLineIntersection()
    testTriangleArea()
    testThreeLinesArea()
    testBonusFindIntRootsOfCubic()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_f17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
