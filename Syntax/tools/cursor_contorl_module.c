#define PY_SSIZE_T_CLEAN
#include <python3.8/Python.h>

#include "cursor_contorl.h"

static PyObject *cursor_contorl_clear(PyObject *self)
{
	clear();
	return Py_None;
}

static PyObject *cursor_contorl_move_up(PyObject *self, PyObject *args)
{
	int x = 0;
	if(!PyArg_ParseTuple(args, "i", &x))
		return NULL;
	move_up(x);
	return Py_None;
}

static PyObject *cursor_contorl_move_down(PyObject *self, PyObject *args)
{
	int x = 0;
	if(!PyArg_ParseTuple(args, "i", &x))
		return NULL;
	move_down(x);
	return Py_None;
}

static PyObject *cursor_contorl_move_left(PyObject *self, PyObject *args)
{
	int y = 0;
	if(!PyArg_ParseTuple(args, "i", &y))
		return NULL;
	move_left(y);
	return Py_None;
}

static PyObject *cursor_contorl_move_right(PyObject *self, PyObject *args)
{
	int y = 0;
	if(!PyArg_ParseTuple(args, "i", &y))
		return NULL;
	move_right(y);
	return Py_None;
}

static PyObject *cursor_contorl_move_to(PyObject *self, PyObject *args)
{
	int x = 0, y = 0;
	if(!PyArg_ParseTuple(args, "ii", &x, &y))
		return NULL;
	move_to(x, y);
	return Py_None;
}

static PyObject *cursor_contorl_reset_cursor(PyObject *self)
{
	reset_cursor();
	return Py_None;
}

static PyObject *cursor_contorl_hide_cursor(PyObject *self)
{
	hide_cursor();
	return Py_None;
}

static PyObject *cursor_contorl_show_cursor(PyObject *self)
{
	show_cursor();
	return Py_None;
}

static PyObject *cursor_contorl_hight_light(PyObject *self)
{
	hight_light();
	return Py_None;
}

static PyObject *cursor_contorl_un_hight_light(PyObject *self)
{
	un_hight_light();
	return Py_None;
}

static PyMethodDef cursorContorlMethods[] = 
{
	{"clear", cursor_contorl_clear, METH_VARARGS}, 
	{"move_up", cursor_contorl_move_up, METH_VARARGS}, 
	{"move_down", cursor_contorl_move_down, METH_VARARGS}, 
	{"move_left", cursor_contorl_move_left, METH_VARARGS}, 
	{"move_right", cursor_contorl_move_right, METH_VARARGS}, 
	{"move_to", cursor_contorl_move_to, METH_VARARGS}, 
	{"reset_cursor", cursor_contorl_reset_cursor, METH_VARARGS}, 
	{"hide_cursor", cursor_contorl_hide_cursor, METH_VARARGS}, 
	{"show_cursor", cursor_contorl_show_cursor, METH_VARARGS}, 
	{"hight_light", cursor_contorl_hight_light, METH_VARARGS}, 
	{"un_hight_light", cursor_contorl_un_hight_light, METH_VARARGS}, 
	{NULL, NULL, 0}
};

static struct PyModuleDef cursorContorlModule = 
{
	PyModuleDef_HEAD_INIT, 
	"cursor_contorl", 
	NULL, 
	-1, 
	cursorContorlMethods
};

PyMODINIT_FUNC PyInit_cursor_contorl()
{
	return PyModule_Create(&cursorContorlModule);
}
