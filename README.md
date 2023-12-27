# BPE

An implementation of byte-pair encoding in Python.

> [!WARNING]
> I wrote this project to learn about byte-pair encoding. This project is not intended for production use.

## Setup

To set up this project, first clone the project and install the project from source:

```
git clone https://github.com/capjamesg/bpe
cd bpe/
pip3 install -e .
```

### Test the encoder

Open `bpe.py`. Update the `text` variable to be the text you want to use to train your byte-pair encoder.

Then, update the `input_seq` value toward the end of `bpe.py` to include some demo text to encode using your encoder.

Run the script to test the encoder.

> [!NOTE]
> This script doesn't save your encoding. I recommend adding your own saving logic if you want to use the encoder on large text samples.

## License

This project is licensed under an [MIT license](LICENSE).
