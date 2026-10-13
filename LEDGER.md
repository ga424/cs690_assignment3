# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 1
artifact:  results/ambiguity_audit.md (Part 6 raw AI audit output)
tool:      Claude Code VS Code extension 2.1.296, subagent running Claude Opus 5.5 (claude-opus-5-5), 2026-10-12
prompts:   Required Part 6 ambiguity audit, run exactly once: prompts/ambiguity_audit_prompt.txt verbatim, with the full text of transcripts/interview.txt pasted after it and no other instructions
review:    Response saved complete and unedited below the starter header, with a one-line run note above it. Adjudication is in report/REPORT.md Part 6 and is not in this file. HUMAN REVIEW (Gustavo Abreu): I read the raw findings against transcripts/interview.txt. I accept the cited ambiguity and contradiction candidates as useful audit inputs, but I treated the audit as analysis rather than evidence and relied on the transcript for final classifications.
checks:    Saved by copying the returned response text; the per-line indentation added by the Claude Code harness was removed and nothing else was changed; grep -c '^\*\*[0-9]\.' results/ambiguity_audit.md -> 8 findings; the audit was not re-run
evidence:  Part 6; findings feed Q-1, Q-2, Q-3 and A-1
risk:      The model's paragraph citations were trusted only after the Part 6 adjudication; the response is a single non-deterministic sample

## Entry 2
artifact:  report/REPORT.md Parts 1 and 2 (evidence log E-1..E-6, A-1, Q-1..Q-3; seven-row evidence audit)
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), with the AISE agentic-sdlc plugin v0.3.4 orchestrate skill, 2026-10-12
prompts:   Orchestrate the assignment end to end: prompts/claude_code_orchestrate_prompt.txt
review:    Claude drafted it from transcripts/interview.txt only, with no SYN-01 sources. It checked that each E entry quotes or paraphrases its cited paragraph, logged the 15 vs 20 minute conflict as Q-1 rather than E, and merged a separate staff-hold-rule entry into E-3 to stay within 8 to 10 entries. HUMAN REVIEW (Gustavo Abreu): I read the six established claims, assumption, and questions against the cited transcript paragraphs. I accept the E versus Q treatment and the exclusion of synthetic-user material; I did not add claims from the normal pickup flow because no requirement depends on them. I note that role-based owners remain provisional where the manager or technicians were not interviewed.
checks:    Claude (not a human) cross-checked every INT-01:Pxx citation against transcripts/interview.txt while drafting; grep "SYN-01" report/REPORT.md -> matches only in the Part 6 critique, none in a Part 1 Source cell
evidence:  E-1..E-6, A-1, Q-1..Q-3; audit rows P06/P12, P07, P10, technicians, P14, P15, P13
risk:      The choice of "strongest past event" (P13 over P04) and of the two ambiguity items is a judgment call; the owner assignments are inferred from speaker roles. E-1 and A-1 were later replaced (Entry 8)

## Entry 3
artifact:  report/REPORT.md Part 3 (R-1..R-4, INVEST table, AC-1..AC-3)
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Orchestrate the assignment end to end: prompts/claude_code_orchestrate_prompt.txt
review:    The grace value is kept as a configured value G in R-1 and in every AC, not 15 or 20. AC-2 tests a time strictly before the hold end so that Q-2 is not settled. No notification requirement was written from the P10 message (then logged as A-1), because its recipient is undefined and nothing in this assignment can test it. INVEST fails are named for R-3 (E) and R-4 (I, E). HUMAN REVIEW (Gustavo Abreu): I read R-1 through R-4, their traces, and the acceptance criteria. I accept the configured-value treatment, the hold-before-end boundary, and leaving P10 as an unresolved notification question. I accept the INVEST failures rather than weakening the evidence standard; R-2 remains in the graded set because it is supported by both speakers and its invariant is testable without choosing new policy. I reject adding a student status channel as an invented requirement.
checks:    Claude confirmed by inspection that each AC is on a different requirement (R-1, R-3, R-4) and has one Given, one When and one observable Then
evidence:  R-1..R-4, AC-1..AC-3; traces E-2, E-3, E-4, E-5, E-6, Q-1, Q-2, Q-3
risk:      R-3's stored hold reason is not tested by anything in this assignment; R-4's "not yet ready" display clause was later removed (Entry 8)

