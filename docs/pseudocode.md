FUNCTION OddOrEvenList(numbers):
    FOR each number IN numbers:
        IF (number MOD 2 = 0) THEN
            PRINT number + " → Even"
        ELSE
            PRINT number + " → Odd"
        ENDIF
    END FOR
END FUNCTION
