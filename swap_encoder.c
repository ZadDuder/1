#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <limits.h>
#define ERR_IO 1
// Функция принимает на вход 32-битное беззнаковое целое число и возвращает 32-битное беззнаковое целое число с изменёнными местами чётных и нечётных битов.
uint32_t swap_even_odd_bits(uint32_t x)
{
    uint32_t even_bits = x & 0xAAAAAAAA; 
    uint32_t odd_bits = x & 0x55555555; 
    even_bits >>= 1; 
    odd_bits <<= 1; 
    return (even_bits | odd_bits); 
}
/// выводит число в двоичном виде
void print_binary(uint32_t n)
{
    for (int i = (sizeof(n) * CHAR_BIT) - 1; i >= 0; i--) 
    {
        putchar((n & (1u << i)) ? '1' : '0');
    }
    putchar('\n');
}
int main(void) 
{
    uint32_t x;
    printf("Enter a number: ");
    if (scanf("%" SCNu32, &x) != 1) 
    {
        printf("Error: Invalid input.\n");
        return ERR_IO;
    }
    uint32_t result = swap_even_odd_bits(x);
    printf("Result: ");
    print_binary(result);
    return 0;
}
