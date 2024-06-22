# CREATED BY AMANJIT to change location for R user library
# 
# R_LIBS_USER defaults to the form /home/username/R/x86_64-pc-linux-gnu-library/version
# e.g. /home/me/R/x86_64-pc-linux-gnu-library/4.4
# but I prefer a simpler path
# 
# this config runs when R starts, and makes R_LIBS_USER take the form:
# /home/username/R_user_libs/version
# e.g. /home/me/R_user_libs/4.4.0
# as is normal, this retains a different user lib for each version of R

# obtain user and version values that are set by R when it starts
user <- Sys.getenv("USER")
full_version <- paste(version$major, ".", version$minor, sep="")

# define a new path string
user_libs_path <- paste("/home/", user, "/R_user_libs/", full_version, sep="")

# set R_LIBS_USER to the new path and add it to .libPaths()
Sys.setenv(R_LIBS_USER = user_libs_path)
.libPaths(c(user_libs_path, .libPaths()))

