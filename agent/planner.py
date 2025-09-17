"""
Planner Agent
Generates structured outlines for academic tasks using reasoning and templates.
"""

import random

class PlannerAgent:
    def __init__(self):
        # Predefined section templates
        self.templates = {
            "Introduction": [
                "Context and motivation",
                "Problem statement",
                "Significance of the task"
            ],
            "Methodology": [
                "System design and architecture",
                "Fine-tuning approach",
                "Data preparation",
                "Evaluation methodology"
            ],
            "Results": [
                "Performance metrics",
                "Quantitative results",
                "Qualitative analysis"
            ],
            "Conclusion": [
                "Summary of findings",
                "Limitations",
                "Future work and improvements"
            ]
        }

    def generate_outline(self, topic: str) -> dict:
        """
        Generates an outline for the given topic.
        Uses a mix of predefined templates and randomized details to simulate reasoning.
        """
        print(f"[Planner] Generating outline for topic: {topic}")
        outline = {}
        for section, points in self.templates.items():
            outline[section] = [f"{point} on '{topic}'" for point in points]
        return outline


if __name__ == "__main__":
    topic = "Automating University Assignments using AI Agents"
    planner = PlannerAgent()
    plan = planner.generate_outline(topic)
    print("\nGenerated Outline:")
    for section, points in plan.items():
        print(f"\n## {section}")
        for p in points:
            print(f"- {p}")
