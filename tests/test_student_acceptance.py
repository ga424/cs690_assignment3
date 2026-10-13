"""Student acceptance tests, one per acceptance criterion AC-1 to AC-3.

Each expected value comes from the acceptance criterion in the report, which
traces to a requirement and to INT-01 evidence. It was not read off the
reference implementation.
"""

from reference import can_offer_to_waitlist, reservation_disposition

# Configured value: the lab's grace period G, in minutes. This is a test
# setting, not settled policy. The interview disputes the real number
# (15 at INT-01:P06, 20 at INT-01:P12; see Q-1), so this deliberately uses
# neither.
GRACE_MINUTES = 12

# Configured value: how far past the grace period the staff hold in AC-2
# ends. It is a test setting, not a hold-length policy.
HOLD_MINUTES_PAST_GRACE = 10


# AC-1 (R-1; E-3)
def test_ac1_unchecked_reservation_without_hold_is_releasable_at_configured_grace() -> None:
    # Given: the lab's configured grace period is G minutes, and a reservation
    # is not checked in and has no staff hold.
    # When: the desk checks its status exactly G minutes after the start.
    state = reservation_disposition(
        minutes_after_start=GRACE_MINUTES,
        grace_minutes=GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=None,
    )
    # Then: the reservation is releasable.
    assert state == "releasable"


# AC-2 (R-3; E-2, E-3)
def test_ac2_staff_hold_keeps_reservation_held_after_grace() -> None:
    # Given: the configured grace period is G minutes, the reservation is not
    # checked in, and staff recorded a hold until G + 10 minutes after the start.
    hold_until = GRACE_MINUTES + HOLD_MINUTES_PAST_GRACE
    # When: the desk checks its status G + 5 minutes after the start, which is
    # past the grace period but before the hold ends.
    state = reservation_disposition(
        minutes_after_start=GRACE_MINUTES + 5,
        grace_minutes=GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=hold_until,
    )
    # Then: the reservation is still held, not releasable.
    assert state == "held"


# AC-3 (R-4; E-5, E-6)
def test_ac3_releasable_kit_not_offered_to_waitlist_until_prepared() -> None:
    # Given: the reservation's status is "releasable" and the equipment
    # technicians have not recorded that preparation is complete.
    # When: the system decides whether to offer the kit to the waitlist.
    offer = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    # Then: the kit is not offered to the waitlist.
    assert offer is False
