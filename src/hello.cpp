#include "hello.h"

#include <iostream>

hello::hello()
{
    std::cout << "hello" << std::endl;
}

hello::~hello()
{
    std::cout << "bye" << std::endl;
}

void hello::greet()
{
    std::cout << "hey" << std::endl;
}