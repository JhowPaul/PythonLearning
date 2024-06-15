#Write a Python program to find files and skip directories of a given directory.

import os
print([i for i in os.listdir("D:\Backup HD Antigo\PYTHON GARAI")if os.path.isfile
(os.path.join("D:\Backup HD Antigo\PYTHON GARAI",i))])

