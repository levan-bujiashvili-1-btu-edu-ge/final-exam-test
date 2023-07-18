# 20672168958215818771
from lib import QuadraticEquationSolver
from pytest import approx, raises


def test_0_0_0():
    with raises(ZeroDivisionError) as e:
        QuadraticEquationSolver(0, 0, 0).solve()


def test_p1_0_0():
    assert QuadraticEquationSolver(1, 0, 0).solve() == [0]


def test_p1_0_n5():
    assert QuadraticEquationSolver(1, 0, -5).solve() == [
        approx(5**0.5),
        approx(-(5**0.5)),
    ]


def test_p1_p1_0():
    assert QuadraticEquationSolver(1, 1, 0).solve() == [0, -1]


def test_p1_n1_0():
    assert QuadraticEquationSolver(1, -1, 0).solve() == [1, 0]


def test_p1_p1_p1():
    assert QuadraticEquationSolver(1, 1, 1).solve() == []


def test_p1_p2_p1():
    assert QuadraticEquationSolver(1, 2, 1).solve() == [-1]


def test_p1_p1_n1():
    assert QuadraticEquationSolver(1, 1, -1).solve() == [
        approx(-0.5 + 5**0.5 * 0.5),
        approx(-0.5 - 5**0.5 * 0.5),
    ]


def test_p1_n1_p1():
    assert QuadraticEquationSolver(1, -1, 1).solve() == []


def test_p1_n1_n1():
    assert QuadraticEquationSolver(1, -1, -1).solve() == [
        approx(+0.5 + 5**0.5 * 0.5),
        approx(+0.5 - 5**0.5 * 0.5),
    ]


def test_n1_0_p1():
    assert QuadraticEquationSolver(-1, 0, 1).solve() == [-1, 1]
