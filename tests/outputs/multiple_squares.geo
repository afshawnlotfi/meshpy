Macro smaller_square
    Point(1) = {-1.0, 1.0, 0.0, 1.0};
    Point(2) = {1.0, 1.0, 0.0, 1.0};
    Point(3) = {1.0, -1.0, 0.0, 1.0};
    Point(4) = {-1.0, -1.0, 0.0, 1.0};
    Line(1) = {1, 2};
    Line(2) = {2, 3};
    Line(3) = {3, 4};
    Line(4) = {4, 1};
Return
Call smaller_square;

Macro larger_square
    Point(5) = {-2.0, 2.0, 0.0, 1.0};
    Point(6) = {2.0, 2.0, 0.0, 1.0};
    Point(7) = {2.0, -2.0, 0.0, 1.0};
    Point(8) = {-2.0, -2.0, 0.0, 1.0};
    Line(5) = {5, 6};
    Line(6) = {6, 7};
    Line(7) = {7, 8};
    Line(8) = {8, 5};
Return
Call larger_square;
