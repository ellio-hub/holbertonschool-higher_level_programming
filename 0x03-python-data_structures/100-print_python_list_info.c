#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object
 *
 */

void print_python_list_info(PyObject *p)
{
size_t i, j = 0;
PyObject *obj;
i = PyList_Size(p);
printf("[*] Size of the Python List = %zu\n", i);
printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
while (j < i)
{
obj = PyList_GET_ITEM(p, j);
printf("Element %zu: %s\n", j, Py_TYPE(obj)->tp_name);
j++;
}
}
