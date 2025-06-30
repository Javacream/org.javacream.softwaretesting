| **Test Case**                                   | **Parameter** | **Ergebnis**                 |
|--------------------------------------------------|---------------|-------------------------------|
| negative_a_is_invalid                       | (-1,3,4)      | Kein Dreieck                  |
| negative_b_is_invalid                       | (3,-1,4)      | Kein Dreieck                  |
| negative_c_is_invalid                       | (3,4,-1)      | Kein Dreieck                  |
| negative_a_and_b_is_invalid                       | (-1,-1,1)     | Kein Dreieck                  |
| negative_a_and_c_is_invalid                       | (-1,1,-1)     | Kein Dreieck                  |
| negative_b_and_c_is_invalid                       | (1,-1,-1)     | Kein Dreieck                  |
| negative_a_b_and_c_is_invalid                       | (-1,-1,-1)    | Kein Dreieck                  |
| a_is_0_is_invalid_length                              | (0,3,4)       | Kein Dreieck                  |
| b_is_0_is_invalid_length                              | (3,0,4)       | Kein Dreieck                  |
| c_is_0_is_invalid_length                              | (3,4,0)       | Kein Dreieck                  |
| a_nad_b_is_0_is_invalid_length                              | (0,0,1)       | Kein Dreieck                  |
| a_and_c_is_0_is_invalid_length                              | (0,1,0)       | Kein Dreieck                  |
| b_and_c_is_0_is_invalid_length                              | (1,0,0)       | Kein Dreieck                  |
| a_b_c_is_0_is_invalid_length                              | (0,0,0)       | Kein Dreieck                  |
| 2_5_4_is_triangle                                 | (2,5,4)       | Dreieck                       |
| 3_3_3_is_equiliteral                              | (3,3,3)       | Gleichseitiges Dreieck        |
| 3_3_4_is_isoscele                                 | (3,3,4)       | Gleichschenkliges Dreieck     |
| sum_of_two_sides_is_greater_than_third_side      | (2,5,4)       | Dreieck                       |
| sum_of_two_sides_is_less_or_equal_third_side     | (1,2,3)       | Kein Dreieck                  |