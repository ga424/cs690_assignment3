# Early sign-off brief: late pickups, holds and waitlist handoff

Media Lab equipment reservations. Based on interview INT-01. Prepared 12 October 2026. Status: draft for your review; nothing has been built.

## What we are asking you to do

1. Confirm or correct the four rules under "What we propose to agree now".
2. Answer the nine decisions under "What we need from you". Until you do, we will not choose a grace period, a hold rule or a waitlist rule on your behalf.
3. Tell us what we got wrong. Everything here rests on one interview with two people.

## Who we heard from, and who we did not

We heard from Jordan Lee, the checkout coordinator, and Priya Shah, one student borrower, in one interview.

We have not yet heard from:

- **Equipment technicians.** Whether a kit can go to the waitlist depends on their check, and "we have not asked them yet" (P19).
- **The Media Lab manager,** who sets the grace period and has changed it before (P06).
- **Waitlisted borrowers,** who wait at the counter while a released kit is checked (P09, P13).
- **Other students.** Every student need below comes from one person.

## Pain points we heard about

Strongest evidence first. A specific past event counts for more than a general statement.

| # | Pain point | Interview | Evidence |
| --- | --- | --- | --- |
| 1 | A late student can get a hold only by getting through on the phone. Yesterday's late student called at 2:08, the desk wrote "hold until 2:25", and the student collected the kit at 2:22. Priya called at 3:13, got a busy line twice, and arrived at 3:16 to find her reservation released. | P04, P13 | Two past events |
| 2 | Students and staff may be working from different grace periods. Jordan gives the current policy as 15 minutes; Priya has been told 20 minutes, twice, and plans around it. Her reservation was gone when she arrived 16 minutes after the start. That does not show which number is right: a release by 3:16 fits a 15-minute rule or a staff judgment call. | P06, P12, P13 | Conflicting statements and one past event |
| 3 | Waitlisted borrowers wait at the counter while technicians check a released kit, and the desk cannot say when it will be ready. | P09, P13 | General statement and one past event |
| 4 | The record of a late pickup is scattered: a paper slip and a spoken instruction to another desk worker; a confirmation email, call history and paper list that "each showed only part of the sequence"; staff who "juggle the phone, email, and the person at the desk". | P04, P10, P13 | Past events and a general statement |
| 5 | There is no rule for an original borrower who arrives after the release but before the kit is handed over. Priya's kit was still behind the counter, but she was put on a paper list, waited until 3:38 for another kit, and started her interview about ten minutes late. | P13 | One past event |
| 6 | Borrowers get upset when a kit is given away while they are already walking over from another building. | P07 | Second-hand, general |

## Needs behind the pain points

| Need | Whose | Interview | Covered by |
| --- | --- | --- | --- |
| N1. Know whether my reservation still stands before I cross campus | Student | P17; pains 1 and 2 | **Not yet covered** |
| N2. Tell the desk I am running late without depending on the phone line | Student | P13; pain 1 | **Not yet covered** |
| N3. The lab's current grace period applied the same way every time, never fixed in the software | Desk staff, manager | P06, P21 | R-1 |
| N4. A checked-in reservation never lapses because of the clock | Student, desk staff | P17, P21 | R-2 |
| N5. Holds recorded with an end time and a reason, so decisions can be explained later | Desk staff | P04, P19, P21 | R-3 |
| N6. A released kit goes to the waitlist only when the technicians say it is ready | Desk staff, waitlisted borrowers | P09, P13, P21 | R-4 |
| N7. A clear rule for who gets a released kit when the original borrower turns up before it is handed over | Student, desk staff | P13; pain 5 | **Not yet covered** (decision D6) |

Our four proposed rules cover the staff-side needs, N3 to N6. N4 is a stated rule; nobody described a time it failed. The student's two strongest needs, N1 and N2, and the late-borrower rule, N7, are not covered yet. We would rather confirm them with more borrowers than guess at a solution.

## Problem statements

- A student running late from a class across campus needs to know, before setting off, whether the reservation still stands, because today the only way to check or ask for a hold is a phone line that can be busy (P12, P13, P17).
- A desk worker needs to know when a released kit is actually ready, because promising it early leaves a waitlisted borrower waiting at the counter (P09, P13).
- A desk worker needs holds recorded with an end time and a reason, because today they live on paper slips and spoken instructions, and decisions sometimes have to be explained later (P04, P19).

