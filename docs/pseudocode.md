FUNCTION RandomOddEvenStream():
    LOOP FOREVER:
        random_number ← generate random integer
        IF (random_number MOD 2 = 0) THEN
            PRINT random_number + " → Even"
        ELSE
            PRINT random_number + " → Odd"
        ENDIF
        WAIT for a short delay (e.g., 1 second)
    END LOOP
END FUNCTION
