import pytest

from conway import Grid, next_generation


@pytest.mark.parametrize("input,expected", [
    ([[0, 1, 0],
     [0, 1, 0],
     [0, 0, 0]], [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]),
    ([[0, 1, 0, 1],
      [0, 1, 0, 1],
      [0, 0, 0, 0]], [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]),
    ([[0, 1, 0],
      [0, 1, 0],
      [0, 0, 0],
      [0, 1, 0]], [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]),
])
def test_less_than_two_neighbours_alive_should_die(input: Grid, expected: Grid) -> None:
    actual = next_generation(input)
    assert expected == actual


def test_more_than_three_neighbours_should_die() -> None:
    grid: Grid = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
    expected: Grid = [[1, 0, 1],
                      [0, 0, 0],
                      [1, 0, 1]]

    actual = next_generation(grid)

    assert expected == actual


def test_two_neighbours_should_live() -> None:
    grid: Grid = [[0, 0, 1],
                  [0, 1, 0],
                  [1, 0, 0]]
    expected: Grid = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

    actual = next_generation(grid)

    assert expected == actual


def test_three_neighbours_should_live() -> None:
    grid: Grid = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 0]]
    expected: Grid = [[1, 1, 0],
                      [1, 1, 0],
                      [0, 0, 0]]

    actual = next_generation(grid)

    assert expected == actual


def test_dead_with_three_neighbours_should_live() -> None:
    grid: Grid = [[1, 1, 0],
                  [1, 0, 0],
                  [0, 0, 0]]
    expected: Grid = [[1, 1, 0],
                      [1, 1, 0],
                      [0, 0, 0]]

    actual = next_generation(grid)

    assert expected == actual
