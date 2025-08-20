FUNCTION OddOrEvenList(numbers):
    results ← empty list
    FOR each number IN numbers:
        IF (number MOD 2 = 0) THEN
            ADD (number + " → Even") TO results
        ELSE
            ADD (number + " → Odd") TO results
        ENDIF
    END FOR
    RETURN results
END FUNCTION
