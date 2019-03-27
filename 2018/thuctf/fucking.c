// fucking.c
#include "Python.h"
#include "longintrepr.h"
#include "code.h"
#include "marshal.h"
#include "../Modules/hashtable.h"

static PyObject *FuckingError;

static PyObject *fucking_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(FuckingError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}

static PyObject *fucking_dumps(PyObject *self, PyObject *args)
{
    PyObject *x;
    int version = Py_MARSHAL_VERSION;
    if (!PyArg_ParseTuple(args, "O|i:dumps", &x, &version))
        return NULL;
    return PyMarshal_WriteObjectToString(x, version);
}

static PyObject *fucking_loads(PyObject *self, PyObject *args)
{
    RFILE rf;
    Py_buffer p;
    char *s;
    Py_ssize_t n;
    PyObject* result;
    if (!PyArg_ParseTuple(args, "y*:loads", &p))
        return NULL;
    s = p.buf;
    n = p.len;
    rf.fp = NULL;
    rf.readable = NULL;
    rf.current_filename = NULL;
    rf.ptr = s;
    rf.end = s + n;
    rf.depth = 0;
    if ((rf.refs = PyList_New(0)) == NULL)
        return NULL;
    result = read_object(&rf);
    PyBuffer_Release(&p);
    Py_DECREF(rf.refs);
    return result;
}

static PyMethodDef FuckingMethods[] = {
    {"system",  fucking_system, METH_VARARGS,   "Execute a shell command."},
    {"dumps",   fucking_dumps,  METH_VARARGS,   "Dumps..."},
    {"loads",   fucking_loads,  METH_VARARGS,   "Loads..."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initfucking(void)
{
    PyObject *m;
    m = Py_InitModule("fucking", FuckingMethods);
    if (m == NULL)
        return;
    FuckingError = PyErr_NewException("fucking.error", NULL, NULL);
    Py_INCREF(FuckingError);
    PyModule_AddObject(m, "error", FuckingError);
}