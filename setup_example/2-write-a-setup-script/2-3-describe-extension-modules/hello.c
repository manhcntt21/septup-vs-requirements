// Include thư viện Python C API để có thể tương tác với Python
#include <Python.h>

// Định nghĩa hàm C mà chúng ta muốn gọi từ Python
// self và args là các tham số bắt buộc theo chuẩn Python C API
static PyObject* hello_world(PyObject* self, PyObject* args) {
    // Py_BuildValue tạo một Python string từ C string
    // "s" là format specifier cho string
    return Py_BuildValue("s", "Hello from C!");
}

// Định nghĩa bảng các phương thức trong module
static PyMethodDef HelloMethods[] = {
    // Mỗi entry có format: {tên_python, hàm_c, kiểu_tham_số, docstring}
    {"say_hello",       // Tên sẽ dùng trong Python để gọi hàm
     hello_world,       // Con trỏ tới hàm C
     METH_NOARGS,      // Cho biết hàm không nhận tham số
     "Print hello from C"}, // Docstring mô tả hàm
    {NULL, NULL, 0, NULL}   // Sentinel đánh dấu kết thúc bảng
};

// Định nghĩa cấu trúc module
static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,  // Macro bắt buộc
    "hello",                // Tên module
    NULL,                   // Module docstring (NULL = không có)
    -1,                     // Size of per-interpreter state (-1 = global)
    HelloMethods            // Con trỏ tới bảng methods ở trên
};

// Hàm khởi tạo module - PHẢI có tên PyInit_<tên_module>
PyMODINIT_FUNC PyInit_hello(void) {
    // Tạo và trả về module
    return PyModule_Create(&hellomodule);
}