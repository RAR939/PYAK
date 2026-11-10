Feature: Console figures for variant 20
  Scenario: Describe the blue rectangle
    Given the figures for variant 20
    Then figure 1 is described as "Прямоугольник: ширина 20, высота 20, цвет синий, площадь 400.00"

  Scenario: Describe the green circle
    Given the figures for variant 20
    Then figure 2 is described as "Круг: радиус 20, цвет зелёный, площадь 1256.64"

  Scenario: Describe the red square
    Given the figures for variant 20
    Then figure 3 is described as "Квадрат: сторона 20, цвет красный, площадь 400.00"
