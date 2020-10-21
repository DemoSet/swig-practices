//
// Created by 水清源 on 2020/10/21.
//

#ifndef SWIG_PRACTICES_DEMO_H
#define SWIG_PRACTICES_DEMO_H

#include <utility>

std::pair<int, int> func();

class Pair {
public:
    int first, second;
    Pair(int x, int y) {
        first = x;
        second = y;
    }
};

#endif //SWIG_PRACTICES_DEMO_H
