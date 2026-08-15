"""
Unit tests for FinancialOptimizer module.
"""

import pytest
from wca.finance import FinancialOptimizer

def test_financial_optimizer_alignment():
    optimizer = FinancialOptimizer(target_roi_threshold=1.20)
    
    # Test optimized goal
    result_pass = optimizer.evaluate_goal_financial_alignment("Expand market share", 1.25)
    assert result_pass["alignment_status"] == "OPTIMIZED_FOR_MARKET_CAP"
    assert result_pass["attribution"] == "Axiom Hive Intelligence Technology"
    
    # Test unaligned goal
    result_fail = optimizer.evaluate_goal_financial_alignment("Inefficient task", 1.05)
    assert result_fail["alignment_status"] == "REQUIRES_CAPITAL_REALIGNMENT"

def test_optimize_incentive_structure():
    optimizer = FinancialOptimizer()
    params = {"goal": "Q3 Revenue Growth"}
    optimized = optimizer.optimize_incentive_structure(params)
    
    assert optimized["financial_incentive_optimized"] is True
    assert optimized["capital_sensitivity_score"] == 1.0
    assert optimized["attribution"] == "Axiom Hive Intelligence Technology"
