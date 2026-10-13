# Implementation-ready specification

## Selected requirement

Requirement ID: R-1 (release disposition under the lab's configured grace period)
Evidence trace: E-3 (INT-01:P06, INT-01:P21), E-4 (INT-01:P17, INT-01:P21), E-2 (INT-01:P04), E-1 (INT-01:P19); assumption A-1 (INT-01:P02, INT-01:P17, INT-01:P21); open questions Q-1 (INT-01:P06, INT-01:P12) and Q-2 (INT-01:P04, INT-01:P19, INT-01:P21)

## Behavior and scope

Given one reservation's current facts (minutes elapsed since its start, the lab's configured grace period, whether the student has checked in, and any staff-recorded hold end time), report the reservation's release disposition: `"active"` (checked in), `"held"` (must not be released yet), or `"releasable"` (staff may release it). The function only reports a disposition. It does not release the kit, notify anyone, or decide whether the kit may be offered to the waitlist.

## Typed interface or function signature

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

## Preconditions

1. `minutes_after_start` counts only fully elapsed whole minutes since the reservation start (for example, 11 minutes 40 seconds is 11), so the grace period can never end before G full minutes have passed (INT-01:P06), and it is `>= 0`; a negative value raises `ValueError`.
2. `grace_minutes` is the lab's currently configured grace period, read from configuration by the caller, and is `>= 0`; a negative value raises `ValueError`. The caller never passes a hard-coded policy number.
3. `checked_in` is `True` only if the desk has recorded the borrower's check-in for this reservation. What counts as check-in is assumption A-1, not a settled fact (see open question 5).
4. `staff_hold_until` is `None` when no staff hold is recorded; otherwise it is the recorded hold end, in whole minutes after the reservation start, and is `>= 0`. A negative value raises `ValueError`.

## Postconditions

1. The return value is exactly one of `"active"`, `"held"`, or `"releasable"`.
2. If `checked_in` is `True`, the result is `"active"` for every value of `minutes_after_start`, `grace_minutes`, and `staff_hold_until`.
3. If `checked_in` is `False`, `staff_hold_until` is not `None`, and `minutes_after_start < staff_hold_until`, the result is `"held"`, even when `minutes_after_start >= grace_minutes`.
4. If `checked_in` is `False`, `staff_hold_until` is `None`, and `minutes_after_start < grace_minutes`, the result is `"held"`.
5. If `checked_in` is `False`, `staff_hold_until` is `None`, and `minutes_after_start >= grace_minutes`, the result is `"releasable"`.
6. The function does not change any stored reservation, hold, check-in, or waitlist record. Calling it again with the same arguments returns the same result.

## Invariant

A reservation whose stored check-in flag is `True` is never reported as `"releasable"`, however much time passes or whatever hold is recorded (E-4: "a checked-in reservation should remain active", INT-01:P21).

## Edge cases

1. `minutes_after_start == grace_minutes`, with no check-in and no hold: the grace period has ended, so the result is `"releasable"` (INT-01:P06, "At 15 minutes ... we can release the kit").
2. Check-in recorded after the grace period has passed, for example `minutes_after_start = grace_minutes + 30` and `checked_in=True`: the result is `"active"`, not `"releasable"`.
3. Staff hold that ends after the grace period, with the clock between the two (`grace_minutes <= minutes_after_start < staff_hold_until`): the result is `"held"`, as in the 2:25 hold at INT-01:P04.
4. `grace_minutes == 0`: no grace window. With no check-in and no hold, every `minutes_after_start >= 0` is `"releasable"`.
5. Staff hold that ends before the grace period ends (`staff_hold_until < grace_minutes`), or a clock reading exactly at the hold end (`minutes_after_start == staff_hold_until`): the result is not settled. See open questions 2 and 3. The implementation agent must not pick one.

## Non-goal

This specification does not decide whether a released kit may be offered to the waitlist. Equipment preparation readiness is covered by R-4 and depends on the technicians' workflow (Q-3).

## Settled decisions

1. The grace period is an input from lab configuration, not a constant in code, because the manager has changed it before (E-3, INT-01:P06, INT-01:P21).
2. With no check-in and no recorded hold, the reservation becomes releasable once the configured grace period has elapsed (E-3, INT-01:P06).
3. A checked-in reservation stays active and is never released by the clock (E-4, INT-01:P17, INT-01:P21).
4. A recorded staff hold keeps the reservation from being released before the hold's end time, even past the grace period (E-2, INT-01:P04; E-3, INT-01:P06 "no recorded hold"; INT-01:P17 "I would expect the hold to count").
5. "Releasable" is a release decision only. It does not mean the kit is ready for the next borrower (E-5, INT-01:P09, INT-01:P21).

## Open questions the implementation agent may not answer

Do not guess any of these. Do not pick a default, do not encode a value, and do not choose the behavior that seems most reasonable. If the code needs an answer, stop and raise the question to the named owner.

1. **What is the configured grace value? (Q-1)** Jordan says 15 minutes (INT-01:P06), and students are told 20 minutes (INT-01:P12). Owner: Media Lab manager. Read the value from configuration, and do not fall back to 15, 20, or any other default.
2. **When does a staff hold end? (Q-2)** At `minutes_after_start == staff_hold_until`, is the reservation still held, or has the hold ended? The interview only shows the student arriving before the hold time (2:22 against "hold until 2:25", INT-01:P04). Owner: Jordan Lee or the Media Lab manager.
3. **Can a hold shorten the grace period? (Q-2)** If a staff hold ends before the configured grace period ends, does the grace period still apply until it ends, or does the hold end make the reservation releasable early? Owner: Jordan Lee or the Media Lab manager.
4. **What are the rules for recording a hold?** Who may record or extend one, is there a maximum length, and is a reason mandatory? INT-01:P19 asks for the reason to be preserved, but no rule is given. INT-01:P21 says staff "extend a reservation" without saying whether that is the same mechanism as a hold. Owner: Jordan Lee or the Media Lab manager.
5. **What counts as check-in? (A-1)** Is check-in a desk step separate from pickup, and who records it? The normal flow in INT-01:P02 mentions only "mark the reservation picked up", while INT-01:P17 and INT-01:P21 rely on a "checked in" state. Owner: Jordan Lee. Take `checked_in` only from the desk's record; do not infer it from pickup, a confirmation email, or a phone call.
6. **Is there an informal margin beyond the grace period?** INT-01:P07 says staff "try not to give the kit away" when someone is "only a little late", with no threshold. Owner: Jordan Lee or the Media Lab manager. Do not add any extra minutes beyond `grace_minutes`; whether to release a `"releasable"` reservation stays a staff decision.
