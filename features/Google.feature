Feature: To verify element on the page after performing search action
  Background:
    Given I launched chrome browser
    When I opened google URL
    When I searched python
  Scenario: Verify page with positive scenario
    Then Title is verified after performing search action
  Scenario: Verify page with negative scenario
    Then Title is not verified after performing search action