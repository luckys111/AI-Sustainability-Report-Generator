from rag.vector_store import (
    create_style_library
)

STYLE_LIBRARY = create_style_library()


def get_style_examples(
        query=None,
        k=5
):

    examples = STYLE_LIBRARY[:k]

    return "\n\n".join(
        examples
    )