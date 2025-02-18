import wave
import numpy as np

inp = input("Filename of the file you want to convert>>  \n")
out = input("Name of the output file>>  \n")
func =  out + ".wav"
def encode_file_to_wav(input_filename, output_wav):
    # Read binary data
    with open(input_filename, "rb") as f:
        binary_data = f.read()

    # Convert binary data to 16-bit PCM values
    samples = np.frombuffer(binary_data, dtype=np.uint8)  # 8-bit raw values
    samples = (samples - 128) * 256  # Convert to signed 16-bit

    # Create WAV file
    with wave.open(output_wav, "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit audio
        wav_file.setframerate(44100)  # Sample rate
        wav_file.writeframes(samples.astype(np.int16).tobytes())

    print(f"Encoded {input_filename} to {output_wav}")

# Example usage
if __name__ == "__main__":
    encode_file_to_wav(inp, func)
