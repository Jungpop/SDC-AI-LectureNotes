/*
main() 함수 안에서
인자값 2개를 가지는 doit(), letsgo() 함수를 호출
doit() 함수는 인자값 2개를 % 연산한 결과를 반환
letsgo() 함수는 인자값 2개를 + 연산한 결과를 반환
doit()의 결과값과 letsgo()의 결과값을 곱한 결과를 출력하시오.
*/

#include "func_var_thirteenth.h"

int doit(int num1, int num2)
{
    return num1 % num2;
}

int letsgo(int num1, int num2)
{
    return num1 + num2; 
}

int process_data(int doit_result, int letsgo_result)
{
    return doit_result * letsgo_result;
}