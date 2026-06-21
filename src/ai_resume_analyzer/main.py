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