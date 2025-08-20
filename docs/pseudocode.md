FUNCTION LogOddEvenStream():
    OPEN file "evens.txt" (append mode)
    OPEN file "odds.txt" (append mode)

    LOOP FOREVER:
        random_number ← generate random integer
        
        IF (random_number MOD 2 = 0) THEN
            WRITE random_number TO "evens.txt"
            PRINT random_number + " → Even"
        ELSE
            WRITE random_number TO "odds.txt"
            PRINT random_number + " → Odd"
        ENDIF

        WAIT for 1 second
    END LOOP
END FUNCTION
