"""
Reviewer Agent
Reviews AI-generated drafts for coherence, relevance, style, and academic tone.
"""

import re

class ReviewerAgent:
    def __init__(self):
        # Define evaluation metrics
        self.metrics = ["coherence", "relevance", "style", "grammar"]

    def evaluate(self, draft: str) -> dict:
        """
        Evaluate draft based on predefined metrics.
        """
        print("[Reviewer] Evaluating draft...")
        results = {}

        # Coherence: simple measure by checking section headers
        headers = re.findall(r"##\s+", draft)
        results["coherence"] = "Pass" if len(headers) >= 3 else "Fail"

        # Relevance: check if keywords are present
        keywords = ["assignment", "AI", "agent", "fine-tuned"]
        results["relevance"] = "Pass" if any(k.lower() in draft.lower() for k in keywords) else "Fail"

        # Style & grammar: simulate scoring
        results["style"] = "Good"
        results["grammar"] = "Good"

        return results

    def review(self, draft: str) -> str:
        """
        Returns a detailed review report.
        """
        results = self.evaluate(draft)
        report = "[Reviewer] Draft Evaluation:\n"
        for metric, score in results.items():
            report += f"- {metric.capitalize()}: {score}\n"
        return report


if __name__ == "__main__":
    from planner import PlannerAgent
    from writer import WriterAgent

    topic = "Automating University Assignments using AI Agents"
    planner = PlannerAgent()
    outline = planner.generate_outline(topic)

    writer = WriterAgent()
    draft = writer.generate_draft(outline)

    reviewer = ReviewerAgent()
    feedback = reviewer.review(draft)
    print("\nDraft Review:\n")
    print(feedback)
