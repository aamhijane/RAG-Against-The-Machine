import fire
import sys
from src.chunking import split_fixed


def hello(name: str = "John") -> str:
    """Return a greeting for name."""
    return f"Hello {name}"


def chunk_file(file_path: str, max_chunk_size: int = 2000, overlap: int = 0) -> None:
    """Split a file into fixed-size chunks"""
    with open(file_path, mode='r', encoding='utf-8') as f:
        text = f.read()
        chunks = split_fixed(text, file_path, max_chunk_size, overlap)
        if not chunks:
            return
        print(f"Total chunks: {len(chunks)}")
        for i, chunk in enumerate(chunks):
            if i == 3:
                break
            print(f"Chunk {i + 1}: [{chunk.first}, {chunk.last}) width={chunk.last - chunk.first}")
        print(f"Last: [{chunks[-1].first}, {chunks[-1].last}) width={chunks[-1].last - chunks[-1].first}")


def read_span(file_path: str, first: int, last: int) -> None:
    """Read span"""
    with open(file_path, mode='r', encoding='utf-8') as f:
        text = f.read()
        if (first < 0):
            print(f"ERROR: '{first}' must be non-negative")
            return
        if (last < first):
            print(f"ERROR: last={last} must be larger than or equal first={first}")
            return
        if (last > len(text)):
            print(f"ERROR: last={last} is beyond file length {len(text)}")
            return
        piece = text[first:last]
        assert len(piece) == last - first, (
                f"expected {last - first} characters, got {len(piece)}"
        )
        print(f"first: {first}")
        print(f"last: {last}")
        print(f"len: {len(piece)}")
        print("--- BEGIN ---")
        print(piece)
        print("--- END ---")


if __name__ == '__main__':
    try:
        fire.Fire({
            "hello": hello,
            "read_span": read_span,
            "chunk_file": chunk_file
            })
    except ValueError as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)
