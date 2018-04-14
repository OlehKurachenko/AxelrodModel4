## Axlerod Model 4

### List of algorithms

#### Standart

1. **eye_for_eye**
    - step: _first step 5, next step the same as competitors previous_
    - analysis: _none_
    - reproduction rule: _none_
2. **random**
    - step: _random_
    - analysis: _none_
    - reproduction rule: _none_
3. **envy**
    - step: _1 every time_
    - analysis: _none_
    - reproduction rule: _none_
4. **analysis**
    - step: _first 5 turns are {3, 5, 1, 4, 2} to test behaviour of oponent. It
    it is eye-for-eye then all turns will be 5, if all are the same - 1,
    else - random._
    - analysis: _none_
    - reproduction rule: _none_
5. **mutable_constant**
    - step: _contant depending on data content_
    - analysis: _none_
    - reproduction _rule: 3/5 of population will have the same constant step
    value as parent, 1/5 - +1 (if possible), 1/5 - -1, randomly_
    
#### Gen 2018

1. **vitalia**
    - step: _first step: 3, all next: competitor-1_
    - analysis: _none_
    - reproduction rule: _none_
    
2. **kt-1**
    - step: _first step: random, then, the next loop for each 6 steps:_
        - 1, 3: competitor+2
        - 2, 4: competitor-2
        - 5: 6 - (competitor on loop step 2)
        - 6: 6 - (competitor on loop step 3)
    - analysis: _none_
    - reproduction rule: _none_
    
3. **kt-2**
    - step: _first step: 3, all next: 6 - competitor_
    - analysis: _none_
    - reproduction rule: _none_
    
4. **bb1601**
    - step: _in loop for each 8 steps:_
        - 1: random
        - 2: 3
        - 3: competitor-1
        - 4: competitor-1
        - 5: 4
        - 6: 2
        - 7: competitor+1
        - 8: competitor+1
    - analysis: _none_
    - reproduction rule: _none_
    
5. **may048be**
    - step: _in loop for each 6 steps:_
        - 1: 3
        - 2: competitor-1
        - 3: competitor+1
        - 4: 4
        - 5: 3
        - 6: competitor-1
    - analysis: _none_
    - reproduction rule: _none_
    
6. **andrew**
    - step: _in loop for each 5 steps:_
        - 1: 3
        - 2: competitor-1
        - 3: competitor+1
        - 4: 3
        - 5: competitor-1
    - analysis: _none_
    - reproduction rule: _none_
    
7. **illya-a**
    - step: first step: 3, then [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]
    - analysis: _none_
    - reproduction rule: _none_
    
8. **illya-b**
    - step: first step: 4, then [1, 2, 3, 4, 5] -> [3, 4, 5, 4, 2]
    - analysis: _none_
    - reproduction rule: _none_
    
9. **illya-c**
    - step: first step: 5, then [1, 2, 3, 4, 5] -> [5, 3, 1, 5, 3]
    - analysis: _none_
    - reproduction rule: _none_
    
10. **sergey-a**
    - step: _in loop for each 5 steps:_
        - 1: 3
        - 2: 3
        - 3: 4
        - 4: 3
        - 5: 4
    - analysis: _none_
    - reproduction rule: _none_
    
11. **novy_misha**
    - step: _in loop for each 3 steps:_
        - 1: 3
        - 2-3: competitor-1
    - analysis: _none_
    - reproduction rule: _none_
    
12. **anya**
    - step: _in loop for each 4 steps:_
        - 1: 4
        - 2: competitor-1
        - 3: 3
        - 4: competitor-1
    - analysis: _none_
    - reproduction rule: _none_
    
13. **ki**
    - step: _steps 1-7: 2. Then, if there were 3 the same in row, 2 on 3-5,
    1 on 1-2. Else 1 in any case._
    - analysis: _none_
    - reproduction rule: _none_