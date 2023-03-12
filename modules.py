"""
If you quit from the Python interpreter and
enter it again, the defintions you have made
(functions and variables) are lost. Therefore,
if you want to write a soemwhat longer program,
you aree better off using a text editor
to prepare the input for the interpreter and
running it with that file as input instead.
This is known as creating a script. As your
program gets longer, you may want to split it
into several files for eaisier maintenance.
You may also want to use a handy function
that you've written in several programs
without coying its definition into
each program.

To support this, Python has a way to put definitions
in a file and use them in a script or in an interactive
instance of the interpreter. Such a file is called
a module (the collection of variables that you have
access to in a script executed at the top level
and in calculator mode.)

A module is a file containing Python definitions
and statements. The file name is the module name with the suffix
.py appended. Within a module, the module's name (as a string) is
available as the value of the global variable __name__.
For instance, use your favourite text editor to create a file called module.py
in the current directory with the following contents:

"""
