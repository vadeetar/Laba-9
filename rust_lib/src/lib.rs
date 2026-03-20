use pyo3::prelude::*;
use aes::Aes128;
use aes::cipher::{KeyInit, BlockEncrypt, generic_array::GenericArray};

#[pyfunction]
fn aes_encrypt(data: Vec<u8>, key: Vec<u8>) -> PyResult<Vec<u8>> {
    if key.len() != 16 {
        return Err(pyo3::exceptions::PyValueError::new_err("Key must be 16 bytes"));
    }
    
    if data.len() != 16 {
        return Err(pyo3::exceptions::PyValueError::new_err("Data must be 16 bytes"));
    }
    
    let cipher = Aes128::new(GenericArray::from_slice(&key));
    let mut block = GenericArray::clone_from_slice(&data[0..16]);
    cipher.encrypt_block(&mut block);
    
    Ok(block.to_vec())
}



#[pyfunction]
fn resize_image(input_path: String, output_path: String, width: u32, height: u32) -> PyResult<bool> {
    use image::GenericImageView;
    
 
    let img = image::open(&input_path)
        .map_err(|e| pyo3::exceptions::PyIOError::new_err(format!("Failed to open image: {}", e)))?;
    

    let resized = img.resize_exact(width, height, image::imageops::FilterType::Lanczos3);
    

    resized.save(&output_path)
        .map_err(|e| pyo3::exceptions::PyIOError::new_err(format!("Failed to save image: {}", e)))?;
    
    Ok(true)
}


#[pymodule]
fn fastlib(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(aes_encrypt, m)?)?;
    m.add_function(wrap_pyfunction!(resize_image, m)?)?;
    Ok(())
}


#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_aes_encrypt() {
        let data = vec![0u8; 16];
        let key = vec![1u8; 16];
        let result = aes_encrypt(data, key).unwrap();
        assert_eq!(result.len(), 16);
    }
    
    #[test]
    fn test_aes_encrypt_invalid_key() {
        let data = vec![0u8; 16];
        let key = vec![1u8; 15];
        assert!(aes_encrypt(data, key).is_err());
    }
}