FUNCTION StreamOddEven():
    LOOP FOREVER:
        READ number from input
        IF number IS "quit" THEN
            EXIT LOOP
        ENDIF

        IF (number MOD 2 = 0) THEN
            PRINT number + " → Even"
        ELSE
            PRINT number + " → Odd"
        ENDIF
    END LOOP
END FUNCTION
