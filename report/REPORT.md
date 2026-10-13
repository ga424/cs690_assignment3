# CS 690 Assignment 3: Evidence to Executable Specification

Name: Gustavo Abreu
Commit SHA: `<fill in after the final commit: git rev-parse HEAD>`
Repository: `<public repository URL>`

## Part 1. Evidence log

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P19 | If the process moves off paper, Jordan wants preserved: the reservation start time, whether the student checked in, whether staff entered a temporary hold and until when, when the reservation became releasable, whether the kit is actually ready for the next checkout, and the reason for a manual hold. | Stated | Jordan Lee (checkout coordinator) |
| E-2 | INT-01:P04 | Yesterday a 2:00 camera kit student called at 2:08 about a lab running long. Jordan wrote "hold until 2:25" on the slip and told the other desk worker not to release it. The student arrived at 2:22 and the reservation was completed. | Observed | Jordan Lee |
| E-3 | INT-01:P06, INT-01:P21 | When the grace period after the start is reached, with no check-in and no recorded hold, staff can release the kit. The system should use whatever grace value the lab has configured, because the manager has changed the policy before. | Stated | Media Lab manager |
| E-4 | INT-01:P17, INT-01:P21 | A reservation that has been checked in should stay active, and should not disappear because the clock passes the grace window. | Stated | Jordan Lee |
| E-5 | INT-01:P09, INT-01:P21 | A released reservation does not mean the kit is ready. Technicians may need to move it back, replace a battery, or check accessories, and the waitlist should only see equipment that is actually ready to hand out. | Stated | Jordan Lee |
| E-6 | INT-01:P13 | Last Thursday, Priya's class ran until 3:11, and when she called the lab at 3:13 the line was busy twice. When she reached the desk at 3:16, her 3:00 lighting kit reservation had already been released, and a waitlisted student was waiting while technicians checked a light stand. She waited until 3:38 for another kit, and her interview started about ten minutes late. | Observed | Priya Shah (student borrower) |
| A-1 | INT-01:P02, INT-01:P17, INT-01:P21 | Assumption: "checked in" means the desk has recorded the borrower's arrival for the reservation, which can happen before the kit is handed over, so it is a separate step from "picked up". The normal flow (P02) mentions only "mark the reservation picked up", and no speaker defines check-in. | Assumption | Jordan Lee |
| Q-1 | INT-01:P06, INT-01:P12 | What grace period is actually configured, and what are students told? Jordan says the current policy is 15 minutes, and Priya says students are told 20. | Open | Media Lab manager |
| Q-2 | INT-01:P04, INT-01:P19, INT-01:P21 | When exactly does a staff hold end (is the reservation still held at the hold time itself), and does a hold that ends before the grace period cut the grace period short? | Open | Jordan Lee / Media Lab manager |
| Q-3 | INT-01:P09, INT-01:P19, INT-01:P21 | How do equipment technicians record that a released kit is prepared and ready for the next checkout? They were never interviewed. | Open | Equipment technicians |

## Part 2. Evidence audit

| Item | Location | Classification | Why it matters |
| --- | --- | --- | --- |
| Contradiction | INT-01:P06, INT-01:P12 | Direct factual contradiction: Jordan says the grace period is 15 minutes, and Priya says the desk's rule is 20 minutes. | Either figure could be current, or both could be accurate if the policy changed and students were not told (P06 says it has changed before), so only the lab manager can settle it. Requirements therefore use a configured value G and keep the conflict open as Q-1. |
| Ambiguous statement 1 | INT-01:P07 | Ambiguity: vague amount of time ("only a little late"). | No threshold is given, so an implementer could invent an informal margin on top of the configured grace period. |
| Ambiguous statement 2 | INT-01:P10 | Ambiguity: unclear who ("They") and unclear what ("it"), plus an unbounded "before". | The message's recipient and timing are undefined, so any notification rule built from this sentence would be invented. |
| Missing stakeholder | INT-01:P02, INT-01:P04, INT-01:P09, INT-01:P13, INT-01:P17, INT-01:P19, INT-01:P21 | Missing stakeholder: equipment technicians. | Waitlist readiness depends on the technicians' preparation step, yet "We have not asked them yet" (P19). Any preparation workflow written without them is a guess. |
| Compliment | INT-01:P14 | Compliment ("a reservation dashboard ... would be amazing"). | Enthusiasm is not evidence of need or behavior, so it cannot justify building a dashboard. The need it hints at, knowing whether the reservation still stands, is supported separately by P13 and P17, not by this remark. |
| Prediction about future use | INT-01:P15 | Prediction about future behavior ("I would probably use it every time"). | A hypothetical "running late" button says nothing about what students do now, so it cannot justify the button. The pain underneath it, a busy desk phone line, is real evidence in P13. |
| Strongest past event | INT-01:P13 | Specific past event (last Thursday, with timestamps 3:00, 3:11, 3:13, 3:16, 3:38, 3:52). | This concrete sequence shows the real failure points (a release before the borrower could get through, a kit not yet ready while a waitlisted student waited, scattered records). Requirements can be checked against it. |

