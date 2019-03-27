// #include "Python.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "Python.h"

#ifdef Py_ENABLE_SHARED
#   undef Py_ENABLE_SHARED
#endif
#define Py_ENABLE_SHARED 1

#ifdef HAVE_DECLSPEC_DLL
#   undef HAVE_DECLSPEC_DLL
#endif
#define HAVE_DECLSPEC_DLL 1

#ifdef Py_BUILD_CORE
#   undef Py_BUILD_CORE
#endif
#define Py_BUILD_CORE 1

#ifdef __cplusplus
#   undef __cplusplus
#endif
#define __cplusplus 1

// #include "moduleobject.h"
// #include "unicodeobject.c"
#include "m.h"

PyObject *__PyUnicode_DecodeUTF8Stateful(const char *s,
                             Py_ssize_t size,
                             const char *errors,
                             Py_ssize_t *consumed)
{
    _PyUnicodeWriter writer;
    const char *starts = s;
    const char *end = s + size;
    Py_ssize_t startinpos;
    Py_ssize_t endinpos;
    const char *errmsg = "";
    PyObject *error_handler_obj = NULL;
    PyObject *exc = NULL;
    _Py_error_handler error_handler = _Py_ERROR_UNKNOWN;
    if (size == 0) {
        if (consumed)
            *consumed = 0;
        _Py_RETURN_UNICODE_EMPTY();
    }
    /* ASCII is equivalent to the first 128 ordinals in Unicode. */
    if (size == 1 && (unsigned char)s[0] < 128) {
        if (consumed)
            *consumed = 1;
        return get_latin1_char((unsigned char)s[0]);
    }
    _PyUnicodeWriter_Init(&writer);
    writer.min_length = size;
    if (_PyUnicodeWriter_Prepare(&writer, writer.min_length, 127) == -1)
        goto onError;
    writer.pos = ascii_decode(s, end, writer.data);
    s += writer.pos;
    while (s < end) {
        Py_UCS4 ch;
        int kind = writer.kind;
        if (kind == PyUnicode_1BYTE_KIND) {
            if (PyUnicode_IS_ASCII(writer.buffer))
                ch = asciilib_utf8_decode(&s, end, writer.data, &writer.pos);
            else
                ch = ucs1lib_utf8_decode(&s, end, writer.data, &writer.pos);
        } else if (kind == PyUnicode_2BYTE_KIND) {
            ch = ucs2lib_utf8_decode(&s, end, writer.data, &writer.pos);
        } else {
            assert(kind == PyUnicode_4BYTE_KIND);
            ch = ucs4lib_utf8_decode(&s, end, writer.data, &writer.pos);
        }
        switch (ch) {
        case 0:
            if (s == end || consumed)
                goto End;
            errmsg = "unexpected end of data";
            startinpos = s - starts;
            endinpos = end - starts;
            break;
        case 1:
            errmsg = "invalid start byte";
            startinpos = s - starts;
            endinpos = startinpos + 1;
            break;
        case 2:
        case 3:
        case 4:
            errmsg = "invalid continuation byte";
            startinpos = s - starts;
            endinpos = startinpos + ch - 1;
            break;
        default:
            if (_PyUnicodeWriter_WriteCharInline(&writer, ch) < 0)
                goto onError;
            continue;
        }

        if (error_handler == _Py_ERROR_UNKNOWN)
            error_handler = get_error_handler(errors);

        switch (error_handler) {
        case _Py_ERROR_IGNORE:
            s += (endinpos - startinpos);
            break;

        case _Py_ERROR_REPLACE:
            if (_PyUnicodeWriter_WriteCharInline(&writer, 0xfffd) < 0)
                goto onError;
            s += (endinpos - startinpos);
            break;

        case _Py_ERROR_SURROGATEESCAPE:
        {
            Py_ssize_t i;

            if (_PyUnicodeWriter_PrepareKind(&writer, PyUnicode_2BYTE_KIND) < 0)
                goto onError;
            for (i=startinpos; i<endinpos; i++) {
                ch = (Py_UCS4)(unsigned char)(starts[i]);
                PyUnicode_WRITE(writer.kind, writer.data, writer.pos,
                                ch + 0xdc00);
                writer.pos++;
            }
            s += (endinpos - startinpos);
            break;
        }

        default:
            if (unicode_decode_call_errorhandler_writer(
                    errors, &error_handler_obj,
                    "utf-8", errmsg,
                    &starts, &end, &startinpos, &endinpos, &exc, &s,
                    &writer))
                goto onError;
        }
    }

End:
    if (consumed)
        *consumed = s - starts;

    Py_XDECREF(error_handler_obj);
    Py_XDECREF(exc);
    return _PyUnicodeWriter_Finish(&writer);

onError:
    Py_XDECREF(error_handler_obj);
    Py_XDECREF(exc);
    _PyUnicodeWriter_Dealloc(&writer);
    return NULL;
}

PyObject *_PyUnicode_FromString(const char *u)
{
    size_t size = strlen(u);
    if (size > PY_SSIZE_T_MAX) {
        // PyErr_SetString(PyExc_OverflowError, "input too long");
        return NULL;
    }
    return _PyUnicode_DecodeUTF8Stateful(u, (Py_ssize_t)size, NULL, NULL);
}

PyObject *_PyDict_New(void)
{
    PyDictKeysObject *keys = new_keys_object(PyDict_MINSIZE);
    if (keys == NULL)
        return NULL;
    return new_dict(keys, NULL);
}

PyObject *_PyModule_NewObject(PyObject *name)
{
    PyModuleObject *m;
    m = PyObject_GC_New(PyModuleObject, &PyModule_Type);
    if (m == NULL)
        return NULL;
    m->md_def = NULL;
    m->md_state = NULL;
    m->md_weaklist = NULL;
    m->md_name = NULL;
    m->md_dict = _PyDict_New();
    if (module_init_dict(m, m->md_dict, name, NULL) != 0)
        goto fail;
    PyObject_GC_Track(m);
    return (PyObject *)m;

 fail:
    Py_DECREF(m);
    return NULL;
}

PyObject *_PyModule_New(const char *name){
    PyObject *nameobj, *module;
    nameobj = _PyUnicode_FromString(name);
    if (nameobj == NULL)
        return NULL;
    module = _PyModule_NewObject(nameobj);
    Py_DECREF(nameobj);
    return module;
}

int main(){
    PyObject *pyObj = _PyModule_New("virink");
    // pyObj->ob_type->tp_print(pyObj,stdout,1);
    return 0;
}