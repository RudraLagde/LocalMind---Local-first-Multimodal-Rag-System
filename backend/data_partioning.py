from unstructured.partition.pdf import partition_pdf
from unstructured.chunking import chunk_by_title


def document_partition(file_path: str):
    
    elements = partition_pdf(
        filename= file_path , 
        strategy="hi_res",
        infer_table_structure=True , 
        extract_image_block_types=["Image"],
        extract_image_block_to_payload= True
    )

    no_of_element = print(f"Number of partiotion created {len(elements)}")

    return elements