## Part 3. Requirements, INVEST, and acceptance criteria

### Four requirement slices

**R-1. Release only after the configured grace period**
- Story: As a checkout desk worker, I want a reservation that has no check-in and no recorded hold to become releasable only once the lab's configured grace period has passed, so that late students are not lost early and kits are not held indefinitely.
- Requirement: For a reservation that is not checked in and has no staff hold, the system shall show the status "held" while the minutes since the start are less than the configured grace period G, and "releasable" once the minutes since the start equal or exceed G. G is read from lab configuration.
- Trace: E-3. The value of G stays open as Q-1. Clarifying question: do staff allow extra time beyond G when someone is "only a little late" (INT-01:P07)? R-1 does not model any such margin, and "releasable" leaves the release itself to staff.

**R-2. A checked-in reservation stays active**
- Story: As a student borrower who has checked in at the desk, I want my reservation to stay active however much time passes, so that it does not disappear because the clock passed the grace window.
- Requirement: For a reservation recorded as checked in, the system shall show the status "active" at any number of minutes after the start, including after the configured grace period, and shall never show it as "releasable".
- Trace: E-4. Assumption A-1 (what "checked in" means). Clarifying question: is check-in a desk step separate from pickup, and who records it?

**R-3. A staff hold keeps the reservation held**
- Story: As a checkout desk worker, I want to record a temporary hold with an end time and a reason, so that a student who contacted the desk keeps the reservation past the grace period.
- Requirement: For a reservation that is not checked in and has a staff hold recorded until H minutes after the start, the system shall show the status "held" at any time before H, even after the configured grace period. The system shall store the hold's end time and its reason.
- Trace: E-2, E-3, E-1. Clarifying questions: Q-2 (what happens at exactly H, and whether a hold ending before G cuts the grace period short). Who may record or extend a hold, is a reason mandatory, and is "extend a reservation" (INT-01:P21) the same thing as a hold?

**R-4. The waitlist is offered only kits that are released and ready**
- Story: As a checkout desk worker, I want a released kit offered to the waitlist only after the technicians have recorded that it is ready, so that I never promise the next borrower a kit that is still being checked.
- Requirement: The system shall offer a kit to the waitlist only when its reservation is "releasable" and the technicians have recorded its preparation as complete. A releasable kit whose preparation is not recorded as complete shall not be offered.
- Trace: E-5, E-6, E-1. Clarifying questions: Q-3 (how technicians record preparation). If the original borrower arrives after the release but before the kit is handed over, who gets it (INT-01:P13)? What, if anything, should the waitlist see for a released kit that is not yet ready? Priya asks for a "not yet ready" message (INT-01:P17), while Jordan says the waitlist should only see ready equipment (INT-01:P21).

### INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-1 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-2 | Pass | Pass | Pass | Fail | Pass | Pass | E: "checked in" is not defined as a step separate from pickup (A-1), so the work to capture it cannot be sized. |
| R-3 | Pass | Pass | Pass | Fail | Pass | Pass | E: the behavior at the hold's end and when a hold ends before the grace period is undecided (Q-2), and the rules for recording a hold are unknown, so the work cannot be sized. |
| R-4 | Fail | Pass | Pass | Fail | Pass | Pass | I: couples the waitlist offer to the technicians' preparation workflow, which has not been specified. E: the technicians' preparation signal is unknown because they were never interviewed (Q-3), and the rule for an original borrower who arrives before handover is undecided, so the work cannot be sized. |

### Three acceptance criteria

**AC-1 (R-1; E-3)**
- Given the lab's configured grace period is G minutes, and a reservation is not checked in and has no staff hold,
- When the desk checks the reservation's status exactly G minutes after its start,
- Then the status is "releasable".

**AC-2 (R-3; E-2, E-3)**
- Given the lab's configured grace period is G minutes, a reservation is not checked in, and staff recorded a hold until G + 10 minutes after the start,
- When the desk checks the reservation's status G + 5 minutes after the start,
- Then the status is "held".

**AC-3 (R-4; E-5, E-6)**
- Given a reservation's status is "releasable" and the equipment technicians have not recorded preparation as complete,
- When the system decides whether to offer the kit to the waitlist,
- Then the kit is not offered to the waitlist.

