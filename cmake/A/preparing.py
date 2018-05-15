code = ["#pragma once",
        "#include <iostream>",
        "void f() {",
        '''std::cout << "generated .h" << std::endl;''',
        "}"]

with open("index.h", 'w') as f:
    for line in code:
        f.write(line + "\n");

