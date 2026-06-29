from autoshortai.learning import LearningSignalType, DEFAULT_ADAPTATION_POLICY
from autoshortai.learning.adaptation import plan_suggestions
from autoshortai.learning.engine import LearningEngine

engine = LearningEngine(default_platforms=("generic", "youtube_shorts", "tiktok"))
signal = engine.extract_basic_signal(
    source_id="content_001",
    signal_type=LearningSignalType.RETENTION_PATTERN,
    strength=0.72,
    sample_size=5,
)
insight = engine.generate_basic_insight(
    signal,
    title="Storytelling hook shows good retention",
    summary="The storytelling variant retained viewers better than the baseline.",
)
suggestions = plan_suggestions([insight], "creative_profile:ai_news_default", DEFAULT_ADAPTATION_POLICY)
print(insight.title)
print(suggestions[0].action.value)