None of the three criteria settles an open question:
- AC-1 uses a configured G. Its release point at exactly G comes from INT-01:P06 ("At 15 minutes ... we can release the kit"), not from either disputed number.
- AC-2 checks a time strictly before the hold ends, which leaves Q-2 open.
- AC-3 only needs a "not complete" preparation state, however technicians record it, which leaves Q-3 open.
- AC-1 and AC-2 use reservations that are not checked in, so they do not depend on A-1.

## Part 4. Implementation-ready specification

The completed `spec/spec_template.md`, for R-1:

### Selected requirement

Requirement ID: R-1 (release disposition under the lab's configured grace period)
Evidence trace: E-3 (INT-01:P06, INT-01:P21), E-4 (INT-01:P17, INT-01:P21), E-2 (INT-01:P04), E-1 (INT-01:P19); assumption A-1 (INT-01:P02, INT-01:P17, INT-01:P21); open questions Q-1 (INT-01:P06, INT-01:P12) and Q-2 (INT-01:P04, INT-01:P19, INT-01:P21)

### Behavior and scope

Given one reservation's current facts (minutes elapsed since its start, the lab's configured grace period, whether the student has checked in, and any staff-recorded hold end time), report the reservation's release disposition: `"active"` (checked in), `"held"` (must not be released yet), or `"releasable"` (staff may release it). The function only reports a disposition. It does not release the kit, notify anyone, or decide whether the kit may be offered to the waitlist.

### Typed interface or function signature

```python
from typing import Literal

Disposition = Literal["active", "held", "releasable"]


def reservation_disposition(
    *,
    minutes_after_start: int,
    grace_minutes: int,
    checked_in: bool,
    staff_hold_until: int | None = None,
) -> Disposition: ...
```

### Preconditions

1. `minutes_after_start` counts only fully elapsed whole minutes since the reservation start (for example, 11 minutes 40 seconds is 11), so the grace period can never end before G full minutes have passed (INT-01:P06), and it is `>= 0`; a negative value raises `ValueError`.
2. `grace_minutes` is the lab's currently configured grace period, read from configuration by the caller, and is `>= 0`; a negative value raises `ValueError`. The caller never passes a hard-coded policy number.
3. `checked_in` is `True` only if the desk has recorded the borrower's check-in for this reservation. What counts as check-in is assumption A-1, not a settled fact (see open question 5).
4. `staff_hold_until` is `None` when no staff hold is recorded; otherwise it is the recorded hold end, in whole minutes after the reservation start, and is `>= 0`. A negative value raises `ValueError`.

### Postconditions

1. The return value is exactly one of `"active"`, `"held"`, or `"releasable"`.
2. If `checked_in` is `True`, the result is `"active"` for every value of `minutes_after_start`, `grace_minutes`, and `staff_hold_until`.
3. If `checked_in` is `False`, `staff_hold_until` is not `None`, and `minutes_after_start < staff_hold_until`, the result is `"held"`, even when `minutes_after_start >= grace_minutes`.
4. If `checked_in` is `False`, `staff_hold_until` is `None`, and `minutes_after_start < grace_minutes`, the result is `"held"`.
5. If `checked_in` is `False`, `staff_hold_until` is `None`, and `minutes_after_start >= grace_minutes`, the result is `"releasable"`.
6. The function does not change any stored reservation, hold, check-in, or waitlist record. Calling it again with the same arguments returns the same result.

### Invariant

A reservation whose stored check-in flag is `True` is never reported as `"releasable"`, however much time passes or whatever hold is recorded (E-4: "a checked-in reservation should remain active", INT-01:P21).

### Edge cases

1. `minutes_after_start == grace_minutes`, with no check-in and no hold: the grace period has ended, so the result is `"releasable"` (INT-01:P06, "At 15 minutes ... we can release the kit").
2. Check-in recorded after the grace period has passed, for example `minutes_after_start = grace_minutes + 30` and `checked_in=True`: the result is `"active"`, not `"releasable"`.
3. Staff hold that ends after the grace period, with the clock between the two (`grace_minutes <= minutes_after_start < staff_hold_until`): the result is `"held"`, as in the 2:25 hold at INT-01:P04.
4. `grace_minutes == 0`: no grace window. With no check-in and no hold, every `minutes_after_start >= 0` is `"releasable"`.
5. Staff hold that ends before the grace period ends (`staff_hold_until < grace_minutes`), or a clock reading exactly at the hold end (`minutes_after_start == staff_hold_until`): the result is not settled. See open questions 2 and 3. The implementation agent must not pick one.

