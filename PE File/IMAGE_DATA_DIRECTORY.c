typedef struct _IMAGE_DATA_DIRECTORY {

    uint32_t VirtualAddress; // RVA of the table

    uint32_t Size;           // Size of the table

} IMAGE_DATA_DIRECTORY32, *PIMAGE_DATA_DIRECTORY32;