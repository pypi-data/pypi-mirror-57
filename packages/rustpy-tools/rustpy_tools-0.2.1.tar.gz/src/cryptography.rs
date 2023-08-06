extern crate crypto;

use crypto::buffer::{BufferResult, ReadBuffer, WriteBuffer};
use crypto::{aes, blockmodes, buffer};
extern crate base64;

use base64::{decode, encode};

pub fn encrypt_to_base64(payload: &str, key: &str, iv: &str) -> String {
    let mut encryptor = aes::cbc_encryptor(
        aes::KeySize::KeySize128,
        key.as_bytes(),
        iv.as_bytes(),
        blockmodes::PkcsPadding,
    );

    let mut final_result = Vec::<u8>::new();
    let mut read_buffer = buffer::RefReadBuffer::new(payload.as_bytes());
    let mut buffer = [0; 4096];
    let mut write_buffer = buffer::RefWriteBuffer::new(&mut buffer);

    loop {
        let result = encryptor
            .encrypt(&mut read_buffer, &mut write_buffer, true)
            .unwrap();
        final_result.extend(
            write_buffer
                .take_read_buffer()
                .take_remaining()
                .iter()
                .map(|&i| i),
        );
        match result {
            BufferResult::BufferUnderflow => break,
            BufferResult::BufferOverflow => {}
        }
    }
    let final_result = encode(&final_result);
    final_result
}

pub fn decrypt_from_base64(payload: &str, key: &str, iv: &str) -> String {
    let encrypted_data = match decode(payload) {
        Ok(v) => v,
        Err(e) => panic!("Base64 decode error: {}", e),
    };

    let mut decryptor = aes::cbc_decryptor(
        aes::KeySize::KeySize128,
        key.as_bytes(),
        iv.as_bytes(),
        blockmodes::PkcsPadding,
    );
    let mut final_result = Vec::<u8>::new();
    let mut read_buffer = buffer::RefReadBuffer::new(&encrypted_data);
    let mut buffer = [0; 4096];
    let mut write_buffer = buffer::RefWriteBuffer::new(&mut buffer);
    loop {
        let result = decryptor
            .decrypt(&mut read_buffer, &mut write_buffer, true)
            .unwrap();
        final_result.extend(
            write_buffer
                .take_read_buffer()
                .take_remaining()
                .iter()
                .map(|&i| i),
        );
        match result {
            BufferResult::BufferUnderflow => break,
            BufferResult::BufferOverflow => {}
        }
    }

    let final_result = match String::from_utf8(final_result.to_vec()) {
        Ok(v) => v,
        Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
    };

    final_result
}
