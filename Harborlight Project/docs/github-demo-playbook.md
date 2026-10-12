# GitHub demo 

This guide gives you sample content to add to GitHub's project-management features after uploading the files. GitHub interface labels may vary slightly by account.

## Suggested labels

Create labels such as `type:story`, `type:bug`, `type:task`, `area:quote`, `area:discounts`, `area:documents`, `priority:high`, `priority:medium`, and `priority:low`. Apply a type, an area, and a priority label to each issue where it fits.

## Suggested milestones

- **Quote flow demo** — target 2026-11-13
- **QA readout** — target 2026-11-20

These dates are fictional. Add the relevant issues to each milestone to demonstrate progress.

## Sample issues to create

Create these as individual issues using the repository's issue forms.

### Story: show an estimate after valid quote details

**Labels:** `type:story`, `area:quote`, `priority:high`  
**Milestone:** Quote flow demo  
**Description:** As a prospective customer, I want to see an estimated premium after entering valid vehicle and driver details so I can decide whether to continue.  
**Acceptance criteria:** A complete valid quote displays an estimate and a quote reference; incomplete required fields display helpful prompts.

### Bug: multi-vehicle discount missing from estimate

**Labels:** `type:bug`, `area:discounts`, `priority:high`  
**Milestone:** Quote flow demo  
**Description:** With two eligible vehicles, the estimate appears to include only the safe-driver discount.  
**Expected:** Both eligible discounts are reflected according to the sample rule.  
**Observed:** The multi-vehicle reduction is absent from the displayed breakdown.  
**Demo impact:** The displayed estimate is inconsistent with requirement REQ-004.

### Task: add document upload test coverage

**Labels:** `type:task`, `area:documents`, `priority:medium`  
**Milestone:** QA readout  
**Description:** Add manual coverage for accepted file types, size limits, and a retry after an interrupted upload. Link the cases to REQ-005.

## Suggested Project fields

Use a board view with a **Status** field (Backlog, Ready, In progress, In review, Done), **Priority**, and **Area**. Add the sample issues and move cards as you narrate the workflow. A table view can show the same issues grouped by milestone or area.

## Demo narration

Show how the README links to details, how issue forms standardize new work, how labels help filter the backlog, how milestones group a release goal, and how a Project view displays status. Finish by opening a Markdown change in Git history to show a readable documentation update.
