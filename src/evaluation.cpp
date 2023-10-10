#include <assert.h>
#include "evaluation.h"
#include <vector>
#include <iostream>
#include <stdio.h>

evaluation::evaluation(const std::vector<expression> &exprs)
//constructor, takes in a vector of expressions. std::vector is a template class
//that implements a dynamic array. The vector is passed by reference
//so that the vector is not copied
//the constructor initializes the result_ variable to 0
//and asserts that the size of the vector is greater than 0
//if it is not, the program will terminate
    : result_(0)
{
    //assert(exprs.size() > 0);
    //dont add code yet

    //asserts that the size of the vector is greater than 0
    //if it is not, the program will terminate


}

void evaluation::add_kwargs_double(const char *key, double value)
//takes in a pointer to a character array and a double value
{
    
}

void evaluation::add_kwargs_ndarray(const char *key, int dim, size_t shape[], double data[])
//takes in a pointer to a character array, an integer, a pointer to a size_t array, and a pointer to a double array
    //the function is called in the main() function in easynn_test.cpp
{
    
}

int evaluation::execute()
//returns 0 for success
//the function is called in the main() function in easynn_test.cpp
//the function is called in the execute() function in libeasynn.cpp
{
    return -1;
}

double &evaluation::get_result()
//returns the variable computed by the last expression
//the function is called in the main() function in easynn_test.cpp
{
    return result_;
    //returns the result_ variable
}
