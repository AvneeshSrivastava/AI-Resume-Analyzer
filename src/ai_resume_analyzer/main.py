"""
Application entry point for the AI Resume Analyzer.

This module creates and configures the FastAPI application instance.
"""

from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered resume analysis platform built with FastAPI.",
    version="0.1.0",
)