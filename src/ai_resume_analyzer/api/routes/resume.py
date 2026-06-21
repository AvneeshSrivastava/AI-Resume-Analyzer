"""
Resume upload API routes.

Handles HTTP requests for resume upload and delegates processing to services.
"""

from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a resume file (PDF/DOCX).

    Args:
        file: Uploaded resume file

    Returns:
        Basic acknowledgement response
    """

    # Basic API-level validation
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF and DOCX are supported."
        )

    return {
        "message": "File received successfully",
        "filename": file.filename,
        "content_type": file.content_type
    }