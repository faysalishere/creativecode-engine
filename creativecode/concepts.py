"""Curated concept architecture generator. No LLM or online service is invoked."""

from __future__ import annotations
from copy import deepcopy
from pathlib import Path
from typing import Any
import json

SUPPORTED_KINDS = ("portfolio", "directory", "product")
STRUCTURE_KEYS = (
    "hero_structure", "information_architecture", "navigation_model",
    "content_presentation", "interaction_model",
)

# Different information and interaction architectures, not different colors.
PATTERNS = {
    "portfolio": (
        {
            "id": "A", "name": "Editorial flagship",
            "thesis": "Introduce the creator through an editorial identity and establish credibility with long-form project stories.",
            "hero_structure": "asymmetric_portrait_identity",
            "information_architecture": "identity_then_sequential_work_stories",
            "navigation_model": "compact_top_anchor_navigation",
            "content_presentation": "full_width_case_study_sections",
            "interaction_model": "scroll_driven_story_reveal",
            "desktop_wireframe": ["Identity copy + authentic portrait in asymmetric frame", "Featured work as expansive editorial case studies", "Expertise, philosophy and contact in distinct reading zones"],
            "mobile_wireframe": ["Identity first; portrait placed below introduction", "One immersive project story per section", "Compact accessible section navigation and direct contact"],
            "tradeoff": "Strong narrative, but lengthy pages require careful navigation and performance testing.",
            "risk": "Long-form reading may slow visitors looking for a specific project.",
            "effort": "medium",
        },
        {
            "id": "B", "name": "Project dossier",
            "thesis": "Make completed work the primary proof, with clear project context and scannable project records.",
            "hero_structure": "compact_identity_and_active_dossier",
            "information_architecture": "project_index_then_deep_dossiers",
            "navigation_model": "persistent_numbered_project_rail",
            "content_presentation": "selectable_project_dossier_panels",
            "interaction_model": "project_selection_updates_detail_pane",
            "desktop_wireframe": ["Compact creator header above selected project", "Numbered project rail beside detailed project dossier", "Skills and contact in a quiet lower information strip"],
            "mobile_wireframe": ["Concise creator header with work-first CTA", "Accessible expandable project dossiers in source order", "Expertise and contact under project index"],
            "tradeoff": "Fast work discovery, but selected-panel behavior needs keyboard and deep-link support.",
            "risk": "Tab-like interactions may hide details from search engines or keyboard users if implemented poorly.",
            "effort": "medium",
        },
        {
            "id": "C", "name": "Cinematic chapters",
            "thesis": "Use distinct narrative chapters to connect the creator's philosophy with selected work without repeating a card grid.",
            "hero_structure": "typographic_manifesto_and_chapter_index",
            "information_architecture": "identity_then_thematic_chapters",
            "navigation_model": "chapter_index_with_skip_links",
            "content_presentation": "chapter_headlines_and_ordered_work_index",
            "interaction_model": "chapter_navigation_and_controlled_reveal",
            "desktop_wireframe": ["Full-height manifesto with explicit chapter index", "Thematic storytelling chapters with project index", "Closing invitation with clear contact action"],
            "mobile_wireframe": ["Readable manifesto with visible jump-to-work control", "Stacked chapters and numbered project links", "No scroll hijacking; reduced-motion alternative"],
            "tradeoff": "Memorable storytelling, but motion must never obstruct direct access to work.",
            "risk": "Animation-heavy layouts can impair readability, low-power performance and motion sensitivity.",
            "effort": "high",
        },
    ),
    "directory": (
        {
            "id": "A", "name": "Search utility",
            "thesis": "Help someone locate a precise item as quickly as possible.",
            "hero_structure": "prominent_query_and_location",
            "information_architecture": "query_results_then_categories",
            "navigation_model": "search_to_results_to_detail",
            "content_presentation": "dense_scannable_result_rows",
            "interaction_model": "search_filter_sort",
            "desktop_wireframe": ["Search and location bar", "Filter rail with dense results list", "Item detail with verified information"],
            "mobile_wireframe": ["Sticky search and compact filters", "Readable results rows", "Accessible item details and back navigation"],
            "tradeoff": "Excellent for known-item retrieval; less helpful to users unsure what to search.",
            "risk": "Incomplete search results must be communicated clearly.",
            "effort": "medium",
        },
        {
            "id": "B", "name": "Guided finder",
            "thesis": "Guide users from a need to a matching service in a few choices.",
            "hero_structure": "single_question_as_entry",
            "information_architecture": "need_selection_then_filtered_categories",
            "navigation_model": "question_wizard_with_browse_exit",
            "content_presentation": "progressive_recommendation_list",
            "interaction_model": "stepwise_need_filtering",
            "desktop_wireframe": ["One prominent question", "Choice steps and contextual explanation", "Matching service list"],
            "mobile_wireframe": ["One question per screen", "Clear back and exit buttons", "Compact matching listings"],
            "tradeoff": "Accessible discovery, but users must always have an immediate browse alternative.",
            "risk": "Poor question choices could obscure relevant categories.",
            "effort": "high",
        },
        {
            "id": "C", "name": "Service atlas",
            "thesis": "Show an understandable overview of available service families for open-ended browsing.",
            "hero_structure": "compact_context_and_category_index",
            "information_architecture": "category_overview_then_local_details",
            "navigation_model": "category_tree_to_details",
            "content_presentation": "hierarchical_service_index",
            "interaction_model": "browse_expand_compare",
            "desktop_wireframe": ["Compact local context", "Category tree and detail reading pane", "Related listings"],
            "mobile_wireframe": ["Compact introduction", "Accessible category accordions", "Detail rows after category selection"],
            "tradeoff": "Excellent for browsing; very large taxonomies require pruning.",
            "risk": "Dense category navigation can overwhelm small screens.",
            "effort": "medium",
        },
    ),
    "product": (
        {
            "id": "A", "name": "Outcome-first overview",
            "thesis": "Lead with a concrete outcome and reveal the product's capabilities as evidence.",
            "hero_structure": "outcome_and_verified_product_media",
            "information_architecture": "outcome_then_proof_then_capabilities",
            "navigation_model": "focused_top_navigation",
            "content_presentation": "use_case_editorial_sections",
            "interaction_model": "guided_reading_and_primary_cta",
            "desktop_wireframe": ["Outcome and product preview", "Use-case explanation and real proof", "Capabilities and action"],
            "mobile_wireframe": ["Single outcome statement", "Use-case reading flow", "Direct accessible action"],
            "tradeoff": "Clear for new visitors, but not optimized for technical comparisons.",
            "risk": "Unsupported product claims must not appear as evidence.",
            "effort": "low",
        },
        {
            "id": "B", "name": "Interactive product workspace",
            "thesis": "Explain the product through a working-task walkthrough rather than a marketing grid.",
            "hero_structure": "active_workspace_preview",
            "information_architecture": "workflow_demo_then_details",
            "navigation_model": "task_steps_and_context",
            "content_presentation": "task_state_panels",
            "interaction_model": "guided_task_walkthrough",
            "desktop_wireframe": ["Realistic task demo", "Context and step rail", "Relevant outcome and action"],
            "mobile_wireframe": ["Single task state", "Progressive steps", "Alternative direct-action path"],
            "tradeoff": "Concrete product learning, but demos must avoid fake functional claims.",
            "risk": "A simulated demo can be mistaken for a real working service.",
            "effort": "high",
        },
        {
            "id": "C", "name": "Evaluation matrix",
            "thesis": "Let experienced buyers assess fit through practical criteria, not generic features.",
            "hero_structure": "compact_value_and_fit_filters",
            "information_architecture": "requirements_then_capabilities_then_tradeoffs",
            "navigation_model": "evaluation_sections_and_anchor_map",
            "content_presentation": "criteria_and_evidence_rows",
            "interaction_model": "expand_criteria_compare_fit",
            "desktop_wireframe": ["Product fit statement", "Criteria and evidence matrix", "Tradeoff notes and contact action"],
            "mobile_wireframe": ["Compact fit statement", "Stacked criteria with visible labels", "Accessible detail expansion"],
            "tradeoff": "Helpful for high-intent technical audiences; can feel dense for first-time visitors.",
            "risk": "Unsupported benchmarks or customer statistics must be omitted.",
            "effort": "medium",
        },
    ),
}


