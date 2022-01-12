#include <pybind11/pybind11.h>

#include "hello.h"

namespace py = pybind11;

PYBIND11_MODULE(hello_py, m)
{
    m.doc() = R"pbdoc(
        hello pybind11 example
    )pbdoc";

    py::class_<hello>(m, "hello")
        .def(py::init())
        .def("greet", &hello::greet);
}
