# MAPLE License Versioning and Governance Specification

> I used Gemini only for the versioning system to provide several suggestions, which I included to check whether they are valid or unnecessary.

## 1. Version identifier

Each version uses three integers:

`MAJOR.MINOR.ITERATION`

Examples: `0.1.0`, `0.4.12`, `1.0.0`, `1.1.0`.

Periods separate independent integers. They are not decimal points. Each integer can increase without a predetermined upper limit.

- `0.10.0` follows `0.9.0`.
- `0.10.0` and `0.1.0` are different versions.
- An iteration counter can continue through `0.1.9`, `0.1.10`, `0.1.11`, and beyond.
- Leading zeroes within an integer are prohibited. Forms such as `0.01` and `0.001` must not be used.

## 2. Working drafts: `0.X.Y`

While the first integer is `0`, the document is an **Unratified Working Draft**. Under this proposed policy, it is non-operative, grants no copyright or patent permissions, and must not be adopted or applied to any work.

### 2.1 Draft epochs: `0.X.0`

The second integer, `X`, starts at `1` and increases by one for substantive structural changes, including:

- Adding a new section.
- Altering the scope of proposed copyright grants.
- Restructuring the legal architecture.
- Rewriting a core policy or philosophy of the draft.

Increasing `X` resets `Y` to `0`.

Example: `0.1.14` → `0.2.0`.

There is no limit of nine draft epochs. Versions may continue through `0.15.0`, `0.50.0`, or higher while remaining drafts. Reaching a particular number does not require a production release.

### 2.2 Stub iterations: `0.X.Y`

The third integer, `Y`, starts at `0` and increases by one for incremental changes within a draft epoch, including:

- Incremental stub additions.
- Adding or refining an individual definition.
- Phrasing refinements.
- Formatting corrections.
- Clause-level adjustments that do not constitute a substantive structural change.

Example: `0.1.0` → `0.1.1` → `0.1.2`.

### 2.3 Release candidates: `0.X.Y-rc.N`

Once all nine sections and the Appendix are text-complete and undergoing final legal audit, a draft may use the suffix `-rc.N`.

Example: `0.9.0-rc.1`.

A release candidate remains non-operative because its first integer is still `0`. Release-candidate status does not itself constitute ratification.

## 3. Ratified releases: `1.0.0` and above

Under this proposed policy, an operative release requires both:

1. Formal ratification by the License Steward.
2. Publication with a `MAJOR` integer of `1` or greater.

A completed draft or increased version number alone does not satisfy both requirements.

### 3.1 Substantive major releases: `X.0.0`

After the initial operative release, increase the first integer when a change alters legal rights, obligations, conditions, or liabilities.

Examples include:

- Changing attribution requirements.
- Modifying patent-retaliation provisions.
- Altering permissive or copyleft boundaries.
- Changing the scope of permissions or restrictions.

Each major version is a distinct legal instrument with its own immutable canonical URL.

### 3.2 Clarification releases: `X.Y.0`

Increase the second integer for backward-compatible structural improvements that do not change existing grants or impose new conditions.

Examples include:

- Updating non-binding Appendix instructions.
- Adding standardized SPDX identifiers.
- Clarifying ambiguous wording without altering its legal scope.

### 3.3 Errata iterations: `X.Y.Z`

Increase the third integer only for clerical corrections with no effect on legal interpretation.

Examples include:

- Correcting spelling.
- Repairing formatting alignment.
- Correcting punctuation where the correction has no interpretive effect.

The official repository records the complete identifier, such as `1.0.1`.

A suggested option would allow source-code headers to use `Version 1.0` as shorthand for the `1.0.Z` errata family, while retaining the exact three-integer identifier in the official records.

## 4. Published text and permanent references

Once a version is published, the text associated with its exact version identifier and canonical URL is frozen.

Example:

`/licenses/maple/1.0.0/`

Published terms must not be silently replaced at an existing version-specific URL. Changes receive a new version identifier and a corresponding new URL.

This preserves the ability to identify the terms associated with a particular release and avoids retroactively changing the text on which an adopter relied.

