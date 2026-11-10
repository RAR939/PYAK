from behave import given, then

from main import build_figures


@given("the figures for variant {variant:d}")
def prepare_figures(context, variant):
    context.figures = build_figures(variant)


@then('figure {number:d} is described as "{description}"')
def check_description(context, number, description):
    assert repr(context.figures[number - 1]) == description
