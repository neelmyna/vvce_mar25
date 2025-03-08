#include <stdio.h>

int main() {
    int num; // assume junk
    int *p = NULL; //  assume junk address. assume p holds address of printer
    printf("%u", p); // we got address of printer
    *p = somevalue;
}

WILD Pointer