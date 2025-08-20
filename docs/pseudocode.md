FUNCTION SplitOddEven(numbers):
    evens ← empty list
    odds ← empty list

    FOR each number IN numbers:
        IF (number MOD 2 = 0) THEN
            ADD number TO evens
        ELSE
            ADD number TO odds
        ENDIF
    END FOR

    RETURN (evens, odds)
END FUNCTION
