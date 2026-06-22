"""
Resume service.

Contains business logic related to resume processing.
"""

from fastapi import UploadFile


class ResumeService:
    """Service responsible for processing uploaded resumes.
    """

    async def process_resume(self, file: UploadFile) -> dict:   
        """
        Process the uploaded resume file.
        Args:
            file (UploadFile): The uploaded resume file.
        returns:
            dict: A dictionary containing the processed resume data.
        """
        return{
            "filename": file.filename,
            "content_type": file.content_type,
            "status": "received",
            "message": "Resume successfully received for processing."
            }
resume_service = ResumeService()