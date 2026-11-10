import pytest

from main import build_figures


def test_rectangle_area():
    rectangle, _, _ = build_figures(20)
    assert rectangle.area() == 400


def test_circle_area():
    _, circle, _ = build_figures(20)
    assert circle.area() == pytest.approx(1256.6370614359173)


def test_square_area():
    _, _, square = build_figures(20)
    assert square.area() == 400
