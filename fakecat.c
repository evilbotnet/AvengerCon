#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define CAT "/bin/cat"

const char *hints[] = {
    "meow",
    "I cAn HaZ Tr3aT?",
    "try -treat",
    "Cats need treats."
};

// add as many hints as you want without updating.
#define RANDOM_HINT hints[rand() % (sizeof(hints) / sizeof(*hints))]

int main(int argc, char *argv[])
{
    srand(time(NULL));

    // handle the case with no arguments, lets just pretend to be
    // cat
    if (argc == 1) {
        execve(CAT, argv, NULL);
    }

    // check whether the -treat option was passed
    for (int i = 1; i < argc; i++) {
        if (!strcmp("-treat", argv[i])) {
            // found treat option, pass all the arguments to the real cat
            // program, except for -treat

            // remove the "-treat" option from the argument list
            for (int j = i; j < argc; j++) {
                argv[j] = argv[j + 1];
            }

            // execute the real cat
            execve(CAT, argv, NULL);
        } else {
            puts(RANDOM_HINT);
        }
    }

    exit(EXIT_FAILURE);
}
