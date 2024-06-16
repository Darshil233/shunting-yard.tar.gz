import expreval

def test_parse():
    evaluator = expreval.ExpressionEvaluator()
    assert evaluator.parse("( 5 - 3 ) / 2") == "5 3 - 2 /"

def test_evaluate():
    evaluator = expreval.ExpressionEvaluator()
    assert evaluator.evaluate("5 3 - 2 /") == 1.0

def test_invert_precedence():
    evaluator = expreval.ExpressionEvaluator(invert_precedence=True)
    assert evaluator.parse("5 + 2 * 3") == "5 2 3 * +"
