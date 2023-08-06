// Copyright (c) 2019 CRS4
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

#pragma once

#include <pybind11/pybind11.h>

template <typename type_, typename... options>
void tensor_addons(pybind11::class_<type_, options...> &cl) {
    cl.def(pybind11::init<const vector<int>&, int>(),
           pybind11::arg("shape"), pybind11::arg("dev") = DEV_CPU,
           pybind11::keep_alive<1, 2>());
    cl.def("getShape", &Tensor::getShape);
    // cl.def_static("delta_reduce", &Tensor::delta_reduce, pybind11::arg("A"),
    // 		  pybind11::arg("B"), pybind11::arg("axis"),
    // 		  pybind11::arg("mode"), pybind11::arg("keepdims"),
    // 		  pybind11::arg("C"), pybind11::arg("incB"));
    // cl.def_static("delta_reduced_op", &Tensor::delta_reduced_op,
    // 		  pybind11::arg("A"), pybind11::arg("B"),
    // 		  pybind11::arg("axis"), pybind11::arg("op"),
    // 		  pybind11::arg("C"), pybind11::arg("incC"));
    cl.def_static("full", &Tensor::full, pybind11::arg("shape"),
		  pybind11::arg("value"), pybind11::arg("dev") = DEV_CPU);
    cl.def_static("ones", &Tensor::ones, pybind11::arg("shape"),
		  pybind11::arg("dev") = DEV_CPU);
    cl.def_static("randn", &Tensor::randn, pybind11::arg("shape"),
		  pybind11::arg("dev") = DEV_CPU);
    // cl.def_static("reduce", &Tensor::reduce, pybind11::arg("A"),
    // 		  pybind11::arg("B"), pybind11::arg("axis"),
    // 		  pybind11::arg("mode"), pybind11::arg("keepdims"),
    // 		  pybind11::arg("C"), pybind11::arg("incB"));
    // cl.def_static("reduced_op", &Tensor::reduced_op, pybind11::arg("A"),
    // 		  pybind11::arg("B"), pybind11::arg("axis"),
    // 		  pybind11::arg("op"), pybind11::arg("C"),
    // 		  pybind11::arg("incC"));
    cl.def_static("select", &Tensor::select, pybind11::arg("A"),
		  pybind11::arg("B"), pybind11::arg("sind"),
		  pybind11::arg("ini"), pybind11::arg("end"));
    cl.def_static("transpose", &Tensor::transpose, pybind11::arg("A"),
		  pybind11::arg("B"), pybind11::arg("dims"));
    cl.def_static("zeros", &Tensor::zeros, pybind11::arg("shape"),
		  pybind11::arg("dev") = DEV_CPU);
    cl.def_buffer([](Tensor &t) -> pybind11::buffer_info {
        std::vector<ssize_t> strides(t.ndim);
        ssize_t S = sizeof(float);
        for (int i = t.ndim - 1; i >=0; --i) {
            strides[i] = S;
            S *= t.shape[i];
        }
        return pybind11::buffer_info(
              t.ptr,
              sizeof(float),
              pybind11::format_descriptor<float>::format(),
              t.ndim,
              t.shape,
              strides
        );
    });
    cl.def("__init__", [](Tensor &t, pybind11::buffer b, int device) {
        pybind11::buffer_info info = b.request();
        if (info.format != pybind11::format_descriptor<float>::format())
            throw std::runtime_error("Invalid format: expected a float array");
        bool have_simple_strides = true;
        std::vector<ssize_t> simple_strides(info.ndim);
        ssize_t S = sizeof(float);
        for (int i = info.ndim - 1; i >=0; --i) {
            simple_strides[i] = S;
            S *= info.shape[i];
        }
        for (int i = 0; i < info.ndim; ++i) {
            if (info.strides[i] != simple_strides[i]) {
                have_simple_strides = false;
                break;
            }
        }
        std::vector<int> shape(info.ndim);
        for (int i = 0; i < info.ndim; ++i) {
            shape[i] = info.shape[i];
        }
        new(&t) Tensor(shape, device);
        if (have_simple_strides) {
            std::copy((float*)info.ptr, ((float*)info.ptr) + t.size, t.ptr);
        } else {
            throw std::runtime_error("complex strides not supported");
        }
	}, pybind11::arg("buf"), pybind11::arg("dev") = DEV_CPU);
}