### Non-goal

This specification does not decide whether a released kit may be offered to the waitlist. Equipment preparation readiness is covered by R-4 and depends on the technicians' workflow (Q-3).

### Settled decisions

1. The grace period is an input from lab configuration, not a constant in code, because the manager has changed it before (E-3, INT-01:P06, INT-01:P21).
2. With no check-in and no recorded hold, the reservation becomes releasable once the configured grace period has elapsed (E-3, INT-01:P06).
3. A checked-in reservation stays active and is never released by the clock (E-4, INT-01:P17, INT-01:P21).
4. A recorded staff hold keeps the reservation from being released before the hold's end time, even past the grace period (E-2, INT-01:P04; E-3, INT-01:P06 "no recorded hold"; INT-01:P17 "I would expect the hold to count").
5. "Releasable" is a release decision only. It does not mean the kit is ready for the next borrower (E-5, INT-01:P09, INT-01:P21).

### Open questions the implementation agent may not answer

Do not guess any of these. Do not pick a default, do not encode a value, and do not choose the behavior that seems most reasonable. If the code needs an answer, stop and raise the question to the named owner.

1. **What is the configured grace value? (Q-1)** Jordan says 15 minutes (INT-01:P06), and students are told 20 minutes (INT-01:P12). Owner: Media Lab manager. Read the value from configuration, and do not fall back to 15, 20, or any other default.
2. **When does a staff hold end? (Q-2)** At `minutes_after_start == staff_hold_until`, is the reservation still held, or has the hold ended? The interview only shows the student arriving before the hold time (2:22 against "hold until 2:25", INT-01:P04). Owner: Jordan Lee or the Media Lab manager.
3. **Can a hold shorten the grace period? (Q-2)** If a staff hold ends before the configured grace period ends, does the grace period still apply until it ends, or does the hold end make the reservation releasable early? Owner: Jordan Lee or the Media Lab manager.
4. **What are the rules for recording a hold?** Who may record or extend one, is there a maximum length, and is a reason mandatory? INT-01:P19 asks for the reason to be preserved, but no rule is given. INT-01:P21 says staff "extend a reservation" without saying whether that is the same mechanism as a hold. Owner: Jordan Lee or the Media Lab manager.
5. **What counts as check-in? (A-1)** Is check-in a desk step separate from pickup, and who records it? The normal flow in INT-01:P02 mentions only "mark the reservation picked up", while INT-01:P17 and INT-01:P21 rely on a "checked in" state. Owner: Jordan Lee. Take `checked_in` only from the desk's record; do not infer it from pickup, a confirmation email, or a phone call.
6. **Is there an informal margin beyond the grace period?** INT-01:P07 says staff "try not to give the kit away" when someone is "only a little late", with no threshold. Owner: Jordan Lee or the Media Lab manager. Do not add any extra minutes beyond `grace_minutes`; whether to release a `"releasable"` reservation stays a staff decision.

## Part 5. Tests

Policy values are named constants marked as configured values: `GRACE_MINUTES = 12`, deliberately neither 15 nor 20 (see Q-1), and `HOLD_MINUTES_PAST_GRACE = 10`. Each expected value comes from the acceptance criterion's Then.

| Test name | AC ID | Requirement ID | Evidence ID |
| --- | --- | --- | --- |
| `test_ac1_unchecked_reservation_without_hold_is_releasable_at_configured_grace` | AC-1 | R-1 | E-3 |
| `test_ac2_staff_hold_keeps_reservation_held_after_grace` | AC-2 | R-3 | E-2; E-3 |
| `test_ac3_releasable_kit_not_offered_to_waitlist_until_prepared` | AC-3 | R-4 | E-5; E-6 |

## Part 6. AI audit and synthetic-user critique

### Audit adjudication

The single audit run is stored unedited in `results/ambiguity_audit.md`. It was produced with `prompts/ambiguity_audit_prompt.txt`, with the transcript pasted after the prompt. The last column shows where each true positive is carried into this report, so no confirmed problem is dropped.

