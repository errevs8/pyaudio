import wave
import numpy as np
inp = input("filename of the file you want to convert back>>  \n")
out = input("filename of the original file>>  \n")

def decode_wav_to_file(input_wav, output_filename):
    # Open the WAV file
    with wave.open(input_wav, "rb") as wav_file:
        frames = wav_file.readframes(wav_file.getnframes())

    # Convert 16-bit PCM to original 8-bit binary
    samples = np.frombuffer(frames, dtype=np.int16)
    binary_data = ((samples / 256) + 128).astype(np.uint8).tobytes()

    # Save reconstructed file
    with open(output_filename, "wb") as f:
        f.write(binary_data)

    print(f"Decoded {input_wav} back to {output_filename}")

# Example usage
if __name__ == "__main__":
    decode_wav_to_file(inp, out)
