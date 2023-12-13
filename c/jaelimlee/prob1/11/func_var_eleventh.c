#include "func_var_eleventh.h"

int check_not_data(int num)
{
    return ~num;
}

// +1 -1 = 0
// 0000 0001  ->  1
// 1000 0001  -> -1이라 가정
// 1000 0010  -> ?

//   0000 0001  ->  1
//   1111 1111  -> -1
// 1 0000 0000  ->  0

//   0000 0010  ->  2
//   1111 1110  -> -2
// 1 0000 0000  ->  0

// 0000 0010 0010  => 34
// 0000 0010 0001  => 33
// 1111 1101 1110 => NOT 33 =? = -X

// 위 숫자에 무언가 더했을 때 0이 되면 +X
// 1111 1101 1110  => NOT 33 = ? = -X = -34
// 0000 0010 0010  => 34 = +X