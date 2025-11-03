typedef struct _IMAGE_NT_HEADERS {

    uint32_t Signature;                     // PE Signature
    IMAGE_FILE_HEADER FileHeader;           // File header
    IMAGE_OPTIONAL_HEADER32 OptionalHeader;   // Optional header

} IMAGE_NT_HEADERS32, *PIMAGE_NT_HEADERS32;