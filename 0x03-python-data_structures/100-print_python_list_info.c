#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size_list = PyList_Size(p);
	int z;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size_list);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (z = 0; z < size_list; z++)
		printf("Element %i: %s\n", z, Py_TYPE(obj->ob_item[z])->tp_name);
}
