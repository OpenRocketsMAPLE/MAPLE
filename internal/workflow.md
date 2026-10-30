# MAPLE Team Workflow

The working sequence is: **private GitHub repository → Overleaf research document → approved publication package → Zenodo record and DOI → external review → documented revisions → next version**.

The license text and white paper are separate documents. The license contains the proposed terms; the white paper explains the problem, research, policy choices, and reasoning behind those terms.

## 1. Develop and record work in GitHub

- Maintain the license draft and supporting documents in the private GitHub repository.
- Record the current version, changes, and supporting references. Use the [versioning specification](../docs/versioning.md) to classify revisions and the [changelog](../CHANGELOG.md) to describe them.
- Preserve earlier versions rather than replacing their historical records.
- Track specific feedback and proposed changes in repository issues, with references to the affected version and section.

The current license is `0.2.0`, an unratified, non-operative working draft. Saving or committing it does not authorize its use as a license.

## 2. Prepare the research document in Overleaf

Develop the white paper in LaTeX using Overleaf. Cover MAPLE's purpose, relevant licensing research, proposed framework, and the rationale for the corresponding license clauses.

Keep the paper aligned with the exact license version it discusses. Compile and review the PDF, then retain both the LaTeX source export and the final PDF with the version's records. Overleaf downloads these separately: the project ZIP contains the sources, while the typeset PDF is a separate download. [Overleaf export instructions](https://docs.overleaf.com/managing-projects-and-files/downloading-a-project).

License drafting, research, website preparation, and review coordination can progress in parallel. They do not require a fixed daily schedule.

## 3. Review and prepare a publication package

Before a version is published:

- Review the exact license text and paper together for contradictions, missing content, and unsupported claims.
- Check that the version in the heading, boilerplate, paper, and release description agrees.
- Identify the exact files and GitHub revision included in the package.
- Retain the non-operative notices on every `0.X.Y` license draft, including release candidates.
- Approve the files, authorship information, deposit rights, and intended visibility before publication.

A research or review publication may contain a non-operative draft. Publishing that draft does not ratify it or turn it into an operative license.

## 4. Deposit approved documents in Zenodo

Keep the development repository private. Prepare a selected package of approved publication files for a manual Zenodo deposit rather than assuming the entire repository will be archived automatically.

Create the record, upload the approved files, and enter the title, creators, resource type, version, description, reuse terms, and related references. The terms governing reuse of the deposited documents must be identified separately from the proposed MAPLE licensing terms.

Preview the record and confirm its visibility. Zenodo supports public or restricted files, but published record metadata is public. A DOI can be reserved while preparing a deposit; it is registered when the record is published. [Zenodo deposit instructions](https://help.zenodo.org/docs/deposit/create-new-upload/).

The license package and the research paper may have separate records and DOIs when they are published as separate objects. Cross-reference them and record which license version the paper explains.

## 5. Obtain external feedback

Use the publication link and DOI to invite feedback from legal reviewers, researchers, developers, and other relevant contributors.

PREreview is the review platform discussed in the meeting-notes chat. Check the eligibility of the specific research publication before submitting a request; do not assume that every deposit or DOI qualifies. Its review-request process uses a preprint DOI. [PREreview instructions](https://content.prereview.org/request-a-review-live-on-prereview/) and [supported sources](https://prereview.org/how-to-use).

Record each substantive review with its source, the version reviewed, the affected provision, and the proposed change. Public feedback and direct expert feedback both feed into the same revision process.

## 6. Evaluate feedback and create the next version

- Evaluate feedback against MAPLE's purpose, research, and intended legal behavior.
- Record whether each proposal is accepted, deferred, or declined, with a concise reason.
- Revise the license and update the corresponding paper, explanations, and changelog where affected.
- Assign the next version using the versioning specification. Do not silently change a published version's text.
- Record the new revision in GitHub, prepare the next publication package, and repeat the publication and review cycle as appropriate.

When a public website is available, update its version links, publication references, and review history to match the published records.

## 7. Ratification and later recognition

An operative release requires the formal ratification and publication conditions described in the versioning specification. A GitHub commit, Overleaf PDF, Zenodo DOI, or favorable review does not independently satisfy those conditions.

SPDX listing and OSI approval were discussed as longer-term possibilities. They are separate processes to evaluate when the license is sufficiently mature; neither is a current approval or an automatic consequence of publication.
