//while b > 40000000 instead of < in line 9 - CC

#include <iostream>

int main()
{
    int a = 0, b = 1;
    int sum_even = 0;
    // FIXED: Turned > to < in while loop WB
    while (b < 4000000) {
        if (b % 2 == 0) {
            sum_even += b;
        }
        int temp = b;
        b = a + b;
        a = temp;
    }
    std::cout << sum_even << std::endl;

    return 0;
}

// answer should be 4613732
// Did you check your work Harry?
