extern crate crypto;
extern crate regex;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use regex::Regex;

pub mod cryptography;

#[pyclass]
struct AES {}

#[pymethods]
impl AES {
    #[staticmethod]
    fn encrypt(payload: &str, key: &str, iv: &str) -> String {
        cryptography::encrypt_to_base64(payload, key, iv)
    }

    #[staticmethod]
    fn decrypt(payload: &str, key: &str, iv: &str) -> String {
        cryptography::decrypt_from_base64(payload, key, iv)
    }
}

#[pyclass]
struct RegexUtil {}

#[pymethods]
impl RegexUtil {
    #[staticmethod]
    fn is_match(pattern: &str, content: &str) -> bool {
        is_match(pattern, content)
    }
}

#[pyfunction]
fn is_match(pattern: &str, content: &str) -> bool {
    let re = Regex::new(pattern).unwrap();
    re.is_match(content)
}

#[pymodule]
fn rustpy_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<RegexUtil>()?;
    m.add_class::<AES>()?;
    m.add_wrapped(wrap_pyfunction!(is_match))?;
    m.add("version", "0.2.1")?;

    Ok(())
}
