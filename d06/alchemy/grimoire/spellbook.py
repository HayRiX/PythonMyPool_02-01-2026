def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    check_ingredients = validate_ingredients(ingredients)
    if "INVALID" not in check_ingredients:
        return f"Spell recorded: {spell_name} ({check_ingredients})"
    else:
        return f"Spell rejected: {spell_name} ({check_ingredients})"
