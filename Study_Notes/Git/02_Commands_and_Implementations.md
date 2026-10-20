# `Git` Useful Commands & Implementation

## Create `.gitignore` to tell `git` to ignore or exclude tracking on specific file or folder

Sample format of `.gitignore` file:

**NOTE**: `#` is comment for `.gitignore`

```shell
# Ignore specific file
<file_name>

# Ignore specific directory and all of its contents
<directory_name>/

# Ignore specific file type
*.<file_type>

# Ignore specific file or directory from multi-level subdirectories
<parent_folder>/**/<file_name>
<parent_folder>/**/directory_name>/ 

# -----------------------------------------------

# Exclude ignore (Using `!`):

# Case 1: For specific filename [for same path as .gitignore]
*.<file_type>
!<file_name>.<file_type> # Used to exclude ignore this <file_name> with the ignored <file_type> mentioned above

# Case 2: For specific filename or directory name in sub-directories

# To exclude ignore for single sub-level
<parent_folder>/*
!<parent_folder>/<file_name>
!<parent_folder>/<directory_name>/

# To exclude ignore in multiple sub-levels
<parent_folder>/*
# If only 1 sub-level
!<parent_folder>/<sub_level_1>
<parent_folder>/<sub_level_1>/*
!<parent_folder>/<sub_level_1>/<file_name>
!<parent_folder>/<sub_level_1>/<directory_name>/
# If more than 1 sub-level
!<parent_folder>/<sub_level_1>/<sub_level_2>/
<parent_folder>/<sub_level_1>/<sub_level_2>/*
!<parent_folder>/<sub_level_1>/<sub_level_2>/<file_name>
!<parent_folder>/<sub_level_1>/<sub_level_2>/<directory_name>/
```