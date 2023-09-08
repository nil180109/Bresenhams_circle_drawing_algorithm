# Bresenhams_circle_drawing_algorithm

Bresenham's Circle Algorithm:
Step1: Start Algorithm

Step2: Declare p, q, x, y, r, d variables
        p, q are coordinates of the center of the circle
        r is the radius of the circle

Step3: Enter the value of r
AD

Step4: Calculate d = 3 - 2r

Step5: Initialize       x=0
          &nbsy= r

Step6: Check if the whole circle is scan converted
            If x > = y
            Stop

Step7: Plot eight points by using concepts of eight-way symmetry. The center is at (p, q). Current active pixel is (x, y).
                putpixel (x+p, y+q)
                putpixel (y+p, x+q)
                putpixel (-y+p, x+q)
                putpixel (-x+p, y+q)
                putpixel (-x+p, -y+q)
                putpixel (-y+p, -x+q)
                putpixel (y+p, -x+q)
                putpixel (x+p, -y-q)

Step8: Find location of next pixels to be scanned
            If d < 0
            then d = d + 4x + 6
            increment x = x + 1
            If d ≥ 0
            then d = d + 4 (x - y) + 10
            increment x = x + 1
            decrement y = y - 1
AD

Step9: Go to step 6

Step10: Stop Algorithm

Example: Plot 6 points of circle using Bresenham Algorithm. When radius of circle is 10 units. The circle has centre (50, 50).

Solution: Let r = 10 (Given)

Step1: Take initial point (0, 10)
                d = 3 - 2r
                d = 3 - 2 * 10 = -17
                d < 0 ∴ d = d + 4x + 6
                      = -17 + 4 (0) + 6
                      = -11

Step2: Plot (1, 10)
          d = d + 4x + 6 (∵ d < 0)
                = -11 + 4 (1) + 6
                = -1

Step3: Plot (2, 10)
           d = d + 4x + 6 (∵ d < 0)
                = -1 + 4 x 2 + 6
                = 13

Step4: Plot (3, 9) d is > 0 so x = x + 1, y = y - 1
                          d = d + 4 (x-y) + 10 (∵ d > 0)
                = 13 + 4 (3-9) + 10
                = 13 + 4 (-6) + 10
                = 23-24=-1

Step5: Plot (4, 9)
            d = -1 + 4x + 6
                = -1 + 4 (4) + 6
                = 21

Step6: Plot (5, 8)
            d = d + 4 (x-y) + 10 (∵ d > 0)
                = 21 + 4 (5-8) + 10
                = 21-12 + 10 = 19

So P1 (0,0)⟹(50,50)
            P2 (1,10)⟹(51,60)
            P3 (2,10)⟹(52,60)
            P4 (3,9)⟹(53,59)
            P5 (4,9)⟹(54,59)
            P6 (5,8)⟹(55,58)
