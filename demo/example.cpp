#include <iostream>
#include <hello.h>

int main()
{
    {
        std::cout << "obj coming to life" << std::endl;
        hello obj;
        obj.greet();
        std::cout << "obj dying..." << std::endl;
    }

    return 0;
}