## 5. Future-version selection

A dual-option upgrade mechanism has been suggested for Section 9.

### 5.1 Default permission to use later releases

Unless the copyright holder specifies otherwise, a work may be used under its stated operative MAPLE version or a later official operative release.

Drafts beginning with `0` are excluded.

### 5.2 Exact-version restriction

A copyright holder may restrict a work to a particular version by including `ONLY` in the notice.

Example:

`Licensed under MAPLE 1.0.0 ONLY`

Under the proposal, this excludes the default permission to choose later versions.

This suggestion draws on the future-version approach used by the Mozilla Public License.

## 6. Notices without a version identifier

If a work states that it is licensed under “the MAPLE License” without identifying a version, a suggested fallback would allow the recipient to choose only among:

- Officially ratified operative releases.
- Releases published at the time that work was distributed.

All `0.X.Y` drafts are excluded from this fallback.

## 7. Draft notices and premature adoption

Every `0.X.Y` license draft must contain an explicit notice that it is non-operative and grants no rights or permissions.

A suggested notice would state that any purported grant under a draft version is **void ab initio**, meaning invalid from the outset.

The intended safeguard is to prevent someone from treating an incomplete draft as an unrestricted license merely because its substantive restrictions have not yet been written.

Release candidates retain the same draft restriction until formal ratification and publication.

## 8. References to future releases and websites

One suggestion is to remove promises about when a website or “Version 1” will become available from the draft legal text.

Instead, draft location fields would identify the present status:

`<NO OPERATIVE URI, UNRATIFIED WORKING DRAFT>`

The proposal is intended to avoid:

- References to terms or websites that do not yet exist.
- An implication that a draft automatically converts into a later operative license.
- A commitment to a particular release name or launch date.

A future release remains a separate publication requiring the ratification and publication steps described above.

## 9. Safeguards covered by the proposal

| Scenario | Proposed safeguard |
|---|---|
| Someone adopts an incomplete draft and claims unrestricted permission. | Explicit non-operative status and a no-grant notice in every draft. |
| Published license text changes at the same URL. | Frozen version-specific text and immutable canonical URLs. |
| A later release changes terms that an author did not intend to permit. | An `ONLY` notice allows the author to select an exact version. |
| A work names MAPLE without specifying a version. | Selection is limited to ratified operative releases available at distribution. |
| A draft points to an unbuilt website or promises a future release. | Present-status location text and no automatic conversion to future terms. |

## 10. TL;DR

Read the version as three separate whole numbers. The dots are separators, so `0.10.0` comes after `0.9.0`. There is no nine-update limit, and numbers must not be padded with extra zeroes.

### While we are drafting

- **Starts with `0`:** It is a draft, grants no permissions, and must not be used as a license.
- **Small change:** Increase the last number, for example, `0.1.0` → `0.1.1`.
- **Major structural or policy change:** Increase the middle number and reset the last number, for example, `0.1.14` → `0.2.0`.
- **Ready for final review:** Add `-rc.N`, for example, `0.9.0-rc.1`. It is still a draft.
- **Ready for an operative release:** The License Steward must formally ratify it and publish it with a first number of at least `1`. Renumbering alone does not make it operative.

### After an operative release

- **Rights, obligations, conditions, or liabilities change:** Increase the first number.
- **A structural improvement or clarification changes no grants or conditions:** Increase the middle number.
- **A clerical correction changes no legal meaning:** Increase the last number.
- Keep the exact three-number version in the official records. The proposal allows `1.0` in a source-code header as shorthand for the `1.0.Z` errata family.

### Rules that apply across versions

- Never overwrite published text at its version-specific URL. Give changed text a new version and URL.
- By default, the proposal allows the stated operative version or a later official operative release. An `ONLY` notice restricts the work to the stated version.
- If no version is stated, the proposed fallback allows only ratified operative releases already published when the work was distributed.
- Drafts are excluded from both version-selection rules. Keep their no-permission notices, avoid promises about future websites or releases, and do not treat them as automatically becoming operative later.
