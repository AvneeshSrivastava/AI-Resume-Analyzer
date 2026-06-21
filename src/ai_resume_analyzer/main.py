"""
Application entry point for AI Resume Analyzer.
"""

from fastapi import FastAPI

from ai_resume_analyzer.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="AI-powered resume analysis platform built with FastAPI.",
    version=settings.app_version,
)


@app.get("/health")
def health_check():
    """
    Health check endpoint to verify application status.
    """
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
    }