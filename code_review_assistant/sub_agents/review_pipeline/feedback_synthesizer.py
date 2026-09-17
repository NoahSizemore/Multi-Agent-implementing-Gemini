"""
Feedback Synthesizer Agent - Provides comprehensive, personalized feedback.

This agent synthesizes all analysis results into constructive feedback,
incorporating past feedback history and tracking improvement over time.
"""

from google.adk.agents import Agent
from google.adk.agents.readonly_context import ReadonlyContext
from google.adk.tools import FunctionTool
from google.adk.utils import instructions_utils
from code_review_assistant.config import config
from code_review_assistant.tools import search_past_feedback, update_grading_progress, save_grading_report


# MODULE_5_STEP_4_INSTRUCTION_PROVIDER
def synthesizer_instruction_provider(context: ReadonlyContext) -> str:
    """Generates dynamic instructions ensuring past context and reports are handled."""
    return """You are a senior code reviewer and educational mentor. Your goal is to synthesize all findings from the code review pipeline into a comprehensive, encouraging, and structured markdown report.

Follow this exact operational workflow:
1. Call `search_past_feedback` to find any historical issues or improvement patterns for the developer.
2. Gather the structural analysis, style violations, and test results from the shared session state.
3. Write a personalized synthesis report containing:
   - A descriptive overall score and structural health assessment.
   - Breakdown of syntax or style issues with actionable advice.
   - Educational deep-dives explaining *why* a fix is recommended.
4. Call `update_grading_progress` to update metrics, track lifetime attempts, and compute score updates.
5. Call `save_grading_report` and pass your full synthesized markdown report to persist the final artifact.
6. Return the exact markdown feedback text as your final response.

Be encouraging, professional, and thorough. Use clear markdown headers and code blocks for readability."""


# MODULE_5_STEP_4_SYNTHESIZER_AGENT
feedback_synthesizer_agent = Agent(
    name="FeedbackSynthesizer",
    model=config.critic_model,
    description="Synthesizes architectural analysis, style compliance, and test runs into an artifact-backed report.",
    instruction=synthesizer_instruction_provider,
    tools=[
        FunctionTool(func=search_past_feedback),
        FunctionTool(func=update_grading_progress),
        FunctionTool(func=save_grading_report)
    ],
    output_key="final_feedback"
)