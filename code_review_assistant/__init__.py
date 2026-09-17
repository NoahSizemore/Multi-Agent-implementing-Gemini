# code_review_assistant/__init__.py
"""
Code Review Assistant - An intelligent code grading system using ADK.

This package provides a multi-agent system for reviewing Python code,
checking style compliance, running tests, and providing personalized feedback.
"""

try:
    from .agent import agent, root_agent
    __all__ = ["agent", "root_agent"]
except (ImportError, AttributeError) as e:
    import logging
    logging.getLogger(__name__).error(f"Failed to automatically discover root agent: {e}", exc_info=True)
    __all__ = []