## Entry 4
artifact:  spec/spec_template.md (Part 4 implementation-ready specification for R-1), also copied into report/REPORT.md Part 4
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Orchestrate the assignment end to end: prompts/claude_code_orchestrate_prompt.txt
review:    The signature parameter names were aligned with the public reference interface (documented in README.md, plus staff_hold_until from the reference docstring) so that the tests can exercise it. Behavior at exactly the hold end, and a hold ending before the grace period, are left as open questions. An open question about automatic release was removed after Part 6 judged audit finding 3 a false positive. No implementation code was added. HUMAN REVIEW (Gustavo Abreu): I compared the specification with R-1 and its acceptance criterion, checked the named parameters against README.md and the reference interface, and confirmed that the file remains a signature stub with no implementation. I accept the whole-minute boundary and the retained open questions. I rejected no additional behavior and did not infer automatic release or a fixed grace value.
checks:    Claude confirmed by inspection that the file contains only a signature stub ("...") and no function body; exactly one non-goal; every settled decision cites an E entry
evidence:  R-1; E-2, E-3, E-4, E-5; Q-1, Q-2
risk:      Edge case 1 (releasable at exactly G) relies on reading P06 "At 15 minutes ... we can release" as an inclusive boundary

## Entry 5
artifact:  tests/test_student_acceptance.py (three tests for AC-1..AC-3)
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Orchestrate the assignment end to end: prompts/claude_code_orchestrate_prompt.txt
review:    Expected values were taken from each AC's Then. The GRACE_MINUTES = 12 configured value deliberately differs from both disputed numbers (15, 20) and from SYN-01's 10. Only reservation_disposition and can_offer_to_waitlist are used, with named arguments. HUMAN REVIEW (Gustavo Abreu): I read all three tests and matched each assertion to its acceptance criterion and requirement. I accept the deliberately neutral configured value of 12, the named-argument calls, and the decision not to add tests for unresolved policy questions or R-2. I confirmed that the tests exercise the reference interface without changing reference/ or the smoke test.
checks:    python -m pytest -q -> "4 passed in 0.02s"; git diff on reference/ and tests/test_reference_smoke.py -> no changes; grep -c "^def test_" -> 3
evidence:  AC-1/R-1/E-3; AC-2/R-3/E-2,E-3; AC-3/R-4/E-5,E-6
risk:      The tests pass against the reference module, which was read for its interface. Agreement with the reference does not prove the ACs match stakeholder intent where Q-1..Q-3 are open

## Entry 6
artifact:  report/REPORT.md Part 6 (true/false-positive adjudication of the 8 audit findings; SYN-01 critique of 7 claims)
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Orchestrate the assignment end to end: prompts/claude_code_orchestrate_prompt.txt
review:    7 findings were judged true positives and 1 false positive (finding 3, automatic vs staff release: the transcript consistently describes release as a staff action). The finding 4 sub-claim that a hold's end time is unsettled was noted as overreaching (P19). The SYN-01 final paragraph and its "moving between classes" aside were excluded because INT-01 supports them. HUMAN REVIEW (Gustavo Abreu): I reviewed all eight classifications against the cited interview paragraphs and the synthetic-user critique. I agree that findings 1, 2, 4, 5, 6, 7 and 8 expose real gaps or ambiguities, while finding 3 is a false positive because release is consistently described as a staff action. I agree that P19 establishes preserving a hold end time, and that claims supported by INT-01 should not be relabeled as synthetic evidence.
checks:    Claude re-read each classification against the cited INT-01 paragraphs and checked each SYN-01 sentence against the full transcript
evidence:  Part 6; Q-1, Q-2, Q-3, A-1
risk:      The adjudication was drafted by the same model family that produced the audit, so independent human review is needed to avoid self-agreement bias

## Entry 7
artifact:  traceability/template.csv (Part 7 traceability matrix)
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Orchestrate the assignment end to end: prompts/claude_code_orchestrate_prompt.txt
review:    One row per test, with multiple evidence IDs separated by semicolons; the IDs match report Parts 1, 3 and 5. HUMAN REVIEW (Gustavo Abreu): I checked that the three CSV rows name the three student tests, that their requirement and acceptance-criterion IDs exist in the report, and that the evidence IDs correspond to the claims used by those criteria. I accept leaving R-2 untraced to an acceptance test because the assignment limits the student tests to three and the requirement is retained as an invariant.
checks:    Python check script: every test_name in the CSV has a matching def in tests/test_student_acceptance.py, and every evidence, requirement and AC ID in the CSV appears in report/REPORT.md -> "rows: 3 all ok"
evidence:  AC-1, AC-2, AC-3; R-1, R-3, R-4; E-2, E-3, E-5, E-6
risk:      R-2 has no AC or test by design (only three ACs allowed), so it is untraced to any test

