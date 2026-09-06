export function suiteState(selected, recipe) {
  const ids = [...new Set(selected)];
  const expected = new Set(
    recipe ? [...recipe.core, ...recipe.complement] : [],
  );
  const matches = Boolean(
    recipe &&
    ids.length === expected.size &&
    ids.every((id) => expected.has(id)),
  );
  return { ids, matches, empty: ids.length === 0, custom: !matches };
}
export function suiteParams(state, recipeId, area) {
  const params = new URLSearchParams();
  if (area) params.set("area", area);
  if (state.matches && recipeId) params.set("recipe", recipeId);
  else params.set("custom", "1");
  for (const id of state.ids) params.append("benchmark", id);
  return params;
}