| # | Finding | Classification | Paragraphs | Reason | Handled in |
| --- | --- | --- | --- | --- | --- |
| 1 | Grace period length conflicts | True positive | INT-01:P06, INT-01:P12 | Jordan states 15 minutes and Priya states 20 minutes for the same rule, a real contradiction that only the lab manager can resolve. | Q-1; spec open question 1 |
| 2 | "A little late" has no definition | True positive | INT-01:P07 | "Only a little late" gives no threshold, so a second, informal margin past the configured grace could be invented. | R-1 clarifying question; spec open question 6 |
| 3 | Release may be automatic or a staff choice | False positive | INT-01:P06, INT-01:P07, INT-01:P09, INT-01:P19 | The transcript consistently describes release as a staff action that becomes permitted at the grace period ("we can release" in P06, staff discretion in P07, "We mark the reservation as released" in P09), and P19 keeps "became releasable" separate, so it does not support this ambiguity. | No defect to carry; the spec only reports a status |
| 4 | Holds, extensions and student signals not separated | True positive | INT-01:P04, INT-01:P21 | P04's written "hold until 2:25" and P21's "extend a reservation after a student contacts us" are never said to be the same mechanism, so how holds and extensions relate really is undefined (though P19 does state that a hold has an end time). | R-3 clarifying question; spec open question 4 |
| 5 | Check-in vs. pickup | True positive | INT-01:P02, INT-01:P17, INT-01:P21 | P02's normal flow has only "mark the reservation picked up", while P17 and P21 rely on a separate "checked in" state that is never defined. | A-1; R-2 clarifying question; spec open question 5 |
| 6 | The "message" in P10 has no recipient, trigger or channel | True positive | INT-01:P10 | "They should get a message before it goes to the waitlist" names no recipient and no lead time. | Part 2 ambiguity 2; no notification requirement is written |
| 7 | The kit-ready signal from technicians is unknown | True positive | INT-01:P19, INT-01:P21 | Jordan says technicians need a way to mark preparation, "We have not asked them yet," so the signal is unspecified. | Q-3; R-4 clarifying question |
| 8 | Priority when the original borrower arrives after release | True positive | INT-01:P13 | Priya arrived after release while a waitlisted student was waiting, and the transcript gives no rule for who gets the kit, only an improvised paper list. | R-4 clarifying question |

### Synthetic-user critique

Each claim in SYN-01 that INT-01 does not establish:

1. **"A likely student borrower wants the media lab reservation process to require as little staff contact as possible."** INT-01 records no preference about staff contact. Priya's stated want is to know whether she still has the reservation before crossing campus (P17), and her only comment on avoiding calls is a prediction about a hypothetical button (P15).
2. **"Students probably prefer text-message alerts over email."** Text messages are never mentioned. The only channels named are the phone, email, the desk (P10) and a confirmation email (P13), and no one states a preference.
3. **"A 10-minute grace period would likely feel fair for late arrivals."** The interview gives 15 minutes (P06) and 20 minutes (P12), never 10, and no one judges what grace length feels fair.
4. **"The strongest feature would be a QR-code self-check-in."** QR codes and self-check-in never appear. Check-in happens at the desk with a university ID (P02, P17), and no feature is ranked by real users.
5. **"...so a borrower can preserve a reservation without waiting for a desk worker."** No one reports that waiting for a desk worker cost them a reservation. Priya's lost reservation came from a class running late and a busy phone line (P13), not from a desk queue.
6. **"Students who lose a reservation are likely willing to accept a different brand of camera or light automatically, as long as the general equipment category is the same."** Brands and automatic substitution are never discussed. Priya took another lighting kit after waiting until 3:38 for one to come back (P13), which says nothing about brands or about accepting a substitute automatically.
7. **"Equipment technicians would probably prefer to receive one batch of released-reservation updates every 30 minutes instead of individual updates."** The technicians were never interviewed (P19: "We have not asked them yet"; P21), so nothing about their preferences, batching, or a 30-minute interval is established.

Not listed, because INT-01 supports them: SYN-01's final paragraph says late arrival, staff-recorded holds, checked-in reservations, equipment preparation and waitlist handoff matter (P04, P06, P09, P17, P19, P21). Its aside that students are "moving between classes" is also consistent with P07, P12 and P13.

## Part 7. Traceability and ledger

`traceability/template.csv`:

```csv
evidence_id,requirement_id,acceptance_criterion_id,test_name
E-3,R-1,AC-1,test_ac1_unchecked_reservation_without_hold_is_releasable_at_configured_grace
E-2;E-3,R-3,AC-2,test_ac2_staff_hold_keeps_reservation_held_after_grace
E-5;E-6,R-4,AC-3,test_ac3_releasable_kit_not_offered_to_waitlist_until_prepared
```

The provenance ledger is `LEDGER.md` at the repository root. The prompts it references are `prompts/ambiguity_audit_prompt.txt`, `prompts/claude_code_orchestrate_prompt.txt` and `prompts/claude_code_critical_review_prompt.txt`.

## Verification

Final output of `python -m pytest -q`:

```text
....                                                                     [100%]
4 passed in 0.02s
```