## Wants we heard, and why they are not in scope yet

These are reactions or proposed solutions. Each points at a real need, but none shows that the solution is the right one.

| What was said | What kind of statement it is | What it points to |
| --- | --- | --- |
| "A reservation dashboard that fixed all of this would be amazing" (P14) | A compliment | N1 |
| A "running late" button that Priya "would probably use every time" (P15) | A prediction about future use | N2. We will test the need before choosing any solution. |
| "They should get a message before it goes to the waitlist" (P10) | A proposed solution; the recipient and timing are unclear | Decision D9 |
| The system should say "not yet ready" rather than send a waitlisted borrower to the desk (P17) | A proposed solution that conflicts with "the waitlist should only see equipment that is actually ready" (P21) | Decision D7 |
| Technicians "need some way to mark the preparation step" (P19) | Jordan's suggestion on the technicians' behalf | Decision D5 |
| Text-message alerts, a 10-minute grace period, QR self-check-in, automatic swaps to another brand, technician updates batched every 30 minutes | Ideas from an AI-generated "synthetic user", not from you; none came up in the interview | Parked |

## What we propose to agree now

| Rule | In plain words | How sure we are | Waiting on |
| --- | --- | --- | --- |
| R-1 | With no check-in and no staff hold, a reservation can be released once the lab's configured grace period has passed, and not before. | Confident about the rule (P06, P21). The number is yours to set. | D1 (the number only), D8 |
| R-2 | A checked-in reservation stays active, however late it gets. | Confident the rule is wanted (P17, P21). We are assuming what "checked in" means. | D4 |
| R-3 | Staff can record a hold with an end time and a reason. Until that time, the reservation stays held, even past the grace period. | Confident about the core (P04, P19, P21). The edges are open. | D2, D3 |
| R-4 | A released kit is offered to the waitlist only after the technicians record that it is ready. | Confident it is wanted (P09, P13, P21). How the technicians record it is unknown. | D5, D6, D7 |

We have written automated checks for three of these: release at the configured grace period, a hold that outlasts the grace period, and a released kit that is not yet ready not being offered. None of them assumes a particular grace period.

### How we read the interview (please confirm)

- **"Checked in."** We assume it means the desk has recorded that the borrower arrived, which can happen before the kit is handed over, so it is a separate step from "picked up". The interview never defines it (P02, P17, P21).
- **Release stays a staff decision.** The system will show when a reservation can be released; staff still decide, as they do today (P06, P07, P09).
- **"At 15 minutes ... we can release" (P06).** We read this as: release becomes allowed when the full grace period has passed, never earlier, and part-minutes do not count.
- **One student speaks for students** until we talk to more.

## What we need from you

| # | Decision | Who decides | What waits on it |
| --- | --- | --- | --- |
| D1 | What grace period is configured today, and what are students told? | Media Lab manager | The live setting and what students hear. The rule itself (R-1) does not wait. |
| D2 | When a hold says "until 2:25", is the kit still held at 2:25? If a hold ends before the grace period would, which one applies? | Jordan Lee or the manager | R-3 |
| D3 | Who can record or extend a hold? Is there a maximum length? Is a reason required? Is "extending a reservation" (P21) the same as a hold? | Jordan Lee or the manager | R-3 |
| D4 | What does "checked in" mean, and who records it? | Jordan Lee | R-2 |
| D5 | How do technicians mark a kit ready, and what does their check cover? This needs a conversation with the technicians. | Equipment technicians | R-4 |
| D6 | If the original borrower arrives after the release but before the kit is handed over, who gets it? | Jordan Lee or the manager | R-4 |
| D7 | Should waitlisted borrowers see a released kit marked "not yet ready", or not see it at all until it is ready? | Jordan Lee | R-4 |
| D8 | When someone is "only a little late", do staff allow extra time beyond the grace period, and should the system show that? | Jordan Lee or the manager | R-1 |
| D9 | Who should get "a message before it goes to the waitlist", how long before, and how? | Jordan Lee | Any future notification work |

## Suggested next step

Talk to two or three equipment technicians (D5) and to a few more borrowers, including someone who has been on the waitlist. Ask about specific recent events rather than features:

- the last kit released while its borrower was on the way;
- the last time a waitlisted borrower waited at the counter;
- how each person found out where their reservation stood.

That is how we would test N1 and N2 before proposing any solution.