## Entry 8
artifact:  Critical review revision of report/REPORT.md (Parts 1, 2, 3, 4 and 6), spec/spec_template.md, and the wording of LEDGER.md Entries 1 to 7
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Critically separate what must be validated from what is assumed, for early customer sign-off: prompts/claude_code_critical_review_prompt.txt
review:    Claude re-checked every requirement clause against the transcript and against its own Part 6 true positives. Changes:
           - E-1 replaced: the generic P02 flow, which no requirement needed, became Jordan's P19 list of what to preserve, because R-3's "store the hold end time and reason" clause had no evidence trace.
           - A-1 replaced: the P10 message recipient, which no requirement relies on, became the undefined meaning of "checked in", which R-2 and the spec rely on (audit finding 5).
           - R-4: role changed from "waitlisted student" to "checkout desk worker", because no waitlisted student was interviewed; the "not yet ready" display clause removed, because P17 and P21 disagree on what the waitlist should see.
           - R-2: INVEST E changed to fail.
           - Clarifying questions added for audit findings 2, 4, 5 and 8.
           - Spec: precondition 1 now counts only fully elapsed minutes (from P06); open questions 5 (check-in) and 6 (informal "a little late" margin) added.
           - Part 6: a "Handled in" column added, and the reasons for finding 3 and SYN-01 claim 6 tightened.
           - Ledger: Entry 2 wrongly said a "generic check-in flow" entry was dropped (a hold-rule entry was merged), Entry 3 described a notification requirement that was never written, and the checks now say who ran them.
           Not changed: R-2 was kept, although the student's strongest need (P17, know whether the reservation still stands) is not covered by R-1 to R-4; that trade-off is left to Gustavo Abreu. No AC or test changed, because none depended on the revised items. HUMAN REVIEW (Gustavo Abreu): I reviewed each listed revision against the transcript, report, specification, tests, and ledger corrections. I approve replacing E-1 with P19, replacing A-1 with the undefined check-in meaning, narrowing R-4 to a checkout desk worker and readiness gate, marking R-2's Estimable check as failed, adding the open questions and Part 6 handling column, and correcting the ledger descriptions. I choose to keep R-2 in the graded report: replacing it with a student status requirement would require an unvalidated channel and timing. I reject no listed revision.
checks:    python -m pytest -q -> 4 passed; traceability check script -> "rows: 3 all ok"; evidence log row count -> 10; Part 4 of the report compared with spec/spec_template.md by script -> identical; spec still has no function body
evidence:  E-1, A-1, R-2, R-3, R-4; audit findings 2, 4, 5, 8; Q-1, Q-2, Q-3
risk:      Precondition 1 and AC-1 still rest on one speaker's wording ("At 15 minutes ... we can release", P06); student needs rest on one student; no open question has been answered by the customer

## Entry 9
artifact:  report/SIGNOFF_BRIEF.md (customer-facing early sign-off brief: pain points, needs, wants, problem statements, requirement confidence, interpretations to confirm, decisions D1 to D9)
tool:      Claude Code VS Code extension 2.1.296, Claude Opus 5.5 (claude-opus-5-5), AISE agentic-sdlc v0.3.4, 2026-10-12
prompts:   Same request as Entry 8: prompts/claude_code_critical_review_prompt.txt
review:    Claude drafted it only from INT-01 and the revised report. Every pain point and need cites interview paragraphs, and wants (P10, P14, P15, P17, P19 and the SYN-01 ideas) are kept apart from needs. It does not pick a grace value: it notes that the 3:16 release in P13 fits a 15-minute rule or a staff judgment call. It states plainly that R-1 to R-4 cover the staff-side needs but not the student's two strongest needs. HUMAN REVIEW (Gustavo Abreu): I read the brief against the transcript and revised report, including the pain-point ranking, needs map, four proposed rules, assumptions, and D1-D9. I approve the separation of established claims, assumptions, and customer decisions; the explicit technician, manager, and borrower gaps; and the choice to keep R-2. I reject no customer-facing content, but confirm that the dashboard, running-late button, and text alerts remain proposals rather than validated requirements.
checks:    Claude re-read every paragraph the brief cites against transcripts/interview.txt and cross-checked R-1 to R-4, A-1 and Q-1 to Q-3 against report/REPORT.md
evidence:  R-1..R-4; E-1..E-6; A-1; Q-1..Q-3
risk:      The brief is not part of the graded report; its ranking of pain points is provisional until the technicians, the manager and more borrowers are heard