def validate_brief(brief: Any) -> dict:
    if not isinstance(brief, dict):
        raise ValueError("Brief must be a JSON object")
    required = ("project_id", "project_type", "project_name", "audience", "primary_goal", "primary_action", "constraints", "content_items")
    missing = [k for k in required if k not in brief]
    if missing:
        raise ValueError("Missing brief fields: " + ", ".join(missing))
    for k in ("project_id", "project_name", "primary_goal", "primary_action"):
        if not isinstance(brief[k], str) or not brief[k].strip():
            raise ValueError(f"{k} must be a nonempty string")
    if brief["project_type"] not in SUPPORTED_KINDS:
        raise ValueError("project_type must be one of: " + ", ".join(SUPPORTED_KINDS))
    if not isinstance(brief["audience"], list) or not brief["audience"] or not all(isinstance(x, str) and x.strip() for x in brief["audience"]):
        raise ValueError("audience must be a nonempty list of strings")
    if not isinstance(brief["constraints"], dict):
        raise ValueError("constraints must be a JSON object")
    if not isinstance(brief["content_items"], list) or not all(isinstance(x, dict) and isinstance(x.get("title"), str) and x["title"].strip() for x in brief["content_items"]):
        raise ValueError("content_items must be an array of objects with title")
    if not brief["content_items"]:
        raise ValueError("content_items may not be empty; add at least one genuine item")
    return brief


def generate(brief: dict) -> dict:
    """Return three curated architectures; this is NOT model-generated design."""
    brief = validate_brief(brief)
    source_items = [x["title"] for x in brief["content_items"]]
    concepts = []
    for pattern in PATTERNS[brief["project_type"]]:
        concept = deepcopy(pattern)
        concept.update({
            "primary_action": brief["primary_action"],
            "featured_content_in_source_order": source_items,
            "project_constraints": deepcopy(brief["constraints"]),
            "audience": deepcopy(brief["audience"]),
            "project_goal": brief["primary_goal"],
            "asset_policy": "Use only verified project assets; identify missing assets, never fabricate live screenshots, logos, or personal facts.",
            "scope": "Concept-only exploration; no production changes or implementation approval.",
        })
        concepts.append(concept)
    return {
        "schema_version": "1.2", "project_id": brief["project_id"],
        "project_name": brief["project_name"], "project_type": brief["project_type"],
        "generator": "curated-architecture-library-no-llm",
        "disclaimer": "These are structured starting points, NOT original AI art, verified UX findings or shipped designs.",
        "concepts": concepts,
    }


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_json(path: str | Path, data: dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
