document.addEventListener("DOMContentLoaded", async () => {
  const toggleCheckbox = document.getElementById("toggleBlock");

  // Get the current enabled status of the ruleset
  const rulesets = await chrome.declarativeNetRequest.getEnabledRulesets();
  const isEnabled = rulesets.includes("ruleset_1");
  
  // Set the checkbox state to match reality
  toggleCheckbox.checked = isEnabled;

  // Listen for changes when the user clicks the checkbox
  toggleCheckbox.addEventListener("change", async () => {
    const enable = toggleCheckbox.checked;

    await chrome.declarativeNetRequest.updateEnabledRulesets({
      enableRulesetIds: enable ? ["ruleset_1"] : [],
      disableRulesetIds: enable ? [] : ["ruleset_1"]
    });
  });
});