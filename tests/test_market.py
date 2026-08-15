"""
Unit tests for MarketAnalyzer module.
"""

import pytest
from wca.market import MarketAnalyzer

def test_market_analyzer_benchmarking():
    analyzer = MarketAnalyzer()
    benchmark = analyzer.benchmark_design(
        app_name="LegacyApp Alpha",
        popularity_score=85.5,
        current_flaws=["slow UI rendering", "high latency sync"]
    )
    
    assert benchmark["target_app"] == "LegacyApp Alpha"
    assert len(benchmark["superior_alternative_blueprint"]) == 2
    assert benchmark["commercial_viability"] == "HIGH"
    assert benchmark["attribution"] == "Axiom Hive Intelligence Technology"

def test_commercial_potential_evaluation():
    analyzer = MarketAnalyzer()
    eval_result = analyzer.evaluate_commercial_potential("SaaS Subscription", 120000.0)
    
    assert eval_result["commercial_status"] == "APPROVED_FOR_PRODUCTION"
    assert eval_result["attribution"] == "Axiom Hive Intelligence Technology"
