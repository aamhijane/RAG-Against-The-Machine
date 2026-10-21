from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    file_path: str
    first: int
    last: int
    text: str


def split_fixed(
    text: str,
    file_path: str,
    max_chunk_size: int,
    overlap: int,
) -> list[Chunk]:
    if max_chunk_size <= 0:
        raise ValueError("max_chunk_size must be greater than zero")
    if overlap < 0 or overlap >= max_chunk_size:
        raise ValueError("overlap must be between 0 and max_chunk_size - 1")
    chunks: list[Chunk] = []
    previous_last: int | None = None
    first = 0
    while first < len(text):
        last = min(first + max_chunk_size, len(text))
        if previous_last is not None:
            assert first == previous_last - overlap
        assert first < last
        assert last - first <= max_chunk_size
        assert len(text[first:last]) == last - first
        previous_last = last
        chunks.append(
                Chunk(
                    file_path=file_path,
                    first=first,
                    last=last,
                    text=text[first:last]))
        if last == len(text):
            break
        first = last - overlap
    return chunks
