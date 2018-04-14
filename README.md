## Axlerod Model 4

#### List of algorithms

##### Standart

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