use pyo3::prelude::*;
use aes::Aes128;
use aes::cipher::{KeyInit, BlockEncrypt, generic_array::GenericArray};

#[pyfunction]
fn aes_encrypt(data: Vec<u8>, key: Vec<u8>) -> PyResult<Vec<u8>> {
    if key.len() != 16 {
        return Err(pyo3::exceptions::PyValueError::new_err("Key must be 16 bytes"));
    }
    let cipher = Aes128::new(GenericArray::from_slice(&key));
    let mut block = GenericArray::clone_from_slice(&data[0..16]);
    cipher.encrypt_block(&mut block);
    Ok(block.to_vec())
}

#[pymodule]
fn fastlib(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(aes_encrypt, m)?)?;
    Ok(())
}
