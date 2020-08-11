#include "dir_scan.h"
#include "errno.h"

#include <dirent.h>
#include <linux/limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>



// check for "." and ".." to avoid infinite recursion.
static bool ignore_path(char *path, char*name)
{
    if ( (strcmp(name, ".") == 0) || strcmp(name, "..") == 0 || name == NULL)
    {
        return true;
    }
    return false;
}

// recursively scan through this directory tree
bool scan_directory_tree(char *root, scan_callback scan)
{
    assert(root != NULL);
    assert(scan != NULL);

    struct dirent *d_p = NULL;

    DIR *dir_p = opendir(root);
    if (dir_p == NULL) 
    {
        return false;
    }

    while ((d_p = readdir(dir_p)) != NULL)
    {
        if (ignore_path(root, d_p->d_name))
        continue;

        char newpath[PATH_MAX];
        sprintf(newpath, "%s/%s", root, d_p->d_name);

        // notify the caller
        scan(newpath, d_p->d_type == DT_DIR);

        if (d_p->d_type == DT_DIR)
        {
            // recurse
            scan_directory_tree(newpath, scan);
        }
    }
    closedir(dir_p);
    return true;
}