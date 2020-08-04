#ifndef __DIR_SCAN_H__
#define __DIR_SCAN_H__

#include <stdbool.h>

typedef void (*scan_callback)(char *path, bool is_directory);

bool scan_directory_tree(char *root /*root of tree to scan*/, scan_callback scan);


#endif // __DIR_SCAN_H__